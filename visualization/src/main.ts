import * as d3 from 'd3';
import type { BottomTab, DefGraph, DefNode, LearnState, Pos, Raw, TreeNode, UIState } from './types';

// Keep raw graph around so checkbox toggles can materialize default included set.
// It is assigned in rerender() after defs.json is loaded.
let raw: Raw | null = null;

const svg = d3.select<SVGSVGElement, unknown>('#viz');

const W = () => svg.node()!.clientWidth;
const H = () => svg.node()!.clientHeight;

const gRoot = svg.append('g');
const gRings = gRoot.append('g').attr('class', 'rings');
const gLinks = gRoot.append('g').attr('class', 'links');
const gNodes = gRoot.append('g').attr('class', 'nodes');

const zoom = d3
  .zoom<SVGSVGElement, unknown>()
  .scaleExtent([0.1, 6])
  .on('zoom', (ev: d3.D3ZoomEvent<SVGSVGElement, unknown>) => {
    gRoot.attr('transform', ev.transform.toString());
  });

svg.call(zoom as any);

function normalizeId(s: string) {
  return s
    .trim()
    .toLowerCase()
    .replace(/\s+/g, '_')
    .replace(/[^a-z0-9_\-\/]/g, '');
}

function setStats(graph: DefGraph) {
  const maxLevel = Math.max(0, ...graph.nodes.map((n) => n.level ?? 0));

  const statsEl = document.getElementById('stats')!;
  statsEl.innerHTML = '';
  const kv: Array<[string, string]> = [
    ['Nodes', String(graph.nodes.length)],
    ['Edges', String(graph.edges.length)],
    ['Levels', String(maxLevel + 1)],
  ];
  for (const [k, v] of kv) {
    const dk = document.createElement('div');
    dk.textContent = k;
    const dv = document.createElement('div');
    dv.textContent = v;
    statsEl.appendChild(dk);
    statsEl.appendChild(dv);
  }
}

// keep track of which level ring is currently highlighted
let hoveredLevel: number | null = null;

// keep track of which node is selected for ring focus
let selectedNodeId: string | null = null;

function applyRingHighlight() {
  // Hover ring takes precedence; otherwise fall back to selected node ring.
  let level: number | null = hoveredLevel;

  if (level === null && selectedNodeId && lastRendered) {
    const n = lastRendered.nodes.find((x) => x.id === selectedNodeId);
    level = n?.level ?? null;
  }

  gRings
    .selectAll<SVGCircleElement, { level: number; r: number }>('circle.ring')
    .classed('hovered', (d) => level !== null && d.level === level);
}

function setRingHighlight(level: number | null) {
  hoveredLevel = level;
  applyRingHighlight();
}

function textWidthPx(text: string) {
  // rough estimate (panel uses ~12-13px font sizes)
  return Math.max(24, text.length * 7.2);
}

function hash01(s: string) {
  // deterministic 0..1
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return (h >>> 0) / 0xffffffff;
}

// Learning-state coloring
const COLOR_OFF = 'rgba(148, 163, 184, 0.18)'; // barely visible
const COLOR_VISIBLE = 'rgba(148, 163, 184, 0.8)'; // normal grey
const COLOR_READY = '#fbbf24'; // yellow
const COLOR_LEARNED = '#22c55e'; // green

// Learning progress is persisted independently from visibility filtering.
const LEARNED_STORAGE_KEY = 'definit-db.learned';

// --- Categories visibility (checkbox) model ---
// A checked box means the item is INCLUDED in the rendered graph.
const VISIBILITY_STORAGE_KEY = 'definit-db.ui.includedIds';

function loadIncludedFromStorage() {
  try {
    const raw = localStorage.getItem(VISIBILITY_STORAGE_KEY);
    if (!raw) return null as Set<string> | null;
    const arr = JSON.parse(raw);
    if (!Array.isArray(arr)) return null;
    return new Set<string>(arr.filter((x) => typeof x === 'string'));
  } catch {
    return null;
  }
}

function saveIncludedToStorage(set: Set<string>) {
  try {
    localStorage.setItem(VISIBILITY_STORAGE_KEY, JSON.stringify(Array.from(set)));
  } catch {
    // ignore
  }
}

function loadLearnedFromStorage() {
  try {
    const raw = localStorage.getItem(LEARNED_STORAGE_KEY);
    if (!raw) return new Set<string>();
    const arr = JSON.parse(raw);
    if (!Array.isArray(arr)) return new Set<string>();
    return new Set<string>(arr.filter((x) => typeof x === 'string'));
  } catch {
    return new Set<string>();
  }
}

function saveLearnedToStorage() {
  try {
    localStorage.setItem(LEARNED_STORAGE_KEY, JSON.stringify(Array.from(learned)));
  } catch {
    // ignore
  }
}

function clearLearnedProgress() {
  learned.clear();
  try {
    localStorage.removeItem(LEARNED_STORAGE_KEY);
  } catch {
    // ignore
  }
}

const learned = loadLearnedFromStorage();

const INFO_TEXT =
  'Welcome to the "Data Structures and Algorithms" course!\n\n' +
  'This is a great starting point if you are preparing for coding interviews. The tool helps you learn or review key definitions related to data structures and algorithms.\n\n' +
  'The definitions are based on Cracking the Coding Interview by Gayle Laakmann McDowell. A total of 275 terms from mathematics and computer science are organized topologically to create a smooth and logical learning experience.\n\n' +
  'Give it a try, take it easy, and have fun! Feedback is always appreciated. Feel free to contact me at janbielecki94@gmail.com.';

function hasAnyLearned() {
  return learned.size > 0;
}

function updateResetProgressButton() {
  const btn = (document.getElementById('resetProgress') ?? document.getElementById('reset')) as HTMLButtonElement | null;
  if (!btn) return;
  btn.disabled = !hasAnyLearned();
  btn.title = btn.disabled ? 'Nothing to reset yet' : 'Reset progress';
}

