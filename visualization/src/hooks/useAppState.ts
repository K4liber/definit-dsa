import { useReducer, useCallback, useEffect, useMemo, useRef } from 'react';
import defs from '../../../docs/defs.json';
import type { DefGraph, DefNode, Raw, LearnState } from '../types';
import type { BottomTab } from '../types';
import {
  buildRaw,
  computeTrackSet,
  renderGraph,
  selectNextReady,
  nodeMatchesQuery,
} from '../lib/graph';
import {
  DEFAULT_FILTERS,
  DEFAULT_TRACK_FILTERS,
  DEFAULT_VISUALIZATION_FILTERS,
  cloneFilters,
  trackEquals,
  type PersistedFilters,
  type TrackFilters,
  type VisualizationFilters,
} from '../lib/filters';
import {
  loadLearnedFromStorage,
  saveLearnedToStorage,
  clearLearnedFromStorage,
  loadFiltersFromStorage,
  saveFiltersToStorage,
  clearFiltersFromStorage,
  loadPanelCollapsed,
  savePanelCollapsed,
} from '../lib/storage';

/* ------------------------------------------------------------------ */
/*  Reducer state shape                                               */
/* ------------------------------------------------------------------ */

type ReducerState = {
  // Graph data
  raw: Raw | null;
  learned: Set<string>;
  selectedLeafId: string | null;
  // Bottom panel state
  panelCollapsed: boolean;
  activeTab: BottomTab;
  // Search
  searchQuery: string;
  // Filters (persisted)
  filters: PersistedFilters;
  // Modal states
  infoOpen: boolean;
  resetConfirmOpen: boolean;
};

function initialReducerState(): ReducerState {
  return {
    raw: null,
    learned: loadLearnedFromStorage(),
    selectedLeafId: null,
    panelCollapsed: loadPanelCollapsed(),
    activeTab: 'definition',
    searchQuery: '',
    filters: cloneFilters(DEFAULT_FILTERS),
    infoOpen: false,
    resetConfirmOpen: false,
  };
}

/* ------------------------------------------------------------------ */
/*  Action types                                                       */
/* ------------------------------------------------------------------ */

const enum A {
  DATA_LOADED = 'DATA_LOADED',
  INIT_COMPLETE = 'INIT_COMPLETE',
  MARK_LEARNED = 'MARK_LEARNED',
  AUTO_SELECT_NEXT = 'AUTO_SELECT_NEXT',
  RESET_PROGRESS = 'RESET_PROGRESS',
  SELECT_LEAF = 'SELECT_LEAF',
  CLEAR_SELECTION = 'CLEAR_SELECTION',
  SET_PANEL_COLLAPSED = 'SET_PANEL_COLLAPSED',
  SET_ACTIVE_TAB = 'SET_ACTIVE_TAB',
  SET_SEARCH_QUERY = 'SET_SEARCH_QUERY',
  SET_TRACK_FILTERS = 'SET_TRACK_FILTERS',
  SET_VISUALIZATION_FILTERS = 'SET_VISUALIZATION_FILTERS',
  RESET_FILTERS = 'RESET_FILTERS',
  SET_INFO_OPEN = 'SET_INFO_OPEN',
  SET_RESET_CONFIRM_OPEN = 'SET_RESET_CONFIRM_OPEN',
  FOCUS_MODE = 'FOCUS_MODE',
}

/* ------------------------------------------------------------------ */
/*  Actions                                                            */
/* ------------------------------------------------------------------ */

type Action =
  | { type: A.DATA_LOADED; raw: Raw }
  | { type: A.INIT_COMPLETE; selectedLeafId: string | null; showInfo: boolean }
  | { type: A.MARK_LEARNED; id: string }
  | { type: A.AUTO_SELECT_NEXT; selectedLeafId: string | null }
  | { type: A.RESET_PROGRESS }
  | { type: A.SELECT_LEAF; id: string }
  | { type: A.CLEAR_SELECTION }
  | { type: A.SET_PANEL_COLLAPSED; collapsed: boolean }
  | { type: A.SET_ACTIVE_TAB; tab: BottomTab }
  | { type: A.SET_SEARCH_QUERY; query: string }
  | { type: A.SET_TRACK_FILTERS; track: TrackFilters }
  | { type: A.SET_VISUALIZATION_FILTERS; visualization: VisualizationFilters }
  | { type: A.RESET_FILTERS }
  | { type: A.SET_INFO_OPEN; open: boolean }
  | { type: A.SET_RESET_CONFIRM_OPEN; open: boolean }
  | { type: A.FOCUS_MODE; selectedLeafId: string | null };

