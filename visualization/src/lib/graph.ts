import * as d3 from 'd3';
import type { DefGraph, DefNode, LearnState, Pos, Raw, TreeNode } from '../types';
import { COLOR_OFF, COLOR_VISIBLE, COLOR_READY, COLOR_LEARNED } from './constants';

/* ------------------------------------------------------------------ */
/*  Utility helpers                                                    */
/* ------------------------------------------------------------------ */

export function normalizeId(s: string): string {
  return s
    .trim()
    .toLowerCase()
    .replace(/\s+/g, '_')
    .replace(/[^a-z0-9_\-\/]/g, '');
}

export function splitCategory(category: string): string[] {
  return category.split('/').filter(Boolean);
}

export function groupIdForPath(parts: string[], depth: number): string {
  return parts.slice(0, depth).join('/');
}

function hash01(s: string): number {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return (h >>> 0) / 0xffffffff;
}

function textWidthPx(text: string): number {
  return Math.max(24, text.length * 7.2);
}

/* ------------------------------------------------------------------ */
/*  Learn state                                                        */
/* ------------------------------------------------------------------ */

export function learnStateForNode(n: DefNode, learned: Set<string>): LearnState {
  if (learned.has(n.id)) return 'learned';
  const deps = n.deps ?? [];
  if (deps.every((d) => learned.has(d))) return 'ready';
  return 'off';
}

export function colorForLearnState(s: LearnState): string {
  if (s === 'learned') return COLOR_LEARNED;
  if (s === 'ready') return COLOR_READY;
  if (s === 'visible') return COLOR_VISIBLE;
  return COLOR_OFF;
}

export function learnStateRank(s: LearnState): number {
  if (s === 'ready') return 0;
  if (s === 'learned') return 1;
  if (s === 'visible') return 2;
  return 3;
}

/* ------------------------------------------------------------------ */
/*  Visible-set computation (nodes with at least one "on" incoming edge) */
/* ------------------------------------------------------------------ */

export function computeVisibleSet(graph: DefGraph, learned: Set<string>): Set<string> {
  const visible = new Set<string>();
  const byId = new Map(graph.nodes.map((n) => [n.id, n] as const));

  for (const e of graph.edges) {
    const prereq = byId.get(e.target);
    if (!prereq) continue;
    if (learnStateForNode(prereq, learned) !== 'learned') continue;

    const dep = byId.get(e.source);
    if (!dep) continue;
    if (learnStateForNode(dep, learned) === 'off') visible.add(dep.id);
  }
  return visible;
}

export function effectiveState(n: DefNode, learned: Set<string>, visibleSet: Set<string>): LearnState {
  const base = learnStateForNode(n, learned);
  return base === 'off' && visibleSet.has(n.id) ? 'visible' : base;
}

/* ------------------------------------------------------------------ */
/*  Level computation                                                  */
/* ------------------------------------------------------------------ */

export function computeLevels(nodes: DefNode[]): void {
  const byId = new Map(nodes.map((n) => [n.id, n] as const));
  const visiting = new Set<string>();
  const visited = new Set<string>();

  const dfs = (id: string): number => {
    const n = byId.get(id);
    if (!n) return 0;
    if (visited.has(id)) return n.level ?? 0;
    if (visiting.has(id)) return 0;

    visiting.add(id);
    let level = 0;
    for (const depId of n.deps ?? []) {
      if (!byId.has(depId)) continue;
      level = Math.max(level, 1 + dfs(depId));
    }
    visiting.delete(id);
    visited.add(id);
    n.level = level;
    return level;
  };

  for (const n of nodes) dfs(n.id);
}

/* ------------------------------------------------------------------ */
/*  Group-level computation (category DAG)                             */
/* ------------------------------------------------------------------ */