function bindInfoPopup() {
  const overlay = document.getElementById('infoOverlay') as HTMLDivElement | null;
  const fab = document.getElementById('infoFab') as HTMLButtonElement | null;
  const closeBtn = document.getElementById('infoClose') as HTMLButtonElement | null;
  const body = document.getElementById('infoBody') as HTMLDivElement | null;

  if (!overlay || !fab || !closeBtn || !body) return;

  body.textContent = INFO_TEXT;

  const open = () => {
    overlay.classList.add('open');
  };

  const close = () => {
    overlay.classList.remove('open');
  };

  fab.onclick = (ev) => {
    ev.preventDefault();
    ev.stopPropagation();
    open();
  };

  closeBtn.onclick = (ev) => {
    ev.preventDefault();
    ev.stopPropagation();
    close();
  };

  // Click outside modal closes it
  overlay.addEventListener('click', (ev) => {
    if (ev.target === overlay) close();
  });

  // ESC closes it
  window.addEventListener('keydown', (ev) => {
    if (ev.key === 'Escape' && overlay.classList.contains('open')) close();
  });

  // Auto-show on initial load if nothing learned yet.
  // If user has not learned anything yet, we always show this on page load.
  if (!hasAnyLearned()) {
    setTimeout(() => open(), 60);
  }

}

bindInfoPopup();
updateResetProgressButton();

// Manual selection is persisted, but can be overwritten by a recompute.
let includedIds: Set<string> | null = loadIncludedFromStorage();

function recomputeIncludedSetFromReady(rawGraph: Raw) {
  // Identify the *specific* categories (immediate parent folder) that contain >=1 READY node.
  // We intentionally do NOT bubble readiness up to ancestor categories/fields.
  const readyParentPrefixes = new Set<string>();

  for (const n of rawGraph.def.nodes) {
    if (learnStateForNode(n) !== 'ready') continue;

    const parts = splitCategory(n.category);
    const parentDepth = Math.max(1, parts.length - 1);
    const parent = groupIdForPath(parts, parentDepth);
    if (parent) readyParentPrefixes.add(parent);
  }

  // If nothing is ready, empty the state.
  if (!readyParentPrefixes.size) {
    console.log("No ready categories found.");
    includedIds = null;
    try {
      localStorage.removeItem(VISIBILITY_STORAGE_KEY);
    } catch {
      console.warn("Failed to clear included IDs from storage.");
    }
    return;
  }

  includedIds = new Set<string>();

  // Include all with a learned state
  for (const n of rawGraph.def.nodes) {
    if (learnStateForNode(n) === 'learned') includedIds.add(n.id);
  }

  // Include all when parent category is ready
  for (const leaf of rawGraph.def.nodes) {
    const parts = splitCategory(leaf.category);
    const parentDepth = Math.max(1, parts.length - 1);
    const parent = groupIdForPath(parts, parentDepth);

    if (parent && readyParentPrefixes.has(parent)) includedIds.add(leaf.id);
  }

  console.log(`  Found ${includedIds.size} included definitions.`);
  saveIncludedToStorage(includedIds);
}

function isIncluded(id: string) {
  // Default: if state is empty, include everything.
  if (!includedIds) return true;
  return includedIds.has(id);
}

function setIncluded(id: string, include: boolean) {
  setIncludedMany([id], include);
}

function setIncludedMany(ids: string[], include: boolean) {
  if (!includedIds) {
    includedIds = new Set<string>((raw?.def.nodes ?? []).map((n: DefNode) => n.id));
  }
  if (!includedIds) includedIds = new Set<string>();

  for (const id of ids) {
    if (include) includedIds.add(id);
    else includedIds.delete(id);
  }

  saveIncludedToStorage(includedIds);
}

function learnStateForNode(n: DefNode): LearnState {
  // Base state from learning/progression only..
  if (learned.has(n.id)) return 'learned';

  // Ready if all deps are learned (including "no deps").
  // IMPORTANT: this is intentionally independent from UI visibility (checkbox filtering).
  const deps = n.deps ?? [];
  const allLearned = deps.every((d) => learned.has(d));
  if (allLearned) return 'ready';

  return 'off';
}

function colorForLearnState(s: LearnState) {
  if (s === 'learned') return COLOR_LEARNED;
  if (s === 'ready') return COLOR_READY;
  if (s === 'visible') return COLOR_VISIBLE;
  return COLOR_OFF;
}

// Cache the most recent layout used for rendering so zoom-to-ring uses the same geometry.
let lastLayout: ReturnType<typeof radialLayout> | null = null;

