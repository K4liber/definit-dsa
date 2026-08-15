import * as d3 from 'd3';
import type { DefGraph, DefNode, LearnState, Pos, Raw, TreeNode } from '../types';
import { COLOR_NOT_READY, COLOR_PRE_READY, COLOR_READY, COLOR_LEARNED } from './constants';

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

export function fieldOfId(id: string): string {
  return id.split('/')[0] ?? '';
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
  return 'not-ready';
}

export function colorForLearnState(s: LearnState): string {
  if (s === 'learned') return COLOR_LEARNED;
  if (s === 'ready') return COLOR_READY;
  if (s === 'pre-ready') return COLOR_PRE_READY;
  return COLOR_NOT_READY;
}

export function learnStateRank(s: LearnState): number {
  if (s === 'ready') return 0;
  if (s === 'learned') return 1;
  if (s === 'pre-ready') return 2;
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
    if (learnStateForNode(dep, learned) === 'not-ready') visible.add(dep.id);
  }
  return visible;
}

export function effectiveState(n: DefNode, learned: Set<string>, visibleSet: Set<string>): LearnState {
  const base = learnStateForNode(n, learned);
  return base === 'not-ready' && visibleSet.has(n.id) ? 'pre-ready' : base;
}

/* ------------------------------------------------------------------ */
/*  Level computation                                                 */
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
/*  Build Raw from DefGraph                                            */
/* ------------------------------------------------------------------ */

export function buildRaw(def: DefGraph): Raw {
  const byId = new Map(def.nodes.map((n) => [n.id, n] as const));

  const fieldsSet = new Set<string>();
  for (const n of def.nodes) {
    const field = fieldOfId(n.id);
    if (field) fieldsSet.add(field);
  }
  const fields = Array.from(fieldsSet).sort();

  return { def, byId, fields };
}

/* ------------------------------------------------------------------ */
/*  renderGraph – project the full graph with visibility filtering    */
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
/*  Recompute included set from ready nodes                           */
/* ------------------------------------------------------------------ */

export function recomputeIncludedSetFromReady(
  raw: Raw,
  learned: Set<string>,
): Set<string> | null {
  const readyFields = new Set<string>();

  for (const n of raw.def.nodes) {
    if (learnStateForNode(n, learned) === 'ready') readyFields.add(fieldOfId(n.id));
  }

  if (!readyFields.size) return null;
  // If every field already has a ready definition, there is nothing to focus on.
  if (raw.fields.every((field) => readyFields.has(field))) return null;

  const included = new Set<string>();

  for (const n of raw.def.nodes) {
    if (learnStateForNode(n, learned) === 'learned') included.add(n.id);
    else if (readyFields.has(fieldOfId(n.id))) included.add(n.id);
  }

  return included;
}

/* ------------------------------------------------------------------ */
/*  Select next ready definition                                      */
/* ------------------------------------------------------------------ */

export function selectNextReady(
  raw: Raw,
  rendered: DefGraph,
  learned: Set<string>,
): string | null {
  void raw; // kept for API stability
  computeLevels(rendered.nodes);
  const ready = rendered.nodes.filter((n) => learnStateForNode(n, learned) === 'ready');
  if (!ready.length) return null;

  ready.sort((a, b) => {
    const la = a.level ?? 0;
    const lb = b.level ?? 0;
    if (la !== lb) return la - lb;
    return a.id.localeCompare(b.id);
  });

  return ready[0].id;
}

/* ------------------------------------------------------------------ */
/*  Build Definition Tree (grouped by field)                           */
/* ------------------------------------------------------------------ */