export function computeGroupLevels(raw: Raw): {
  depsByGroup: Map<string, Set<string>>;
  levelByGroup: Map<string, number>;
} {
  const groups = new Set<string>(raw.childrenByPrefix.keys());
  const depsByGroup = new Map<string, Set<string>>();
  for (const g of groups) depsByGroup.set(g, new Set());

  const groupOfLeafAtDepth = (leafCategory: string, depth: number) => {
    const parts = splitCategory(leafCategory);
    if (depth > parts.length - 1) return null;
    return groupIdForPath(parts, depth);
  };

  for (const n of raw.def.nodes) {
    const srcParts = splitCategory(n.category);

    for (const depId of n.deps ?? []) {
      const depCategory = raw.byId.get(depId)?.category;
      if (!depCategory) continue;

      const depParts = splitCategory(depCategory);
      const maxDepth = Math.min(srcParts.length - 1, depParts.length - 1);

      for (let d = 1; d <= maxDepth; d++) {
        const a = groupOfLeafAtDepth(n.category, d);
        const b = groupOfLeafAtDepth(depCategory, d);
        if (!a || !b || a === b) continue;
        depsByGroup.get(a)?.add(b);
      }
    }
  }

  const levelByGroup = new Map<string, number>();
  const visiting = new Set<string>();
  const visited = new Set<string>();

  const dfs = (g: string): number => {
    if (levelByGroup.has(g)) return levelByGroup.get(g)!;
    if (visited.has(g)) return levelByGroup.get(g) ?? 0;
    if (visiting.has(g)) return 0;

    visiting.add(g);
    let lvl = 0;
    for (const dep of depsByGroup.get(g) ?? []) {
      lvl = Math.max(lvl, dfs(dep) + 1);
    }
    visiting.delete(g);
    visited.add(g);
    levelByGroup.set(g, lvl);
    return lvl;
  };

  for (const g of groups) dfs(g);

  return { depsByGroup, levelByGroup };
}

/* ------------------------------------------------------------------ */
/*  Build Raw from DefGraph                                            */
/* ------------------------------------------------------------------ */

export function buildRaw(def: DefGraph): Raw {
  const byId = new Map(def.nodes.map((n) => [n.id, n] as const));

  const fieldsSet = new Set<string>();
  for (const n of def.nodes) {
    const [field] = splitCategory(n.category);
    if (field) fieldsSet.add(field);
  }
  const fields = Array.from(fieldsSet).sort();

  const childrenByPrefix = new Map<string, string[]>();
  for (const n of def.nodes) {
    const parts = splitCategory(n.category);
    for (let d = 1; d <= parts.length - 1; d++) {
      const prefix = groupIdForPath(parts, d);
      const arr = childrenByPrefix.get(prefix) ?? [];
      arr.push(n.id);
      childrenByPrefix.set(prefix, arr);
    }
  }

  for (const [k, arr] of childrenByPrefix) {
    childrenByPrefix.set(k, Array.from(new Set(arr)).sort());
  }

  return { def, byId, childrenByPrefix, fields };
}

/* ------------------------------------------------------------------ */
/*  renderGraph – project the full graph with visibility filtering      */
/* ------------------------------------------------------------------ */

export function renderGraph(raw: Raw, includedIds: Set<string> | null): DefGraph {
  const isIncluded = (id: string) => (!includedIds ? true : includedIds.has(id));

  const nodes = raw.def.nodes
    .filter((n) => isIncluded(n.id))
    .map((n) => ({ ...n, level: 0 }));

  const nodeSet = new Set(nodes.map((n) => n.id));
  const edges = raw.def.edges
    .filter((e) => nodeSet.has(e.source) && nodeSet.has(e.target))
    .map((e) => ({ ...e }));

  const depsByNode = new Map<string, string[]>();
  for (const e of edges) {
    const arr = depsByNode.get(e.source) ?? [];
    arr.push(e.target);
    depsByNode.set(e.source, arr);
  }
  for (const n of nodes) {
    n.deps = depsByNode.get(n.id) ?? (n.deps ?? []);
    n.level = 0;
  }

  computeLevels(nodes);
  return { nodes, edges };
}

/* ------------------------------------------------------------------ */
/*  Recompute included set from ready nodes                            */
/* ------------------------------------------------------------------ */

export function recomputeIncludedSetFromReady(
  raw: Raw,
  learned: Set<string>,
): Set<string> | null {
  const readyParentPrefixes = new Set<string>();

  for (const n of raw.def.nodes) {
    if (learnStateForNode(n, learned) !== 'ready') continue;
    const parts = splitCategory(n.category);
    const parentDepth = Math.max(1, parts.length - 1);
    const parent = groupIdForPath(parts, parentDepth);
    if (parent) readyParentPrefixes.add(parent);
  }

  if (!readyParentPrefixes.size) return null;

  const included = new Set<string>();

  for (const n of raw.def.nodes) {
    if (learnStateForNode(n, learned) === 'learned') included.add(n.id);
  }

  for (const leaf of raw.def.nodes) {
    const parts = splitCategory(leaf.category);
    const parentDepth = Math.max(1, parts.length - 1);
    const parent = groupIdForPath(parts, parentDepth);
    if (parent && readyParentPrefixes.has(parent)) included.add(leaf.id);
  }

  return included;
}

