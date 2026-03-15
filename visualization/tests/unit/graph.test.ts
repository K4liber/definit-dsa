import { describe, expect, it } from 'vitest';

import defs from '../../../docs/defs.json';
import type { DefGraph } from '../../src/types';
import {
  buildCategoryTree,
  buildRaw,
  computeStats,
  computeGroupLevels,
  computeVisibleSet,
  effectiveState,
  normalizeId,
  prerequisiteClosure,
  renderMdToHtml,
  renderGraph,
  selectNextReady,
} from '../../src/lib/graph';

function makeGraph(): DefGraph {
  return {
    nodes: [
      {
        id: 'math/root_a',
        title: 'root_a',
        category: 'mathematics/fundamental/root_a',
        deps: [],
        content: '',
      },
      {
        id: 'math/root_b',
        title: 'root_b',
        category: 'mathematics/fundamental/root_b',
        deps: [],
        content: '',
      },
      {
        id: 'math/mid',
        title: 'mid',
        category: 'mathematics/analysis/mid',
        deps: ['math/root_a'],
        content: '',
      },
      {
        id: 'math/target',
        title: 'target',
        category: 'mathematics/analysis/target',
        deps: ['math/mid'],
        content: '',
      },
      {
        id: 'cs/compound',
        title: 'compound',
        category: 'computer_science/algorithms/compound',
        deps: ['math/root_a', 'math/root_b'],
        content: '',
      },
    ],
    edges: [
      { source: 'math/mid', target: 'math/root_a' },
      { source: 'math/target', target: 'math/mid' },
      { source: 'cs/compound', target: 'math/root_a' },
      { source: 'cs/compound', target: 'math/root_b' },
    ],
  };
}

function makeTreeGraph(): DefGraph {
  return {
    nodes: [
      {
        id: 'math/root_a',
        title: 'root_a',
        category: 'mathematics/fundamental/root_a',
        deps: [],
        content: '',
      },
      {
        id: 'math/root_b',
        title: 'root_b',
        category: 'mathematics/fundamental/root_b',
        deps: [],
        content: '',
      },
      {
        id: 'math/mid',
        title: 'mid',
        category: 'mathematics/fundamental/mid',
        deps: ['math/root_a'],
        content: '',
      },
      {
        id: 'math/analysis_ready_a',
        title: 'alpha ready',
        category: 'mathematics/analysis/alpha_ready',
        deps: [],
        content: '',
      },
      {
        id: 'math/analysis_ready_z',
        title: 'zeta ready',
        category: 'mathematics/analysis/zeta_ready',
        deps: [],
        content: '',
      },
      {
        id: 'math/analysis_learned',
        title: 'learned leaf',
        category: 'mathematics/analysis/learned_leaf',
        deps: [],
        content: '',
      },
      {
        id: 'math/analysis_preready',
        title: 'pre ready leaf',
        category: 'mathematics/analysis/pre_ready_leaf',
        deps: ['math/root_a', 'math/root_b'],
        content: '',
      },
      {
        id: 'math/analysis_notready',
        title: 'not ready leaf',
        category: 'mathematics/analysis/not_ready_leaf',
        deps: ['math/mid'],
        content: '',
      },
      {
        id: 'cs/algo',
        title: 'algo',
        category: 'computer_science/algorithms/algo',
        deps: ['math/root_a'],
        content: '',
      },
    ],
    edges: [
      { source: 'math/mid', target: 'math/root_a' },
      { source: 'math/analysis_preready', target: 'math/root_a' },
      { source: 'math/analysis_preready', target: 'math/root_b' },
      { source: 'math/analysis_notready', target: 'math/mid' },
      { source: 'cs/algo', target: 'math/root_a' },
    ],
  };
}