/* ------------------------------------------------------------------ */
/*  Reducer                                                            */
/* ------------------------------------------------------------------ */

function reducer(state: ReducerState, action: Action): ReducerState {
  switch (action.type) {
    case A.DATA_LOADED: {
      // Load persisted filters only once the known groups/definitions are
      // available, so stale ids can be sanitized away.
      const groupIds = new Set((action.raw.def.groups ?? []).map((g) => g.id));
      const nodeIds = new Set(action.raw.def.nodes.map((n) => n.id));
      const filters = loadFiltersFromStorage(groupIds, nodeIds);
      return { ...state, raw: action.raw, filters };
    }

    case A.INIT_COMPLETE:
      return {
        ...state,
        selectedLeafId: action.selectedLeafId,
        infoOpen: action.showInfo || state.infoOpen,
        activeTab: action.selectedLeafId ? 'definition' : state.activeTab,
        panelCollapsed: state.panelCollapsed,
      };

    case A.MARK_LEARNED: {
      const next = new Set(state.learned);
      next.add(action.id);
      saveLearnedToStorage(next);
      return { ...state, learned: next };
    }

    case A.AUTO_SELECT_NEXT:
      return {
        ...state,
        selectedLeafId: action.selectedLeafId,
        activeTab: action.selectedLeafId ? 'definition' : state.activeTab,
      };

    case A.RESET_PROGRESS:
      clearLearnedFromStorage();
      saveLearnedToStorage(new Set());
      clearFiltersFromStorage();
      return {
        ...state,
        learned: new Set(),
        filters: cloneFilters(DEFAULT_FILTERS),
        selectedLeafId: null,
        resetConfirmOpen: false,
      };

    case A.SELECT_LEAF:
      savePanelCollapsed(false);
      return {
        ...state,
        selectedLeafId: action.id,
        activeTab: 'definition',
        panelCollapsed: false,
      };

    case A.CLEAR_SELECTION:
      return { ...state, selectedLeafId: null };

    case A.SET_PANEL_COLLAPSED:
      savePanelCollapsed(action.collapsed);
      return { ...state, panelCollapsed: action.collapsed };

    case A.SET_ACTIVE_TAB:
      return { ...state, activeTab: action.tab };

    case A.SET_SEARCH_QUERY:
      return { ...state, searchQuery: action.query };

    case A.SET_TRACK_FILTERS: {
      const filters: PersistedFilters = {
        track: action.track,
        visualization: state.filters.visualization,
      };
      saveFiltersToStorage(filters);
      return { ...state, filters };
    }

    case A.SET_VISUALIZATION_FILTERS: {
      const filters: PersistedFilters = {
        track: state.filters.track,
        visualization: action.visualization,
      };
      saveFiltersToStorage(filters);
      return { ...state, filters };
    }

    case A.RESET_FILTERS: {
      const filters = cloneFilters(DEFAULT_FILTERS);
      saveFiltersToStorage(filters);
      return { ...state, filters, searchQuery: '' };
    }

    case A.SET_INFO_OPEN:
      return { ...state, infoOpen: action.open };

    case A.SET_RESET_CONFIRM_OPEN:
      return { ...state, resetConfirmOpen: action.open };

    case A.FOCUS_MODE:
      return {
        ...state,
        selectedLeafId: action.selectedLeafId,
        // Do not change activeTab / panelCollapsed; focus must not affect panel visibility
      };

    default:
      return state;
  }
}

/* ------------------------------------------------------------------ */
/*  Public types                                                       */
/* ------------------------------------------------------------------ */

export type AppState = {
  raw: Raw | null;
  rendered: DefGraph | null;
  /** Graph restricted to the current track (before visualization filters). */
  trackGraph: DefGraph | null;
  learned: Set<string>;
  selectedLeafId: string | null;
  selectedNode: DefNode | null;
  panelCollapsed: boolean;
  activeTab: BottomTab;
  searchQuery: string;
  searchMatches: DefNode[];
  filters: PersistedFilters;
  filtersAreDefault: boolean;
  infoOpen: boolean;
  resetConfirmOpen: boolean;
};