/* ------------------------------------------------------------------ */
/*  Select next ready definition                                       */
/* ------------------------------------------------------------------ */

export function selectNextReady(
  raw: Raw,
  rendered: DefGraph,
  learned: Set<string>,
): string | null {
  computeLevels(rendered.nodes);
  const ready = rendered.nodes.filter((n) => learnStateForNode(n, learned) === 'ready');
  if (!ready.length) return null;

  const { levelByGroup } = computeGroupLevels(raw);
  const parentGroupLevel = (category: string) => {
    const parts = splitCategory(category);
    const parentDepth = Math.max(1, parts.length - 1);
    const parent = groupIdForPath(parts, parentDepth);
    return parent ? (levelByGroup.get(parent) ?? 0) : 0;
  };

  ready.sort((a, b) => {
    const la = a.level ?? 0;
    const lb = b.level ?? 0;
    if (la !== lb) return la - lb;
    const ga = parentGroupLevel(a.category);
    const gb = parentGroupLevel(b.category);
    if (ga !== gb) return ga - gb;
    return a.id.localeCompare(b.id);
  });

  return ready[0].id;
}

/* ------------------------------------------------------------------ */
/*  Build Category Tree                                                */
/* ------------------------------------------------------------------ */

export function buildCategoryTree(
  raw: Raw,
  rendered: DefGraph,
  learned: Set<string>,
): { root: TreeNode; visibleNodeIds: Set<string> } {
  const visibleNodeIds = computeVisibleSet(rendered, learned);
  const { levelByGroup } = computeGroupLevels(raw);

  const root: TreeNode = { id: '', name: '', kind: 'group', depth: 0, children: [], groupLevel: 0 };

  for (const leaf of raw.def.nodes) {
    const parts = splitCategory(leaf.category);
    let cur = root;
    for (let i = 0; i < parts.length - 1; i++) {
      const prefix = parts.slice(0, i + 1).join('/');
      let child = cur.children.find((c) => c.kind === 'group' && c.id === prefix);
      if (!child) {
        child = {
          id: prefix,
          name: parts[i],
          kind: 'group',
          depth: i + 1,
          children: [],
          groupLevel: levelByGroup.get(prefix) ?? 0,
        };
        cur.children.push(child);
      } else {
        child.groupLevel = levelByGroup.get(prefix) ?? child.groupLevel ?? 0;
      }
      cur = child;
    }

    const leafNode: TreeNode = {
      id: leaf.id,
      name: parts.at(-1) ?? leaf.id,
      kind: 'leaf',
      depth: parts.length,
      children: [],
      leaf: raw.byId.get(leaf.id) ?? leaf,
    };
    cur.children.push(leafNode);
  }

  const stateForCat = (leaf: DefNode): LearnState => {
    const base = learnStateForNode(leaf, learned);
    return base === 'off' && visibleNodeIds.has(leaf.id) ? 'visible' : base;
  };

  const sortChildren = (n: TreeNode) => {
    for (const c of n.children) sortChildren(c);

    n.children.sort((a, b) => {
      if (a.kind !== b.kind) return a.kind === 'group' ? -1 : 1;

      if (a.kind === 'group' && b.kind === 'group') {
        const la = a.groupLevel ?? 0;
        const lb = b.groupLevel ?? 0;
        if (la !== lb) return la - lb;
        return a.name.localeCompare(b.name);
      }

      const la = a.leaf!;
      const lb = b.leaf!;
      const sa = stateForCat(la);
      const sb = stateForCat(lb);
      const ra = learnStateRank(sa);
      const rb = learnStateRank(sb);
      if (ra !== rb) return ra - rb;
      const da = la.level ?? 0;
      const db = lb.level ?? 0;
      if (da !== db) return da - db;
      return (la.title ?? la.id).localeCompare(lb.title ?? lb.id);
    });
  };

  sortChildren(root);

  return { root, visibleNodeIds };
}

/* ------------------------------------------------------------------ */
/*  Radial layout                                                      */
/* ------------------------------------------------------------------ */

export type RadialLayout = {
  cx: number;
  cy: number;
  ringGap: number;
  base: number;
  maxLevel: number;
  pos: Map<string, Pos>;
};