function radialLayout(graph: DefGraph) {
  const width = W();
  const height = H();
  const cx = width / 2;
  const cy = height / 2;

  const maxLevel = Math.max(0, ...graph.nodes.map((n) => n.level ?? 0));

  // Make rings less dense for large labels.
  const maxLabel = Math.max(6, ...graph.nodes.map((n) => n.title?.length ?? 0));
  const ringGap = Math.max(54, Math.min(120, 30 + maxLabel * 2.4));
  const base = 56;

  const byLevel = d3.group(graph.nodes, (n: DefNode) => n.level ?? 0);

  const placed = new Map<string, Pos>();

  // Per-level angular offset so nodes on different rings don't align.
  const levelOffset = (level: number) => (hash01(String(level)) * 0.9 + level * 0.37) % (Math.PI * 2);

  // Simple per-ring relaxation in angle space to reduce overlaps.
  // We treat each node as needing an arc length proportional to its label width.
  const relaxAngles = (nodes: DefNode[], r: number, baseAngles: number[]) => {
    if (nodes.length <= 1) return baseAngles;

    const angles = baseAngles.slice();
    const widths = nodes.map((n) => textWidthPx(n.title));

    // Convert desired pixel spacing into angular spacing.
    const need = widths.map((w) => (w + 18) / Math.max(1, r));

    // iteration: push neighbors apart
    const iters = 22;
    for (let it = 0; it < iters; it++) {
      // sort by angle
      const idx = d3.range(nodes.length).sort((a, b) => angles[a] - angles[b]);
      for (let j = 0; j < idx.length; j++) {
        const a = idx[j];
        const b = idx[(j + 1) % idx.length];

        // circular distance
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

    // normalize back into 0..2pi
    for (let i = 0; i < angles.length; i++) {
      angles[i] = ((angles[i] % (Math.PI * 2)) + Math.PI * 2) % (Math.PI * 2);
    }

    return angles;
  };

  for (let level = 0; level <= maxLevel; level++) {
    const nodes = ((byLevel.get(level) ?? []) as DefNode[])
      .slice()
      .sort((a: DefNode, b: DefNode) => a.id.localeCompare(b.id));

    const count = nodes.length;
    if (!count) continue;

    const r = base + level * ringGap;

    // Spread by angle; avoid a shared horizontal line when count is small.
    const baseOffset = levelOffset(level);

    let baseAngles: number[];
    if (count === 2) {
      // put them on a diagonal rather than left/right
      baseAngles = [baseOffset + Math.PI / 4, baseOffset + (Math.PI + Math.PI / 4)];
    } else if (count === 3) {
      baseAngles = [0, 1, 2].map((i) => baseOffset + (i / 3) * Math.PI * 2 + Math.PI / 6);
    } else {
      baseAngles = nodes.map((_n, i) => baseOffset + (i / count) * Math.PI * 2);
    }

    const angles = relaxAngles(nodes, r, baseAngles);

    for (let i = 0; i < count; i++) {
      const n = nodes[i];
      const a = angles[i];
      placed.set(n.id, { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) });
    }
  }

  return {
    cx,
    cy,
    ringGap,
    base,
    maxLevel,
    pos: placed,
  };
}

function computeLevels(nodes: DefNode[]) {
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

// Compute group DAG (prefix -> prefix) from leaf deps and return per-group level.
function computeGroupLevels(raw: Raw) {
  const groups = new Set<string>(raw.childrenByPrefix.keys());
  console.log(`Computing group levels for ${groups.size} groups.`);

  const depsByGroup = new Map<string, Set<string>>();
  for (const g of groups) depsByGroup.set(g, new Set());

  const groupOfLeafAtDepth = (leafCategory: string, depth: number) => {
    const parts = splitCategory(leafCategory);
    if (parts.length < depth) return null;
    // group prefixes exist only for depths < leaf length
    if (depth > parts.length - 1) return null;
    return groupIdForPath(parts, depth);
  };

  // Group dependency rule: if any leaf within A depends on any leaf within B,
  // then A depends on B (at that same depth), unless it stays within the same group.
  for (const n of raw.def.nodes) {
    const srcParts = splitCategory(n.category);

    for (const depId of n.deps ?? []) {
      const depCategory = raw.byId.get(depId)?.category;

      if (!depCategory) throw new Error(`Dependency id not found: ${depId}`);

      const depParts = splitCategory(depCategory);
      const maxDepth = Math.min(srcParts.length - 1, depParts.length - 1);

      for (let d = 1; d <= maxDepth; d++) {
        const a = groupOfLeafAtDepth(n.category, d);
        const b = groupOfLeafAtDepth(depCategory, d);
        if (!a || !b) continue;
        if (a === b) continue;
        depsByGroup.get(a)?.add(b);
      }
    }
  }

  // Level is max(dep.level + 1) (same as leaf levels). DAG assumed.
  const levelByGroup = new Map<string, number>();
  const visiting = new Set<string>();
  const visited = new Set<string>();

  const dfs = (g: string): number => {
    const cached = levelByGroup.get(g);
    if (cached !== undefined) return cached;
    if (visited.has(g)) return levelByGroup.get(g) ?? 0;
    if (visiting.has(g)) return 0; // should not happen if DAG; guard anyway

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

// For sorting groups: compare by topological level first, then name.
function compareGroupsTopologicalLevel(a: TreeNode, b: TreeNode) {
  const la = a.groupLevel ?? 0;
  const lb = b.groupLevel ?? 0;
  if (la !== lb) return la - lb;
  return a.name.localeCompare(b.name);
}

function draw(graph: DefGraph) {
  // Ensure dynamic levels exist for rendering.
  computeLevels(graph.nodes);

  setStats(graph);

  const layout = radialLayout(graph);
  lastLayout = layout;

  // nodes that should be "visible" (not learned/ready, but have >=1 incoming on-edge)
  const visibleNodeIds = new Set<string>();
  {
    const byId = new Map(graph.nodes.map((n) => [n.id, n] as const));
    for (const e of graph.edges as Array<{ source: string; target: string }>) {
      // Edge is "on" when the prerequisite (target) is learned.
      const prereq = byId.get(e.target);
      if (!prereq) continue;
      if (learnStateForNode(prereq) !== 'learned') continue;

      // Mark the dependent node as "visible" if it isn't ready/learned.
      const dep = byId.get(e.source);
      if (!dep) continue;
      const base = learnStateForNode(dep);
      if (base === 'off') visibleNodeIds.add(dep.id);
    }
  }

  // rings
  const ringData = d3.range(0, layout.maxLevel + 1).map((level: number) => ({
    level,
    r: layout.base + level * layout.ringGap,
  }));

  gRings
    .selectAll<SVGCircleElement, { level: number; r: number }>('circle.ring')
    .data(ringData, (d) => String(d.level))
    .join((enter) => enter.append('circle').attr('class', 'ring'))
    .attr('cx', layout.cx)
    .attr('cy', layout.cy)
    .attr('r', (d) => d.r);

  // keep hovered ring if any, otherwise keep selected ring
  applyRingHighlight();

  type Edge = { source: string; target: string };

  // Curved edge path generator (quadratic curve via mid-point pulled toward center)
  const edgePath = (d: Edge) => {
    const s = layout.pos.get(d.source);
    const t = layout.pos.get(d.target);
    if (!s || !t) return '';

    const mx = (s.x + t.x) / 2;
    const my = (s.y + t.y) / 2;

    // Pull the control point toward the center so edges arc inward.
    const k = 0.55;
    const cx = mx + (layout.cx - mx) * k;
    const cy = my + (layout.cy - my) * k;

    return `M${s.x},${s.y} Q${cx},${cy} ${t.x},${t.y}`;
  };

  const byId = new Map(graph.nodes.map((n) => [n.id, n] as const));

  const linkSel = gLinks
    .selectAll<SVGPathElement, Edge>('path.link')
    .data(graph.edges as Edge[], (d) => `${d.source}->${d.target}`)
    .join((enter) =>
      enter
        .append('path')
        .attr('class', 'link')
        .attr('fill', 'none')
        .attr('stroke-linecap', 'round')
        .attr('stroke-linejoin', 'round'),
    );

  linkSel
    .attr('d', edgePath)
    // edge styling based on prerequisite learn-state (target)
    .classed('link-on', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      return s === 'learned';
    })
    .classed('link-off', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      return s !== 'learned';
    })
    .attr('stroke', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      // prerequisite not learned => subtle but visible; learned => emphasized
      return s === 'learned' ? 'rgba(226, 232, 240, 0.85)' : 'rgba(148, 163, 184, 0.16)';
    })
    .attr('stroke-width', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      return s === 'learned' ? 2.2 : 1.0;
    })
    .attr('stroke-dasharray', (d) => {
      const prereq = byId.get(d.target);
      const s = prereq ? learnStateForNode(prereq) : 'off';
      return s === 'learned' ? null : '3 5';
    })
    .attr('opacity', 1);

  const nodeSel = gNodes
    .selectAll<SVGGElement, DefNode>('g.node')
    .data(graph.nodes, (d) => d.id)
    .join((enter) => {
      const g = enter.append('g').attr('class', 'node');

      // Bigger base size
      const circleR = 8;
      const leafR = 11;

      // circle for nodes
      g.append('circle').attr('class', 'node-circle').attr('r', circleR);

      // underline/accent ring for nodes
      g.append('circle').attr('class', 'leaf-underline').attr('r', leafR + 4);

      g.append('text').attr('dx', 12).attr('dy', 5);

      // Native SVG tooltip
      g.append('title');

      return g;
    });

  // Update tooltip content for all nodes (enter+update)
  nodeSel
    .select('title')
    .text((d: DefNode) => {
      return `${d.title} (level: ${d.level ?? 0})\n${d.category}`;
    });

  // hover effect
  nodeSel
    .on('mouseenter', (ev: MouseEvent, d: DefNode) => {
      d3.select(ev.currentTarget as SVGGElement).classed('hovering', true);
      setRingHighlight(d.level ?? 0);
    })
    .on('mouseleave', (ev: MouseEvent) => {
      d3.select(ev.currentTarget as SVGGElement).classed('hovering', false);
      setRingHighlight(null);

      // Restore pulsing to the selected node (if any) when not hovering.
      if (selectedNodeId) {
        const sel = gNodes.selectAll<SVGGElement, DefNode>('g.node').filter((n) => n.id === selectedNodeId);
        sel.classed('hovering', true);
      }
    });

  // Ensure the selected node pulses when not hovering another node.
  if (selectedNodeId) {
    gNodes
      .selectAll<SVGGElement, DefNode>('g.node')
      .classed('hovering', (n) => hoveredLevel === null && n.id === selectedNodeId);
  }

  nodeSel.attr('transform', (d) => {
    const p = layout.pos.get(d.id)!;
    return `translate(${p.x},${p.y})`;
  });

  const fillFor = (d: DefNode) => {
    const base = learnStateForNode(d);
    const s: LearnState = base === 'off' && visibleNodeIds.has(d.id) ? 'visible' : base;
    return colorForLearnState(s);
  };

  const stateFor = (d: DefNode): LearnState => {
    const base = learnStateForNode(d);
    return base === 'off' && visibleNodeIds.has(d.id) ? 'visible' : base;
  };

  nodeSel
    .select<SVGCircleElement>('circle.node-circle')
    .attr('display', (d) => {
      return null;
    })
    .attr('fill', (d) => fillFor(d))
    .attr('opacity', 1);

  // underline ring only for nodes
  nodeSel
    .select<SVGCircleElement>('circle.leaf-underline')
    .attr('fill', 'none')
    .attr('stroke', (d) => (fillFor(d)))
    .attr('stroke-width', (d) => (2))
    .attr('opacity', (d) => (0.9));

  // label text
  nodeSel
    .select('text')
    .text((d: DefNode) => d.title)
    .attr('fill', '#e6edf3')
    .attr('opacity', (d: DefNode) => (stateFor(d) === 'off' ? 0.22 : 1))
    .attr('text-decoration', 'none')
    .attr('text-decoration-thickness', null)
    .attr('text-underline-offset', null);

  bindInteractions(nodeSel);

  const search = document.getElementById('search') as HTMLInputElement;
  search.oninput = () => {
    const q = normalizeId(search.value);
    const isMatch = (d: DefNode) => q && normalizeId(d.id).includes(q);

    nodeSel
      .selectAll<SVGCircleElement | SVGPathElement, DefNode>('circle.node-circle')
      .attr('stroke', (d) => (isMatch(d) ? '#ef4444' : 'none'))
      .attr('stroke-width', (d) => (isMatch(d) ? 2.5 : 1));
  };
}