describe('graph helpers', () => {
  it('normalizes ids for search and matching', () => {
    expect(normalizeId('  Fibonacci Number!? / Intro  ')).toBe('fibonacci_number_/_intro');
  });

  it('recomputes levels on the rendered graph after filtering hidden prerequisites', () => {
    const raw = buildRaw(makeGraph());
    const rendered = renderGraph(raw, new Set(['math/mid', 'math/target']));
    const byId = new Map(rendered.nodes.map((node) => [node.id, node] as const));

    expect(rendered.edges).toEqual([{ source: 'math/target', target: 'math/mid' }]);
    expect(byId.get('math/mid')?.deps).toEqual(['math/root_a']);
    expect(byId.get('math/mid')?.level).toBe(0);
    expect(byId.get('math/target')?.level).toBe(1);
  });

  it('marks partially unlocked nodes as pre-ready through the visible set', () => {
    const raw = buildRaw(makeGraph());
    const rendered = renderGraph(raw, new Set(['math/root_a', 'math/root_b', 'cs/compound']));
    const visible = computeVisibleSet(rendered, new Set(['math/root_a']));
    const compound = rendered.nodes.find((node) => node.id === 'cs/compound');

    expect(visible.has('cs/compound')).toBe(true);
    expect(compound).toBeTruthy();
    expect(effectiveState(compound!, new Set(['math/root_a']), visible)).toBe('pre-ready');
  });

  it('returns the prerequisite closure including the selected node', () => {
    const raw = buildRaw(makeGraph());

    expect(Array.from(prerequisiteClosure(raw, 'math/target')).sort()).toEqual([
      'math/mid',
      'math/root_a',
      'math/target',
    ]);
  });

  it('selects the next ready definition using rendered levels and stable ordering', () => {
    const raw = buildRaw(makeGraph());
    const rendered = renderGraph(raw, new Set(['math/root_a', 'math/root_b', 'math/mid']));

    expect(selectNextReady(raw, rendered, new Set(['math/root_a']))).toBe('math/root_b');
    expect(selectNextReady(raw, rendered, new Set(['math/root_a', 'math/root_b']))).toBe('math/mid');
  });

  it('computes group levels from cross-group dependencies', () => {
    const raw = buildRaw(makeTreeGraph());
    const { levelByGroup } = computeGroupLevels(raw);

    expect(levelByGroup.get('mathematics')).toBe(0);
    expect(levelByGroup.get('mathematics/fundamental')).toBe(0);
    expect(levelByGroup.get('mathematics/analysis')).toBe(1);
    expect(levelByGroup.get('computer_science')).toBe(1);
    expect(levelByGroup.get('computer_science/algorithms')).toBe(1);
  });

  it('sorts category groups by computed group level and leaves by state, level, and title', () => {
    const raw = buildRaw(makeTreeGraph());
    const rendered = renderGraph(raw, null);
    const { root } = buildCategoryTree(raw, rendered, new Set(['math/root_a', 'math/analysis_learned']));

    expect(root.children.map((child) => child.id)).toEqual(['mathematics', 'computer_science']);

    const mathematics = root.children.find((child) => child.id === 'mathematics');
    expect(mathematics?.children.map((child) => child.id)).toEqual([
      'mathematics/fundamental',
      'mathematics/analysis',
    ]);

    const analysis = mathematics?.children.find((child) => child.id === 'mathematics/analysis');
    expect(analysis?.children.map((child) => child.id)).toEqual([
      'math/analysis_ready_a',
      'math/analysis_ready_z',
      'math/analysis_learned',
      'math/analysis_preready',
      'math/analysis_notready',
    ]);
  });

  it('computes progress stats for learned definitions, unlocked edges, and completed levels', () => {
    const raw = buildRaw(makeGraph());
    const rendered = renderGraph(raw, null);
    const stats = computeStats(rendered, new Set(['math/root_a', 'math/root_b']));

    expect(stats).toEqual({
      totalDefs: 5,
      learnedDefs: 2,
      totalEdges: 4,
      unlockedEdges: 3,
      totalLevels: 3,
      completedLevels: 1,
    });
  });

  it('renders dependency links as clickable spans in definition HTML', () => {
    const renderedNodes = (defs as DefGraph).nodes;
    const kAryTree = renderedNodes.find((node) => node.id === 'mathematics/k_ary_tree');

    expect(kAryTree).toBeTruthy();

    const html = renderMdToHtml(kAryTree!.content, kAryTree!.deps, renderedNodes);

    expect(html).toContain('data-dep="mathematics/n-ary_tree"');
    expect(html).toContain('>n-ary tree<');
    expect(html).toContain('data-dep="mathematics/node"');
  });
});