export function radialLayout(graph: DefGraph, width: number, height: number): RadialLayout {
  const cx = width / 2;
  const cy = height / 2;
  const maxLevel = Math.max(0, ...graph.nodes.map((n) => n.level ?? 0));
  const maxLabel = Math.max(6, ...graph.nodes.map((n) => n.title?.length ?? 0));
  const ringGap = Math.max(54, Math.min(120, 30 + maxLabel * 2.4));
  const base = 56;

  const byLevel = d3.group(graph.nodes, (n: DefNode) => n.level ?? 0);
  const placed = new Map<string, Pos>();

  const levelOffset = (level: number) =>
    (hash01(String(level)) * 0.9 + level * 0.37) % (Math.PI * 2);

  const relaxAngles = (nodes: DefNode[], r: number, baseAngles: number[]) => {
    if (nodes.length <= 1) return baseAngles;
    const angles = baseAngles.slice();
    const widths = nodes.map((n) => textWidthPx(n.title));
    const need = widths.map((w) => (w + 18) / Math.max(1, r));

    for (let it = 0; it < 22; it++) {
      const idx = d3.range(nodes.length).sort((a, b) => angles[a] - angles[b]);
      for (let j = 0; j < idx.length; j++) {
        const a = idx[j];
        const b = idx[(j + 1) % idx.length];
        let da = angles[b] - angles[a];
        if (da < 0) da += Math.PI * 2;
        const minSep = (need[a] + need[b]) / 2;
        if (da < minSep) {
          const push = (minSep - da) / 2;
          angles[a] -= push;
          angles[b] += push;
        }
      }
    }

    for (let i = 0; i < angles.length; i++) {
      angles[i] = ((angles[i] % (Math.PI * 2)) + Math.PI * 2) % (Math.PI * 2);
    }
    return angles;
  };

  for (let level = 0; level <= maxLevel; level++) {
    const nodes = ((byLevel.get(level) ?? []) as DefNode[])
      .slice()
      .sort((a, b) => a.id.localeCompare(b.id));
    const count = nodes.length;
    if (!count) continue;

    const r = base + level * ringGap;
    const baseOff = levelOffset(level);

    let baseAngles: number[];
    if (count === 2) {
      baseAngles = [baseOff + Math.PI / 4, baseOff + Math.PI + Math.PI / 4];
    } else if (count === 3) {
      baseAngles = [0, 1, 2].map((i) => baseOff + (i / 3) * Math.PI * 2 + Math.PI / 6);
    } else {
      baseAngles = nodes.map((_n, i) => baseOff + (i / count) * Math.PI * 2);
    }

    const angles = relaxAngles(nodes, r, baseAngles);

    for (let i = 0; i < count; i++) {
      placed.set(nodes[i].id, {
        x: cx + r * Math.cos(angles[i]),
        y: cy + r * Math.sin(angles[i]),
      });
    }
  }

  return { cx, cy, ringGap, base, maxLevel, pos: placed };
}

/* ------------------------------------------------------------------ */
/*  Progress stats computation                                         */
/* ------------------------------------------------------------------ */

export function computeStats(
  raw: Raw,
  rendered: DefGraph,
  learned: Set<string>,
): { totalDefs: number; learnedDefs: number; totalEdges: number; unlockedEdges: number; totalLevels: number; completedLevels: number } {
  // Filtered stats: only count what is in `rendered` (i.e. what passes current filters)
  const renderedIds = new Set(rendered.nodes.map((n) => n.id));

  const totalDefs = rendered.nodes.length;
  const learnedDefs = rendered.nodes.reduce((acc, n) => acc + (learned.has(n.id) ? 1 : 0), 0);

  const totalEdges = rendered.edges.length;
  const unlockedEdges = rendered.edges.reduce(
    (acc, e) => acc + (learned.has(e.target) ? 1 : 0),
    0,
  );

  const maxTotalLevel = Math.max(0, ...rendered.nodes.map((n) => n.level ?? 0));

  const totalCountByLevel = new Map<number, number>();
  const learnedCountByLevel = new Map<number, number>();

  for (const n of rendered.nodes) {
    const lvl = n.level ?? 0;
    totalCountByLevel.set(lvl, (totalCountByLevel.get(lvl) ?? 0) + 1);
    if (learned.has(n.id)) {
      learnedCountByLevel.set(lvl, (learnedCountByLevel.get(lvl) ?? 0) + 1);
    }
  }

  let completedLevels = 0;
  for (let lvl = 0; lvl <= maxTotalLevel; lvl++) {
    const total = totalCountByLevel.get(lvl) ?? 0;
    if (!total) continue;
    if ((learnedCountByLevel.get(lvl) ?? 0) === total) completedLevels++;
  }

  return {
    totalDefs,
    learnedDefs,
    totalEdges,
    unlockedEdges,
    totalLevels: maxTotalLevel + 1,
    completedLevels,
  };
}