// -------------------------------
// Interactive projection model
// -------------------------------

const viewerEl = document.getElementById('viewer') as HTMLDivElement;
const viewerTitleEl = document.getElementById('viewerTitle') as HTMLHeadingElement;
const viewerPathEl = document.getElementById('viewerPath') as HTMLDivElement;
const viewerBodyEl = document.getElementById('viewerBody') as HTMLDivElement;
const markLearnedBtn = document.getElementById('markLearned') as HTMLButtonElement | null;

function updateMarkLearnedButton(node?: DefNode) {
  if (!markLearnedBtn) return;
  if (!node) {
    markLearnedBtn.style.display = 'none';
    markLearnedBtn.disabled = true;
    markLearnedBtn.onclick = null;
    return;
  }

  const s = learnStateForNode(node);
  markLearnedBtn.style.display = '';
  markLearnedBtn.disabled = s !== 'ready';

  markLearnedBtn.onclick = () => {
    // Only works for ready nodes.
    if (learnStateForNode(node) !== 'ready') return;

    learned.add(node.id);
    saveLearnedToStorage();
    updateResetProgressButton();

    // After learning, recompute the suggested visibility set (may unlock/shift readiness).
    if (raw) recomputeIncludedSetFromReady(raw);

    // Re-render to update node+edge styles and any newly-ready nodes.
    rerender(true);

    // Behave like clicking "Definitions": clear selection/viewer and refocus to highest active ring
    // so newly-unlocked nodes are brought into view.
    state.selectedLeaf = undefined;
    selectedNodeId = null;
    hideViewer();

    requestAnimationFrame(() => {
      focusHighestActiveRing();
    });
  };
}