export function buildDefinitionTree(
  raw: Raw,
  rendered: DefGraph,
  learned: Set<string>,
): { root: TreeNode; visibleNodeIds: Set<string> } {
  const visibleNodeIds = computeVisibleSet(rendered, learned);
  const renderedById = new Map(rendered.nodes.map((n) => [n.id, n] as const));

  const root: TreeNode = { id: '', name: '', kind: 'group', depth: 0, children: [] };

  const groupByField = new Map<string, TreeNode>();
  for (const field of raw.fields) {
    const group: TreeNode = { id: field, name: field, kind: 'group', depth: 1, children: [] };
    groupByField.set(field, group);
    root.children.push(group);
  }

  for (const leaf of raw.def.nodes) {
    const field = fieldOfId(leaf.id);
    const parent = groupByField.get(field);
    if (!parent) continue;

    const rawLeaf = raw.byId.get(leaf.id) ?? leaf;
    const leafNode: TreeNode = {
      id: leaf.id,
      name: leaf.id.split('/').at(-1) ?? leaf.id,
      kind: 'leaf',
      depth: 2,
      children: [],
      // Prefer the dynamically computed level from the rendered graph.
      leaf: { ...rawLeaf, level: renderedById.get(leaf.id)?.level ?? rawLeaf.level ?? 0 },
    };
    parent.children.push(leafNode);
  }

  const stateForCat = (leaf: DefNode): LearnState => {
    const base = learnStateForNode(leaf, learned);
    return base === 'not-ready' && visibleNodeIds.has(leaf.id) ? 'pre-ready' : base;
  };

  const sortChildren = (n: TreeNode) => {
    for (const c of n.children) sortChildren(c);

    n.children.sort((a, b) => {
      if (a.kind !== b.kind) return a.kind === 'group' ? -1 : 1;

      if (a.kind === 'group' && b.kind === 'group') {
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
  rendered: DefGraph,
  learned: Set<string>,
): {
  totalDefs: number;
  learnedDefs: number;
  totalEdges: number;
  unlockedEdges: number;
  totalLevels: number;
  completedLevels: number;
} {
  const totalDefs = rendered.nodes.length;
  const learnedDefs = rendered.nodes.reduce((acc, n) => acc + (learned.has(n.id) ? 1 : 0), 0);

  const totalEdges = rendered.edges.length;
  const unlockedEdges = rendered.edges.reduce((acc, e) => acc + (learned.has(e.target) ? 1 : 0), 0);

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
  const normalizedDeps = new Map<string, string[]>();

  const addNormalizedCandidate = (key: string, id: string) => {
    const arr = normalizedDeps.get(key) ?? [];
    if (!arr.includes(id)) arr.push(id);
    normalizedDeps.set(key, arr);
  };

  for (const id of deps) {
    const node = byId.get(id);
    const t = node?.title ?? id.split('/').at(-1) ?? id;
    depMap.set(id, { id, title: t });

    const field = id.split('/')[0];
    const idSuffix = id.split('/').at(-1);
    if (field && idSuffix) addNormalizedCandidate(`${field}/${normalizeId(idSuffix)}`, id);
  }

  const linkRe = /\[([^\]]+)\]\(([^)]+)\)/g;

  const replaced = clean.replace(linkRe, (_m, labelRaw, hrefRaw) => {
    const label = String(labelRaw ?? '').trim();
    const href = String(hrefRaw ?? '').trim();

    let depId: string | undefined;
    if (depMap.has(href)) depId = href;

    if (!depId) {
      const normalizedHref = href.includes('/')
        ? `${href.split('/')[0]}/${normalizeId(href.split('/').at(-1) ?? '')}`
        : normalizeId(href);
      const normalizedMatches = normalizedDeps.get(normalizedHref) ?? [];
      if (normalizedMatches.length === 1) depId = normalizedMatches[0];
    }

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
    return `<span class="dep" data-dep="${escapeHtml(dep.id)}">${escapeHtml(label || dep.title)}</span>`;
  });

  const paragraphs = replaced
    .split(/\n\s*\n+/g)
    .map((p) => p.replace(/\s*\n\s*/g, ' ').trim())
    .filter(Boolean);

  return paragraphs.map((p) => `<p>${p}</p>`).join('');
}

/* ------------------------------------------------------------------ */
/*  Search filtering helpers                                           */
/* ------------------------------------------------------------------ */;

function walkGraph(raw: Raw, startId: string): Set<string> {
  const out = new Set<string>();
  const stack: string[] = [startId];

  // Build adjacency
  const nextById = new Map<string, string[]>();
  for (const n of raw.def.nodes) nextById.set(n.id, []);

  for (const n of raw.def.nodes) {
    nextById.set(n.id, (n.deps ?? []).filter((d) => raw.byId.has(d)));
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
  return walkGraph(raw, id);
}

/** Intersection helper that handles nulls. */
export function intersectSets(a: Set<string>, b: Set<string>): Set<string> {
  const out = new Set<string>();
  for (const x of a) if (b.has(x)) out.add(x);
  return out;
}
