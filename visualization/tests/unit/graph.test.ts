import { describe, expect, it } from 'vitest';

import defs from '../../../docs/defs.json';
import type { DefGraph } from '../../src/types';
import {
  buildFieldGroups,
  buildRaw,
  computeStats,
  computeTrackSet,
  computeVisibleSet,
  effectiveState,
  isDefaultTrackFilters,
  nodeMatchesQuery,
  normalizeId,
  prerequisiteClosure,
  referencesClosure,
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
        deps: [],
        content: '',
      },
      {
        id: 'math/root_b',
        title: 'root_b',
        deps: [],
        content: '',
      },
      {
        id: 'math/mid',
        title: 'mid',
        deps: ['math/root_a'],
        content: '',
      },
      {
        id: 'math/target',
        title: 'target',
        deps: ['math/mid'],
        content: '',
      },
      {
        id: 'cs/compound',
        title: 'compound',
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
    groups: [
      {
        id: 'group_math',
        name: 'Mathematics',
        definitions: ['math/root_a', 'math/root_b', 'math/mid', 'math/target'],
      },
    ],
  };
}

function makeTreeGraph(): DefGraph {
  return {
    nodes: [
      {
        id: 'math/root_a',
        title: 'root_a',
        deps: [],
        content: '',
      },
      {
        id: 'math/root_b',
        title: 'root_b',
        deps: [],
        content: '',
      },
      {
        id: 'math/mid',
        title: 'mid',
        deps: ['math/root_a'],
        content: '',
      },
      {
        id: 'math/analysis_ready_a',
        title: 'alpha ready',
        deps: [],
        content: '',
      },
      {
        id: 'math/analysis_ready_z',
        title: 'zeta ready',
        deps: [],
        content: '',
      },
      {
        id: 'math/analysis_learned',
        title: 'learned leaf',
        deps: [],
        content: '',
      },
      {
        id: 'math/analysis_preready',
        title: 'pre ready leaf',
        deps: ['math/root_a', 'math/root_b'],
        content: '',
      },
      {
        id: 'math/analysis_notready',
        title: 'not ready leaf',
        deps: ['math/mid'],
        content: '',
      },
      {
        id: 'cs/algo',
        title: 'algo',
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

  it('computes the references closure (all definitions the seeds reference)', () => {
    const raw = buildRaw(makeGraph());

    expect(Array.from(referencesClosure(raw, ['math/root_a'])).sort()).toEqual(['math/root_a']);
    expect(Array.from(referencesClosure(raw, ['math/target'])).sort()).toEqual([
      'math/mid',
      'math/root_a',
      'math/target',
    ]);
  });

  it('computes the track set from groups, extra definitions and references', () => {
    const raw = buildRaw(makeGraph());

    // Group only, no references: exactly the group members.
    expect(
      Array.from(
        computeTrackSet(raw, {
          includeReferences: false,
          groupIds: ['group_math'],
          definitionIds: [],
        }),
      ).sort(),
    ).toEqual(['math/mid', 'math/root_a', 'math/root_b', 'math/target']);

    // Extra definition pulls in that node itself, no more.
    expect(
      Array.from(
        computeTrackSet(raw, {
          includeReferences: false,
          groupIds: [],
          definitionIds: ['cs/compound'],
        }),
      ).sort(),
    ).toEqual(['cs/compound']);

    // With references: everything the seed references is included —
    // the basic definitions to learn first.
    expect(
      Array.from(
        computeTrackSet(raw, {
          includeReferences: true,
          groupIds: [],
          definitionIds: ['cs/compound'],
        }),
      ).sort(),
    ).toEqual(['cs/compound', 'math/root_a', 'math/root_b']);

    // math/target references math/mid which references math/root_a: the whole chain.
    expect(
      Array.from(
        computeTrackSet(raw, {
          includeReferences: true,
          groupIds: [],
          definitionIds: ['math/target'],
        }),
      ).sort(),
    ).toEqual(['math/mid', 'math/root_a', 'math/target']);

    // Unknown group and definition ids are ignored.
    expect(
      Array.from(
        computeTrackSet(raw, {
          includeReferences: false,
          groupIds: ['ghost'],
          definitionIds: ['ghost/id'],
        }),
      ),
    ).toEqual([]);
  });

  it('detects default track filters', () => {
    const defaults = { includeReferences: true, groupIds: ['group_math'], definitionIds: [] };

    expect(isDefaultTrackFilters(defaults, defaults)).toBe(true);
    expect(
      isDefaultTrackFilters({ ...defaults, includeReferences: false }, defaults),
    ).toBe(false);
    expect(isDefaultTrackFilters({ ...defaults, definitionIds: ['cs/compound'] }, defaults)).toBe(
      false,
    );
    // Order-insensitive comparison of the id lists.
    expect(isDefaultTrackFilters({ ...defaults, groupIds: ['group_math'] }, defaults)).toBe(true);
  });

  it('matches search queries against id, title and aliases', () => {
    const node = {
      id: 'cs/depth_first_search',
      title: 'depth_first_search',
      aliases: ['DFS', 'depth first search'],
      deps: [],
      content: '',
    };

    expect(nodeMatchesQuery(node, 'depth')).toBe(true);
    expect(nodeMatchesQuery(node, 'cs/depth')).toBe(true);
    expect(nodeMatchesQuery(node, 'dfs')).toBe(true);
    expect(nodeMatchesQuery(node, 'depth first')).toBe(true);
    expect(nodeMatchesQuery(node, 'breadth')).toBe(false);
    expect(nodeMatchesQuery(node, '')).toBe(false);
  });

  it('selects the next ready definition using rendered levels and stable ordering', () => {
    const raw = buildRaw(makeGraph());
    const rendered = renderGraph(raw, new Set(['math/root_a', 'math/root_b', 'math/mid']));

    expect(selectNextReady(raw, rendered, new Set(['math/root_a']))).toBe('math/root_b');
    expect(selectNextReady(raw, rendered, new Set(['math/root_a', 'math/root_b']))).toBe('math/mid');
  });

  it('groups definitions by field and sorts them by state, level, and title', () => {
    const raw = buildRaw(makeTreeGraph());
    const rendered = renderGraph(raw, null);
    const { groups } = buildFieldGroups(raw, rendered, new Set(['math/root_a', 'math/analysis_learned']));

    expect(groups.map((group) => group.field)).toEqual(['cs', 'math']);

    const computerScience = groups.find((group) => group.field === 'cs');
    expect(computerScience?.definitions.map((def) => def.id)).toEqual(['cs/algo']);

    const mathematics = groups.find((group) => group.field === 'math');
    expect(mathematics?.definitions.map((def) => def.id)).toEqual([
      'math/analysis_ready_a',
      'math/root_b',
      'math/analysis_ready_z',
      'math/mid',
      'math/analysis_learned',
      'math/root_a',
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
    const nAryTree = renderedNodes.find((node) => node.id === 'mathematics/n_ary_tree');

    expect(nAryTree).toBeTruthy();

    const html = renderMdToHtml(nAryTree!.content, nAryTree!.deps, renderedNodes);

    expect(html).toContain('data-dep="mathematics/tree"');
    expect(html).toContain('>tree<');
    expect(html).toContain('data-dep="mathematics/node"');
  });
});