export type AppActions = {
  markLearned: (id: string) => void;
  resetProgress: () => void;
  selectLeaf: (id: string) => void;
  clearSelection: () => void;
  setPanelCollapsed: (collapsed: boolean) => void;
  setActiveTab: (tab: BottomTab) => void;
  setSearchQuery: (q: string) => void;
  setTrackFilters: (track: TrackFilters) => void;
  setVisualizationFilters: (visualization: VisualizationFilters) => void;
  resetFilters: () => void;
  setInfoOpen: (open: boolean) => void;
  setResetConfirmOpen: (open: boolean) => void;
  focusMode: () => void;
  overviewMode: () => void;
  getNextReadyId: () => string | null;
};

/* ------------------------------------------------------------------ */
/*  Hook                                                              */
/* ------------------------------------------------------------------ */

export function useAppState(): AppState & AppActions {
  const [state, dispatch] = useReducer(reducer, undefined, initialReducerState);

  // ── Load bundled data on mount ───────────────────────────────────
  useEffect(() => {
    const raw = buildRaw(defs as DefGraph);
    dispatch({ type: A.DATA_LOADED, raw });
  }, []);

  // ── Derive search matches for dropdown (id/title/aliases) ────────
  const searchMatches = useMemo<DefNode[]>(() => {
    if (!state.raw) return [];
    if (!state.searchQuery.trim()) return [];

    const matches = state.raw.def.nodes.filter((n) => nodeMatchesQuery(n, state.searchQuery));
    matches.sort((a, b) => a.id.localeCompare(b.id));
    return matches.slice(0, 80);
  }, [state.raw, state.searchQuery]);

  // ── Track graph: groups + definitions (+ descendants) ────────────
  const trackGraph = useMemo<DefGraph | null>(() => {
    if (!state.raw) return null;
    const trackSet = computeTrackSet(state.raw, state.filters.track);
    if (trackSet.size === 0) return { nodes: [], edges: [] };
    return renderGraph(state.raw, trackSet);
  }, [state.raw, state.filters.track]);

  // ── Final rendered graph: visualization filters on top of track ──
  const rendered = useMemo<DefGraph | null>(() => {
    if (!state.raw || !trackGraph) return null;
    if (trackGraph.nodes.length === 0) return trackGraph;

    const learned = state.learned;
    const v = state.filters.visualization;

    const byId = new Map(trackGraph.nodes.map((n) => [n.id, n] as const));
    const preReadySet = new Set<string>();
    for (const e of trackGraph.edges) {
      if (!learned.has(e.target)) continue;
      const dep = byId.get(e.source);
      if (!dep || learned.has(dep.id)) continue;
      const deps = dep.deps ?? [];
      if (!deps.every((d) => learned.has(d))) preReadySet.add(dep.id);
    }

    const stateOf = (n: DefNode): LearnState => {
      if (learned.has(n.id)) return 'learned';
      const deps = n.deps ?? [];
      if (deps.every((d) => learned.has(d))) return 'ready';
      return preReadySet.has(n.id) ? 'pre-ready' : 'not-ready';
    };

    const keep = trackGraph.nodes.filter((n) => {
      const st = stateOf(n);
      if (st === 'learned') return v.showLearned;
      if (st === 'ready') return v.showReady;
      if (st === 'pre-ready') return v.showPreReady;
      return v.showNotReady;
    });

    if (keep.length === trackGraph.nodes.length) return trackGraph;
    return renderGraph(state.raw, new Set(keep.map((n) => n.id)));
  }, [trackGraph, state.learned, state.filters.visualization, state.raw]);

  // ── Derive selected node ─────────────────────────────────────────
  const selectedNode = useMemo<DefNode | null>(() => {
    if (!state.selectedLeafId || !state.raw) return null;
    // Look up in the full database so the definition content stays available
    // even when the node is filtered out of the current visualization.
    return state.raw.byId.get(state.selectedLeafId) ?? null;
  }, [state.raw, state.selectedLeafId]);

  // ── One-time initialization after data + graph are ready ─────────
  const initDone = useRef(false);
  useEffect(() => {
    if (!state.raw || !rendered || initDone.current) return;
    initDone.current = true;

    // Determine first definition to show from the CURRENTLY FILTERED graph,
    // so computed levels / ready set are consistent with the UI.
    const nextId = selectNextReady(state.raw, rendered, state.learned);

    dispatch({
      type: A.INIT_COMPLETE,
      selectedLeafId: nextId,
      showInfo: state.learned.size === 0,
    });
  }, [state.raw, rendered, state.learned]);

  // ── Auto-select next ready after marking learned ─────────────────────
  const pendingMarkId = useRef<string | null>(null);
  useEffect(() => {
    if (!pendingMarkId.current || !state.raw || !rendered) return;

    // Confirm the mark was applied (the id is now in the learned set)
    if (!state.learned.has(pendingMarkId.current)) return;
    pendingMarkId.current = null;

    // Select next ready within the CURRENTLY FILTERED graph
    const nextId = selectNextReady(state.raw, rendered, state.learned);
    dispatch({ type: A.AUTO_SELECT_NEXT, selectedLeafId: nextId });
  }, [state.raw, rendered, state.learned]);

  // ── Filters are at their default values? ─────────────────────────
  const filtersAreDefault = useMemo(
    () =>
      trackEquals(state.filters.track, DEFAULT_TRACK_FILTERS) &&
      JSON.stringify(state.filters.visualization) === JSON.stringify(DEFAULT_VISUALIZATION_FILTERS),
    [state.filters],
  );

  // ── Action creators ──────────────────────────────────────────────

  const markLearned = useCallback((id: string) => {
    pendingMarkId.current = id;
    dispatch({ type: A.MARK_LEARNED, id });
  }, []);

  const resetProgress = useCallback(() => {
    dispatch({ type: A.RESET_PROGRESS });
  }, []);

  const selectLeaf = useCallback((id: string) => {
    dispatch({ type: A.SELECT_LEAF, id });
  }, []);

  const clearSelection = useCallback(() => {
    dispatch({ type: A.CLEAR_SELECTION });
  }, []);

  const setPanelCollapsed = useCallback((collapsed: boolean) => {
    dispatch({ type: A.SET_PANEL_COLLAPSED, collapsed });
  }, []);

  const setActiveTab = useCallback((tab: BottomTab) => {
    dispatch({ type: A.SET_ACTIVE_TAB, tab });
  }, []);

  const setSearchQuery = useCallback((query: string) => {
    dispatch({ type: A.SET_SEARCH_QUERY, query });
  }, []);

  const setTrackFilters = useCallback((track: TrackFilters) => {
    dispatch({ type: A.SET_TRACK_FILTERS, track });
  }, []);

  const setVisualizationFilters = useCallback((visualization: VisualizationFilters) => {
    dispatch({ type: A.SET_VISUALIZATION_FILTERS, visualization });
  }, []);

  const resetFilters = useCallback(() => {
    dispatch({ type: A.RESET_FILTERS });
  }, []);

  const setInfoOpen = useCallback((open: boolean) => {
    dispatch({ type: A.SET_INFO_OPEN, open });
  }, []);

  const setResetConfirmOpen = useCallback((open: boolean) => {
    dispatch({ type: A.SET_RESET_CONFIRM_OPEN, open });
  }, []);

  const focusMode = useCallback(() => {
    if (!state.raw || !rendered) return;

    // Jump to next ready-to-learn node within the CURRENTLY FILTERED graph
    const nextId = selectNextReady(state.raw, rendered, state.learned);
    if (!nextId) return;
    dispatch({ type: A.FOCUS_MODE, selectedLeafId: nextId });
  }, [state.raw, rendered, state.learned]);

  const overviewMode = useCallback(() => {
    // GraphCanvas handles zoom; no state change needed
  }, []);

  const getNextReadyId = useCallback((): string | null => {
    if (!state.raw || !rendered) return null;
    return selectNextReady(state.raw, rendered, state.learned);
  }, [state.raw, rendered, state.learned]);

  return {
    raw: state.raw,
    rendered,
    trackGraph,
    learned: state.learned,
    selectedLeafId: state.selectedLeafId,
    selectedNode,
    panelCollapsed: state.panelCollapsed,
    activeTab: state.activeTab,
    searchQuery: state.searchQuery,
    searchMatches,
    filters: state.filters,
    filtersAreDefault,
    infoOpen: state.infoOpen,
    resetConfirmOpen: state.resetConfirmOpen,
    markLearned,
    resetProgress,
    selectLeaf,
    clearSelection,
    setPanelCollapsed,
    setActiveTab,
    setSearchQuery,
    setTrackFilters,
    setVisualizationFilters,
    resetFilters,
    setInfoOpen,
    setResetConfirmOpen,
    focusMode,
    overviewMode,
    getNextReadyId,
  };
}