/* ------------------------------------------------------------------ */
/*  Markdown content helpers                                           */
/* ------------------------------------------------------------------ */

export function escapeHtml(s: string): string {
  return s
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

export function normalizeMdForViewer(md: string): string {
  const lines = md.replace(/\r\n?/g, '\n').split('\n');
  const out: string[] = [];

  let i = 0;
  while (i < lines.length && !lines[i].trim()) i++;
  if (i < lines.length && /^#{1,2}\s+/.test(lines[i].trim())) i++;

  for (; i < lines.length; i++) out.push(lines[i]);

  while (out.length && !out[0].trim()) out.shift();
  while (out.length && !out[out.length - 1].trim()) out.pop();

  const collapsed: string[] = [];
  let blank = 0;
  for (const l of out) {
    if (!l.trim()) {
      blank++;
      if (blank <= 2) collapsed.push('');
      continue;
    }
    blank = 0;
    collapsed.push(l);
  }

  return collapsed.join('\n');
}

export function renderMdToHtml(
  md: string,
  deps: string[],
  renderedNodes: DefNode[],
): string {
  const clean = normalizeMdForViewer(md);
  const byId = new Map(renderedNodes.map((n) => [n.id, n] as const));
  const depMap = new Map<string, { id: string; title: string }>();
  for (const id of deps) {
    const t = byId.get(id)?.title ?? id.split('/').at(-1) ?? id;
    depMap.set(id, { id, title: t });
  }

  const linkRe = /\[([^\]]+)\]\(([^)]+)\)/g;

  const replaced = clean.replace(linkRe, (_m, labelRaw, hrefRaw) => {
    const label = String(labelRaw ?? '').trim();
    const href = String(hrefRaw ?? '').trim();

    let depId: string | undefined;
    if (depMap.has(href)) depId = href;

    if (!depId && href.includes('/')) {
      const suffix = '/' + href.split('/').filter(Boolean).pop();
      const field = href.split('/')[0];
      const candidates = Array.from(depMap.keys()).filter(
        (id) => id.startsWith(field + '/') && id.endsWith(suffix),
      );
      if (candidates.length === 1) depId = candidates[0];
    }

    if (!depId) return escapeHtml(label || href);

    const dep = depMap.get(depId)!;
    return `<span class="dep" data-dep="${escapeHtml(dep.id)}">${escapeHtml(dep.title)}</span>`;
  });

  const paragraphs = replaced
    .split(/\n\s*\n+/g)
    .map((p) => p.replace(/\s*\n\s*/g, ' ').trim())
    .filter(Boolean);

  return paragraphs.map((p) => `<p>${p}</p>`).join('');
}

/* ------------------------------------------------------------------ */
/*  Search filtering helpers                                           */
/* ------------------------------------------------------------------ */

type WalkDir = 'deps' | 'dependents';

function walkGraph(raw: Raw, startId: string, dir: WalkDir): Set<string> {
  const out = new Set<string>();
  const stack: string[] = [startId];

  // Build adjacency
  const nextById = new Map<string, string[]>();
  for (const n of raw.def.nodes) nextById.set(n.id, []);

  if (dir === 'deps') {
    for (const n of raw.def.nodes) {
      nextById.set(n.id, (n.deps ?? []).filter((d) => raw.byId.has(d)));
    }
  } else {
    // dependents: dep -> list of nodes that depend on dep
    for (const n of raw.def.nodes) {
      for (const dep of n.deps ?? []) {
        if (!raw.byId.has(dep)) continue;
        const arr = nextById.get(dep) ?? [];
        arr.push(n.id);
        nextById.set(dep, arr);
      }
    }
  }

  while (stack.length) {
    const id = stack.pop()!;
    if (out.has(id)) continue;
    if (!raw.byId.has(id)) continue;
    out.add(id);
    for (const nxt of nextById.get(id) ?? []) stack.push(nxt);
  }

  return out;
}

/** All prerequisites needed before `id` can be learned (including `id` itself). */
export function prerequisiteClosure(raw: Raw, id: string): Set<string> {
  return walkGraph(raw, id, 'deps');
}

/** All definitions that (transitively) depend on `id` (including `id` itself). */
export function dependentClosure(raw: Raw, id: string): Set<string> {
  return walkGraph(raw, id, 'dependents');
}

/** Intersection helper that handles nulls. */
export function intersectSets(a: Set<string>, b: Set<string>): Set<string> {
  const out = new Set<string>();
  for (const x of a) if (b.has(x)) out.add(x);
  return out;
}