function escapeHtml(s: string) {
  return s
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function normalizeMdForViewer(md: string) {
  // 1) drop the first markdown title line (e.g. "# name")
  // 2) normalize CRLF -> LF
  // 3) collapse excessive blank lines
  const lines = md.replace(/\r\n?/g, '\n').split('\n');
  const out: string[] = [];

  let i = 0;
  // drop initial empty lines
  while (i < lines.length && !lines[i].trim()) i++;
  // drop first H1/H2 line
  if (i < lines.length && /^#{1,2}\s+/.test(lines[i].trim())) i++;

  for (; i < lines.length; i++) out.push(lines[i]);

  // trim leading/trailing blank lines
  while (out.length && !out[0].trim()) out.shift();
  while (out.length && !out[out.length - 1].trim()) out.pop();

  // collapse 3+ blank lines to 2
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

function selectLeafById(id: string) {
  if (!lastRendered) return;
  const node = lastRendered.nodes.find((n) => n.id === id);
  if (!node) return;

  // Track selection for ring focus + pulsing.
  state.selectedLeaf = id;
  selectedNodeId = id;

  // Re-render (keeps transform) so node/link styles update.
  rerender(true);

  // Focus and pulse on the selected node.
  requestAnimationFrame(() => {
    focusRingOfNode(id);
  });

  // Open viewer content.
  void openLeaf(node);
}

// Keep old helper for internal callers (compat)
function behaviorLikeGraphClick(id: string) {
  selectLeafById(id);
}

function buildDepLinkMap(deps: string[]) {
  const map = new Map<string, { id: string; title: string }>();

  // Prefer the currently rendered graph for titles (matches what's on screen)
  const byId = new Map((lastRendered?.nodes ?? []).map((n) => [n.id, n] as const));

  for (const id of deps) {
    const t = byId.get(id)?.title ?? id.split('/').at(-1) ?? id;
    map.set(id, { id, title: t });
  }

  return map;
}

function renderViewerBody(md: string, deps: string[]) {
  const clean = normalizeMdForViewer(md);
  const depMap = buildDepLinkMap(deps);

  // (A) convert markdown links [label](href) into dependency spans (when href points to a known dep)
  const linkRe = /\[([^\]]+)\]\(([^)]+)\)/g;

  const replaced = clean.replace(linkRe, (_m, labelRaw, hrefRaw) => {
    const label = String(labelRaw ?? '').trim();
    const href = String(hrefRaw ?? '').trim();

    // Try to resolve by exact dep id first.
    let depId: string | undefined;
    if (depMap.has(href)) depId = href;

    // Try to resolve by suffix match: "field/name" against deps containing that suffix.
    if (!depId && href.includes('/')) {
      const suffix = '/' + href.split('/').filter(Boolean).pop();
      const field = href.split('/')[0];
      const candidates = Array.from(depMap.keys()).filter((id) => id.startsWith(field + '/') && id.endsWith(suffix));
      if (candidates.length === 1) depId = candidates[0];
    }

    if (!depId) {
      // Not a known dependency; keep label text only (drop the "(href)" part).
      return escapeHtml(label || href);
    }

    const dep = depMap.get(depId)!;
    // Display only the definition name (title), not "[name](category)".
    return `<span class="dep" data-dep="${escapeHtml(dep.id)}">${escapeHtml(dep.title)}</span>`;
  });

  // (B) Create paragraphs by splitting on blank lines. Within a paragraph, join lines with spaces
  // so there are no visible newline characters.
  const paragraphs = replaced
    .split(/\n\s*\n+/g)
    .map((p) => p.replace(/\s*\n\s*/g, ' ').trim())
    .filter(Boolean);

  viewerBodyEl.innerHTML = paragraphs.map((p) => `<p>${p}</p>`).join('');

  // Bind click handlers for dependency links
  viewerBodyEl.querySelectorAll<HTMLElement>('span.dep[data-dep]').forEach((el) => {
    el.onclick = (ev) => {
      ev.preventDefault();
      ev.stopPropagation();
      const id = el.dataset.dep;
      if (!id) return;
      behaviorLikeGraphClick(id);
    };
  });
}

function showViewer(node: DefNode, md: string) {
  viewerEl.style.display = '';
  viewerTitleEl.textContent = node.title;
  viewerPathEl.style.display = '';
  viewerPathEl.textContent = node.category;
  renderViewerBody(md, node.deps ?? []);
  updateMarkLearnedButton(node);
}

function hideViewer() {
  // Keep the viewer panel visible, but show a placeholder.
  viewerEl.style.display = '';
  viewerTitleEl.textContent = 'Content';
  viewerPathEl.style.display = 'none';
  viewerPathEl.textContent = '';
  viewerBodyEl.innerHTML = '<p style="margin:0; color:#a9b4c0;">Select a definition to show the content.</p>';
  updateMarkLearnedButton(undefined);
}

function splitCategory(category: string) {
  return category.split('/').filter(Boolean);
}

function groupIdForPath(parts: string[], depth: number) {
  return parts.slice(0, depth).join('/');
}

function buildRaw(def: DefGraph): Raw {
  console.log("Building raw data structure...");
  const byId = new Map(def.nodes.map((n) => [n.id, n] as const));

  const fieldsSet = new Set<string>();
  for (const n of def.nodes) {
    const [field] = splitCategory(n.category);
    if (field) fieldsSet.add(field);
  }
  const fields = Array.from(fieldsSet).sort();
  console.log(`  Found ${fields.length} fields: ${fields.join(', ')}`);

  // childrenByPrefix: prefix -> leaf ids directly under that prefix (any depth)
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

  // de-dupe and sort
  for (const [k, arr] of childrenByPrefix) {
    childrenByPrefix.set(k, Array.from(new Set(arr)).sort());
  }

  return { def, byId, childrenByPrefix, fields };
}

const CATEGORIES_OPEN_KEY = 'definit-db.ui.categories.openPrefixes';
function loadOpenPrefixes() {
  try {
    const raw = localStorage.getItem(CATEGORIES_OPEN_KEY);
    if (!raw) return new Set<string>();
    const arr = JSON.parse(raw);
    if (!Array.isArray(arr)) return new Set<string>();
    return new Set<string>(arr.filter((x) => typeof x === 'string'));
  } catch {
    return new Set<string>();
  }
}
function saveOpenPrefixes(s: Set<string>) {
  try {
    localStorage.setItem(CATEGORIES_OPEN_KEY, JSON.stringify(Array.from(s)));
  } catch {
    // ignore
  }
}

let openPrefixes = loadOpenPrefixes();

function learnStateRank(s: LearnState) {
  // Desired order: ready, learned, visible, off
  if (s === 'ready') return 0;
  if (s === 'learned') return 1;
  if (s === 'visible') return 2;
  return 3;
}

function computeVisibleSetFromRendered(rendered: DefGraph) {
  // Same logic as inside draw(), but we need it for Categories sorting.
  const visible = new Set<string>();
  const byId = new Map(rendered.nodes.map((n) => [n.id, n] as const));

  for (const e of rendered.edges as Array<{ source: string; target: string }>) {
    const prereq = byId.get(e.target);
    if (!prereq) continue;
    if (learnStateForNode(prereq) !== 'learned') continue;

    const dep = byId.get(e.source);
    if (!dep) continue;
    if (learnStateForNode(dep) === 'off') visible.add(dep.id);
  }

  return visible;
}

function stateForCategories(leaf: DefNode, visibleNodeIds: Set<string>): LearnState {
  const base = learnStateForNode(leaf);
  return base === 'off' && visibleNodeIds.has(leaf.id) ? 'visible' : base;
}

function buildCategoryTree(raw: Raw, rendered: DefGraph) {
  const byId = raw.byId;
  const visibleNodeIds = computeVisibleSetFromRendered(rendered);

  const { levelByGroup } = computeGroupLevels(raw);

  const root: TreeNode = { id: '', name: '', kind: 'group', depth: 0, children: [], groupLevel: 0 };

  // Insert leaves into a folder-like tree based on id path parts.
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
        // Ensure computed group level is present even if node existed.
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
      leaf: byId.get(leaf.id) ?? leaf,
    };
    cur.children.push(leafNode);
  }

  const sortChildren = (n: TreeNode) => {
    for (const c of n.children) sortChildren(c);

    n.children.sort((a, b) => {
      if (a.kind !== b.kind) return a.kind === 'group' ? -1 : 1;

      if (a.kind === 'group' && b.kind === 'group') {
        return compareGroupsTopologicalLevel(a, b);
      }

      // leaf sort: 1) state 2) level 3) title
      const la = a.leaf!;
      const lb = b.leaf!;

      const sa = stateForCategories(la, visibleNodeIds);
      const sb = stateForCategories(lb, visibleNodeIds);
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

function renderCategoriesTree(raw: Raw, rendered: DefGraph) {
  const host = document.getElementById('categoriesTree') as HTMLDivElement | null;
  if (!host) return;

  const { root, visibleNodeIds } = buildCategoryTree(raw, rendered);

  host.innerHTML = '';

  const isOpen = (prefix: string) => {
    // Root is always open; groups default to open unless explicitly collapsed.
    if (!prefix) return true;
    return !openPrefixes.has(prefix);
  };

  const setOpen = (prefix: string, open: boolean) => {
    if (!prefix) return;
    // We store "collapsed" prefixes for simpler defaults.
    if (open) openPrefixes.delete(prefix);
    else openPrefixes.add(prefix);
    saveOpenPrefixes(openPrefixes);
  };

  const leafIdsUnderPrefix = (prefix: string) => {
    if (!prefix) return raw.def.nodes.map((n) => n.id);
    return raw.childrenByPrefix.get(prefix) ?? [];
  };

  const renderNode = (n: TreeNode) => {
    // Skip rendering children if parent is closed.
    const open = n.kind === 'group' ? isOpen(n.id) : true;

    if (n.id !== '') {
      const row = document.createElement('div');
      row.className = 'treeRow';
      row.style.setProperty('--indent', String(Math.max(0, n.depth - 1)));

      const indent = document.createElement('span');
      indent.className = 'treeIndent';
      row.appendChild(indent);

      const chevron = document.createElement('span');
      chevron.className = 'treeChevron';
      chevron.textContent = '▶';
      row.appendChild(chevron);

      const cb = document.createElement('input');
      cb.type = 'checkbox';
      cb.className = 'treeCheckbox';

      const label = document.createElement('span');
      label.className = 'treeLabel';

      const meta = document.createElement('span');
      meta.className = 'treeMeta';

      if (n.kind === 'group') {
        const childLeafIds = leafIdsUnderPrefix(n.id);
        const allIncluded = childLeafIds.length ? childLeafIds.every((id) => isIncluded(id)) : true;
        const anyIncluded = childLeafIds.some((id) => isIncluded(id));

        cb.checked = allIncluded;
        // Make it show indeterminate when mixed.
        cb.indeterminate = anyIncluded && !allIncluded;

        label.textContent = n.name;

        row.classList.add('hasChildren');
        row.classList.add('clickable');
        chevron.classList.toggle('open', open);

        // Toggle open/close on row click (not on checkbox).
        row.onclick = (ev) => {
          const t = ev.target as HTMLElement | null;
          if (t && (t.tagName === 'INPUT')) return;
          setOpen(n.id, !open);
          renderCategoriesTree(raw, lastRendered ?? rendered);
        };

        cb.onchange = () => {
          const next = cb.checked;
          setIncludedMany(childLeafIds, next);
          rerender(true);
          renderCategoriesTree(raw, lastRendered ?? rendered);
        };

        // Keep group labels from wrapping.
        meta.textContent = '';

        // Show computed group level.
        const lvl = document.createElement('span');
        lvl.textContent = `L${n.groupLevel ?? 0}`;
        meta.appendChild(lvl);
      } else {
        const leaf = n.leaf!;
        cb.checked = isIncluded(leaf.id);

        const st = stateForCategories(leaf, visibleNodeIds);
        const dot = document.createElement('span');
        dot.className = `stateDot ${st}`;
        meta.appendChild(dot);

        const lvl = document.createElement('span');
        lvl.textContent = `L${leaf.level ?? 0}`;
        meta.appendChild(lvl);

        label.textContent = leaf.title;

        row.classList.add('clickable');
        row.onclick = (ev) => {
          const t = ev.target as HTMLElement | null;
          if (t && (t.tagName === 'INPUT')) return;
          // Selecting a definition from Categories behaves like clicking in the graph.
          setBottomTab('definition');
          selectLeafById(leaf.id);

          // Ensure panel is expanded.
          if (bottomPanelEl && !bottomPanelEl.classList.contains('expanded')) {
            setPanelCollapsed(false);
          }
        };

        cb.onchange = () => {
          setIncluded(leaf.id, cb.checked);
          rerender(true);
          renderCategoriesTree(raw, lastRendered ?? rendered);
        };
      }

      row.appendChild(cb);
      row.appendChild(label);
      row.appendChild(meta);

      host.appendChild(row);
    }

    if (n.kind === 'group' && open) {
      for (const c of n.children) renderNode(c);
    }
  };

  renderNode(root);
}

function renderGraph(raw: Raw, state: UIState): DefGraph {
  const includeLeaf = (id: string) => isIncluded(id);

  const nodes = raw.def.nodes
    .filter((n) => includeLeaf(n.id))
    .map((n) => ({
      ...n,
      level: 0,
    }));

  // Keep only edges where both ends exist.
  const nodeSet = new Set(nodes.map((n) => n.id));
  const edges = raw.def.edges.filter((e) => nodeSet.has(e.source) && nodeSet.has(e.target)).map((e) => ({ ...e }));

  // Assign deps from edges (projected deps, used for level layout).
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

function bindInteractions(nodeSel: d3.Selection<SVGGElement, DefNode, SVGGElement, unknown>) {
  // Ensure we don't overwrite existing hover handlers added in draw()
  nodeSel
    .on('click.interact', (ev: MouseEvent, d: DefNode) => {
      ev.preventDefault();
      ev.stopPropagation();

      // clicking a rendered node opens its definition.
      setBottomTab('definition');
      selectLeafById(d.id);
      return;
    });
}

// -------------------------------
// App bootstrap / state
// -------------------------------

const rawPromise: Promise<Raw> = fetch('./defs.json')
  .then((r) => r.json())
  .then((def: DefGraph) => buildRaw(def));

const state: UIState = {
  selectedLeaf: undefined,
};

let lastRendered: DefGraph | null = null;

function focusHighestActiveRing() {
  if (!lastRendered) return;

  const maxLevel = Math.max(0, ...lastRendered.nodes.map((n) => n.level ?? 0));

  // Prefer highest ring that has something actionable/achieved.
  let best = maxLevel;
  for (let level = maxLevel; level >= 0; level--) {
    const has = lastRendered.nodes.some((n) => {
      if ((n.level ?? 0) !== level) return false;
      const s = learnStateForNode(n);
      return s === 'ready' || s === 'learned';
    });
    if (has) {
      best = level;
      break;
    }
  }

  focusRing(best);
  setRingHighlight(best);
}

function rerender(keepTransform: boolean) {
  const current = keepTransform ? d3.zoomTransform(svg.node() as any) : null;

  rawPromise
    .then((r) => {
      raw = r;
      console.log(`Rendering graph with ${r.def.nodes.length} definitions...`);
      // On reload, if there is no manual selection stored, derive initial selection from "ready".
      // If there IS a stored selection, keep it (manual overrides).
      if (loadIncludedFromStorage() === null) {
        recomputeIncludedSetFromReady(r);
      } else {
        includedIds = loadIncludedFromStorage();
      }

      const rendered = renderGraph(r, state);
      lastRendered = rendered;
      draw(rendered);

      // Keep current zoom/pan transform when re-rendering due to UI actions.
      if (current) {
        svg.call(zoom.transform as any, current);
      }

      // Keep ring highlight consistent with selection after redraw.
      applyRingHighlight();

      // Auto-select a "next ready" definition on initial load if nothing is selected.
      // (Also shows the definition content immediately.)
      if (!state.selectedLeaf) {
        // Ensure panel is expanded so content is visible immediately.
        if (bottomPanelEl && !bottomPanelEl.classList.contains('expanded')) {
          setPanelCollapsed(false);
        }
        const selected = selectNextReadyDefinition(r, rendered);
        if (!selected) {
          // Fallback: keep old behavior if there's nothing ready.
          requestAnimationFrame(() => {
            focusHighestActiveRing();
          });
        }
      }

      // Keep viewer updated if we have a selected leaf.
      if (state.selectedLeaf) {
        const n = rendered.nodes.find((x: DefNode) => x.id === state.selectedLeaf);
        if (n) void openLeaf(n);
      }

      renderCategoriesTree(r, rendered);
    })
    .catch((err) => {
      // eslint-disable-next-line no-console
      console.error(err);
    });
}

function focusRing(level: number) {
  if (!lastRendered) return;

  // Use the actual layout used during the last draw() to avoid ring spacing mismatch.
  const layout = lastLayout ?? radialLayout(lastRendered);
  const r = layout.base + level * layout.ringGap;

  // Fit the circle to viewport.
  const pad = 60;
  const width = W();
  const height = H();

  const diameter = 2 * r + pad;
  const scale = Math.max(0.12, Math.min(6, Math.min(width / diameter, height / diameter)));

  const tx = width / 2 - layout.cx * scale;
  const ty = height / 2 - layout.cy * scale;

  svg
    .transition()
    .duration(650)
    .call(zoom.transform as any, d3.zoomIdentity.translate(tx, ty).scale(scale));
}

function focusRingOfNode(id: string) {
  if (!lastRendered) return;
  const n = lastRendered.nodes.find((x: DefNode) => x.id === id);
  if (!n) return;
  focusRing(n.level ?? 0);
}

async function openLeaf(node: DefNode) {
  // Ensure pulsing matches whatever opened the viewer.
  selectedNodeId = node.id;
  applyRingHighlight();

  // Use preloaded content from defs.json if available
  const md = node.content || '(no content)';
  showViewer(node, md);
}

// Initial render
rerender(false);

// Bottom functional panel collapse/expand (persisted)
const PANEL_COLLAPSED_KEY = 'definit-db.ui.bottomPanelCollapsed';
const bottomPanelEl = document.getElementById('bottomPanel') as HTMLDivElement | null;
const togglePanelBtn = document.getElementById('togglePanel') as HTMLButtonElement | null;
const mainPanelEl = document.getElementById('mainPanel') as HTMLDivElement | null;

function setPanelCollapsed(collapsed: boolean) {
  if (!bottomPanelEl || !togglePanelBtn) return;
  // Track if the state has changed
  const stateChanged = togglePanelBtn.getAttribute('aria-expanded') !== String(!collapsed);

  if (!stateChanged) return;

  bottomPanelEl.classList.toggle('expanded', !collapsed);
  mainPanelEl?.classList.toggle('expanded', !collapsed);

  togglePanelBtn.textContent = collapsed ? '▲' : '▼';
  togglePanelBtn.setAttribute('aria-expanded', String(!collapsed));

  try {
    localStorage.setItem(PANEL_COLLAPSED_KEY, collapsed ? '1' : '0');
  } catch {
    // ignore
  }

  requestAnimationFrame(() => {
    focusHighestActiveRing();
  });
}

if (bottomPanelEl && togglePanelBtn) {
  let initialCollapsed = false;
  try {
    initialCollapsed = localStorage.getItem(PANEL_COLLAPSED_KEY) === '1';
  } catch {
    initialCollapsed = false;
  }

  setPanelCollapsed(initialCollapsed);

  togglePanelBtn.addEventListener('click', (ev) => {
    ev.preventDefault();
    const collapsed = !bottomPanelEl.classList.contains('expanded');
    setPanelCollapsed(!collapsed);
  });
}

// Bottom panel tabs
const tabDefinitionBtn = document.getElementById('tabDefinition') as HTMLButtonElement | null;
const tabCategoriesBtn = document.getElementById('tabCategories') as HTMLButtonElement | null;
const tabGraphBtn = document.getElementById('tabGraph') as HTMLButtonElement | null;
const tabPageDefinition = document.getElementById('tabPageDefinition') as HTMLDivElement | null;
const tabPageCategories = document.getElementById('tabPageCategories') as HTMLDivElement | null;
const tabPageGraph = document.getElementById('tabPageGraph') as HTMLDivElement | null;

function setBottomTab(tab: BottomTab) {
  const isDef = tab === 'definition';
  const isCat = tab === 'categories';
  const isGraph = tab === 'graph';

  tabDefinitionBtn?.classList.toggle('active', isDef);
  tabCategoriesBtn?.classList.toggle('active', isCat);
  tabGraphBtn?.classList.toggle('active', isGraph);

  tabDefinitionBtn?.setAttribute('aria-selected', String(isDef));
  tabCategoriesBtn?.setAttribute('aria-selected', String(isCat));
  tabGraphBtn?.setAttribute('aria-selected', String(isGraph));

  tabPageDefinition?.classList.toggle('active', isDef);
  tabPageCategories?.classList.toggle('active', isCat);
  tabPageGraph?.classList.toggle('active', isGraph);

  // Refresh categories content when tab is opened.
  if (isCat && raw && lastRendered) {
    renderCategoriesTree(raw, lastRendered);
  }
}

tabDefinitionBtn?.addEventListener('click', (ev) => {
  ev.preventDefault();
  setBottomTab('definition');
});

tabCategoriesBtn?.addEventListener('click', (ev) => {
  ev.preventDefault();
  setBottomTab('categories');
  // Keep the graph as-is; this is only a panel tab.
});

tabGraphBtn?.addEventListener('click', (ev) => {
  ev.preventDefault();
  setBottomTab('graph');
});

// Default tab
setBottomTab('definition');

// Progress button: focus highest ring that has at least one node not "off" (ready/learned preferred)
const progressBtn = (document.getElementById('progress')) as
  | HTMLButtonElement
  | null;
progressBtn?.addEventListener('click', () => {
  // Clear selection + viewer to behave like entering Focus mode.
  state.selectedLeaf = undefined;
  selectedNodeId = null;
  hideViewer();

  // Reset visibility selection to the same default as a fresh load with no stored selection:
  // derived from current READY nodes.
  if (raw) {
    recomputeIncludedSetFromReady(raw);
  }

  rerender(true);
  requestAnimationFrame(() => {
    if (raw && lastRendered) {
      // In Focus, immediately jump to the next definition to learn.
      // (this also opens the definition viewer)
      const selected = selectNextReadyDefinition(raw, lastRendered);
      if (!selected) focusHighestActiveRing();
    } else {
      focusHighestActiveRing();
    }
  });
});

// Overview button: fit whole graph into view
const overviewBtn = (document.getElementById('overview') ?? document.getElementById('focus')) as HTMLButtonElement | null;
overviewBtn?.addEventListener('click', () => {
  if (!lastRendered) return;
  const maxLevel = Math.max(0, ...lastRendered.nodes.map((n) => n.level ?? 0));
  focusRing(maxLevel);
  setRingHighlight(maxLevel);
});

// Reset progress button
const resetBtn = (document.getElementById('resetProgress') ?? document.getElementById('reset')) as HTMLButtonElement | null;
resetBtn?.addEventListener('click', () => {
  // If there's nothing to reset, do nothing (button should be disabled anyway).
  if (!hasAnyLearned()) {
    updateResetProgressButton();
    return;
  }

  const overlay = document.getElementById('resetConfirmOverlay') as HTMLDivElement | null;
  const closeBtn = document.getElementById('resetConfirmClose') as HTMLButtonElement | null;
  const cancelBtn = document.getElementById('resetConfirmCancel') as HTMLButtonElement | null;
  const okBtn = document.getElementById('resetConfirmOk') as HTMLButtonElement | null;

  if (!overlay || !closeBtn || !cancelBtn || !okBtn) {
    console.error('Missing reset confirmation elements');
    return;
  }

  const open = () => overlay.classList.add('open');
  const close = () => overlay.classList.remove('open');

  // Avoid stacking handlers if user clicks multiple times.
  closeBtn.onclick = (ev) => {
    ev.preventDefault();
    ev.stopPropagation();
    close();
  };

  cancelBtn.onclick = (ev) => {
    ev.preventDefault();
    ev.stopPropagation();
    close();
  };

  okBtn.onclick = (ev) => {
    ev.preventDefault();
    ev.stopPropagation();

    close();

    console.log('Resetting progress...');
    clearLearnedProgress();
    saveLearnedToStorage();
    hideViewer();

    updateResetProgressButton();
    rerender(true);
  };

  // Click outside modal closes it
  overlay.onclick = (ev) => {
    if (ev.target === overlay) close();
  };

  // ESC closes it (only while open)
  const onKeyDown = (ev: KeyboardEvent) => {
    if (ev.key !== 'Escape') return;
    if (!overlay.classList.contains('open')) return;
    close();
  };
  window.addEventListener('keydown', onKeyDown, { passive: true });

  open();
});

function selectNextReadyDefinition(rawGraph: Raw, rendered: DefGraph) {
  // compute or refresh levels on rendered graph so sorting is correct
  computeLevels(rendered.nodes);

  const ready = rendered.nodes.filter((n) => learnStateForNode(n) === 'ready');
  if (!ready.length) return false;

  // Precompute once to avoid recompute per compare
  const { levelByGroup } = computeGroupLevels(rawGraph);
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

  setBottomTab('definition');
  selectLeafById(ready[0].id);
  return true;
}
