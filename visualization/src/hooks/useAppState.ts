import { useReducer, useCallback, useEffect, useMemo, useRef } from 'react';
import type { DefGraph, DefNode, Raw, LearnState } from '../types';
import type { BottomTab } from '../types';
import {
  buildRaw,
  renderGraph,
  recomputeIncludedSetFromReady,
  selectNextReady,
  normalizeId,
  prerequisiteClosure,
} from '../lib/graph';
import {
  loadLearnedFromStorage,
  saveLearnedToStorage,
  clearLearnedFromStorage,
  loadIncludedFromStorage,
  saveIncludedToStorage,
  clearIncludedFromStorage,
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
  includedIds: Set<string> | null;
  selectedLeafId: string | null;
  // Bottom panel state
  panelCollapsed: boolean;
  activeTab: BottomTab;
  // Search / selected definition filter
  searchQuery: string;
  searchSelectedId: string | null;
  // State filters (positive)
  showNotReady: boolean;
  showPreReady: boolean;
  showReady: boolean;
  showLearned: boolean;
  // Modal states
  infoOpen: boolean;
  resetConfirmOpen: boolean;
};

function initialReducerState(): ReducerState {
  return {
    raw: null,
    learned: loadLearnedFromStorage(),
    includedIds: loadIncludedFromStorage(),
    selectedLeafId: null,
    panelCollapsed: loadPanelCollapsed(),
    activeTab: 'definition',
    searchQuery: '',
    searchSelectedId: null,
    showNotReady: false,
    showPreReady: true,
    showReady: true,
    showLearned: true,
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
  RECOMPUTE_INCLUDED = 'RECOMPUTE_INCLUDED',
  RESET_PROGRESS = 'RESET_PROGRESS',
  SET_INCLUDED = 'SET_INCLUDED',
  SET_INCLUDED_MANY = 'SET_INCLUDED_MANY',
  SELECT_LEAF = 'SELECT_LEAF',
  CLEAR_SELECTION = 'CLEAR_SELECTION',
  SET_PANEL_COLLAPSED = 'SET_PANEL_COLLAPSED',
  SET_ACTIVE_TAB = 'SET_ACTIVE_TAB',
  SET_SEARCH_QUERY = 'SET_SEARCH_QUERY',
  SET_SEARCH_SELECTED = 'SET_SEARCH_SELECTED',
  SET_INFO_OPEN = 'SET_INFO_OPEN',
  SET_RESET_CONFIRM_OPEN = 'SET_RESET_CONFIRM_OPEN',
  FOCUS_MODE = 'FOCUS_MODE',
  SET_SHOW_NOT_READY = 'SET_SHOW_NOT_READY',
  SET_SHOW_PRE_READY = 'SET_SHOW_PRE_READY',
  SET_SHOW_READY = 'SET_SHOW_READY',
  SET_SHOW_LEARNED = 'SET_SHOW_LEARNED',
}

/* ------------------------------------------------------------------ */
/*  Actions                                                            */
/* ------------------------------------------------------------------ */

type Action =
  | { type: A.DATA_LOADED; raw: Raw }
  | { type: A.INIT_COMPLETE; selectedLeafId: string | null; includedIds: Set<string> | null; showInfo: boolean }
  | { type: A.MARK_LEARNED; id: string }
  | { type: A.AUTO_SELECT_NEXT; selectedLeafId: string | null }
  | { type: A.RECOMPUTE_INCLUDED; includedIds: Set<string> | null }
  | { type: A.RESET_PROGRESS }
  | { type: A.SET_INCLUDED; id: string; include: boolean }
  | { type: A.SET_INCLUDED_MANY; ids: string[]; include: boolean }
  | { type: A.SELECT_LEAF; id: string }
  | { type: A.CLEAR_SELECTION }
  | { type: A.SET_PANEL_COLLAPSED; collapsed: boolean }
  | { type: A.SET_ACTIVE_TAB; tab: BottomTab }
  | { type: A.SET_SEARCH_QUERY; query: string }
  | { type: A.SET_SEARCH_SELECTED; id: string | null }
  | { type: A.SET_INFO_OPEN; open: boolean }
  | { type: A.SET_RESET_CONFIRM_OPEN; open: boolean }
  | { type: A.FOCUS_MODE; selectedLeafId: string | null }
  | { type: A.SET_SHOW_NOT_READY; value: boolean }
  | { type: A.SET_SHOW_PRE_READY; value: boolean }
  | { type: A.SET_SHOW_READY; value: boolean }
  | { type: A.SET_SHOW_LEARNED; value: boolean };

/* ------------------------------------------------------------------ */
/*  Reducer                                                            */
/* ------------------------------------------------------------------ */

function reducer(state: ReducerState, action: Action): ReducerState {
  switch (action.type) {
    case A.DATA_LOADED:
      return { ...state, raw: action.raw };

    case A.INIT_COMPLETE:
      return {
        ...state,
        selectedLeafId: action.selectedLeafId,
        includedIds: action.includedIds ?? state.includedIds,
        infoOpen: action.showInfo || state.infoOpen,
        activeTab: action.selectedLeafId ? 'definition' : state.activeTab,
        panelCollapsed: action.selectedLeafId ? false : state.panelCollapsed,
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

    case A.RECOMPUTE_INCLUDED:
      if (action.includedIds) {
        saveIncludedToStorage(action.includedIds);
      } else {
        clearIncludedFromStorage();
      }
      return { ...state, includedIds: action.includedIds };

    case A.RESET_PROGRESS:
      clearLearnedFromStorage();
      saveLearnedToStorage(new Set());
      clearIncludedFromStorage();
      return {
        ...state,
        learned: new Set(),
        includedIds: null,
        selectedLeafId: null,
        resetConfirmOpen: false,
      };

    case A.SET_INCLUDED: {
      const allIds = state.raw?.def.nodes.map((n) => n.id) ?? [];
      const next = new Set(state.includedIds ?? allIds);
      if (action.include) next.add(action.id);
      else next.delete(action.id);
      saveIncludedToStorage(next);
      return { ...state, includedIds: next };
    }

    case A.SET_INCLUDED_MANY: {
      const allIds = state.raw?.def.nodes.map((n) => n.id) ?? [];
      const next = new Set(state.includedIds ?? allIds);
      for (const id of action.ids) {
        if (action.include) next.add(id);
        else next.delete(id);
      }
      saveIncludedToStorage(next);
      return { ...state, includedIds: next };
    }

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
      // Typing clears selection; selection is only set via the dropdown.
      return { ...state, searchQuery: action.query, searchSelectedId: null };

    case A.SET_SEARCH_SELECTED:
      return {
        ...state,
        searchSelectedId: action.id,
        searchQuery: action.id ?? '',
      };

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

    case A.SET_SHOW_NOT_READY:
      return { ...state, showNotReady: action.value };

    case A.SET_SHOW_PRE_READY:
      return { ...state, showPreReady: action.value };

    case A.SET_SHOW_READY:
      return { ...state, showReady: action.value };

    case A.SET_SHOW_LEARNED:
      return { ...state, showLearned: action.value };

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
  learned: Set<string>;
  includedIds: Set<string> | null;
  selectedLeafId: string | null;
  selectedNode: DefNode | null;
  panelCollapsed: boolean;
  activeTab: BottomTab;
  searchQuery: string;
  searchSelectedId: string | null;
  searchMatches: DefNode[];
  showNotReady: boolean;
  showPreReady: boolean;
  showReady: boolean;
  showLearned: boolean;
  infoOpen: boolean;
  resetConfirmOpen: boolean;
};

export type AppActions = {
  markLearned: (id: string) => void;
  resetProgress: () => void;
  setIncluded: (id: string, include: boolean) => void;
  setIncludedMany: (ids: string[], include: boolean) => void;
  selectLeaf: (id: string) => void;
  clearSelection: () => void;
  setPanelCollapsed: (collapsed: boolean) => void;
  setActiveTab: (tab: BottomTab) => void;
  setSearchQuery: (q: string) => void;
  setSearchSelectedId: (id: string | null) => void;
  setInfoOpen: (open: boolean) => void;
  setResetConfirmOpen: (open: boolean) => void;
  focusMode: () => void;
  overviewMode: () => void;
  getNextReadyId: () => string | null;
  setShowNotReady: (v: boolean) => void;
  setShowPreReady: (v: boolean) => void;
  setShowReady: (v: boolean) => void;
  setShowLearned: (v: boolean) => void;
};

/* ------------------------------------------------------------------ */
/*  Hook                                                              */
/* ------------------------------------------------------------------ */

export function useAppState(): AppState & AppActions {
  const [state, dispatch] = useReducer(reducer, undefined, initialReducerState);

  // ── Fetch data on mount ──────────────────────────────────────────
  useEffect(() => {
    fetch('./defs.json')
      .then((r) => r.json())
      .then((def: DefGraph) => {
        const raw = buildRaw(def);
        dispatch({ type: A.DATA_LOADED, raw });
      })
      .catch(console.error);
  }, []);

  // ── Derive search matches for dropdown ───────────────────────────
  const searchMatches = useMemo<DefNode[]>(() => {
    if (!state.raw) return [];
    const q = normalizeId(state.searchQuery);
    if (!q) return [];

    const matches = state.raw.def.nodes.filter((n) => {
      const id = normalizeId(n.id);
      const title = normalizeId(n.title ?? '');
      return id.includes(q) || title.includes(q);
    });

    matches.sort((a, b) => a.id.localeCompare(b.id));
    return matches.slice(0, 80);
  }, [state.raw, state.searchQuery]);

  // ── Derive filtered graph for selection ───────────────────────────
  const filteredGraphForSelection = useMemo<DefGraph | null>(() => {
    if (!state.raw) return null;

    // Base included set from category filter
    let included: Set<string>;
    if (state.includedIds) included = new Set(state.includedIds);
    else included = new Set(state.raw.def.nodes.map((n) => n.id));

    // Search selection filter overrides category filter (study subtree)
    if (state.searchSelectedId) {
      included = prerequisiteClosure(state.raw, state.searchSelectedId);
    }

    // Apply state filters
    const preGraph = renderGraph(state.raw, included);

    const preReadySet = new Set<string>();
    const byId = new Map(preGraph.nodes.map((n) => [n.id, n] as const));
    for (const e of preGraph.edges) {
      const prereq = byId.get(e.target);
      if (!prereq) continue;
      if (!state.learned.has(prereq.id)) continue;
      const dep = byId.get(e.source);
      if (!dep) continue;
      const deps = dep.deps ?? [];
      const isReady = deps.every((d) => state.learned.has(d));
      if (!state.learned.has(dep.id) && !isReady) preReadySet.add(dep.id);
    }

    const stateOf = (n: DefNode): LearnState => {
      if (state.learned.has(n.id)) return 'learned';
      const deps = n.deps ?? [];
      if (deps.every((d) => state.learned.has(d))) return 'ready';
      return preReadySet.has(n.id) ? 'pre-ready' : 'not-ready';
    };

    const keep = new Set<string>();
    for (const n of preGraph.nodes) {
      const st = stateOf(n);
      if (st === 'learned' && state.showLearned) keep.add(n.id);
      else if (st === 'ready' && state.showReady) keep.add(n.id);
      else if (st === 'pre-ready' && state.showPreReady) keep.add(n.id);
      else if (st === 'not-ready' && state.showNotReady) keep.add(n.id);
    }

    // Ensure searched node stays visible if present
    if (state.searchSelectedId) keep.add(state.searchSelectedId);

    return renderGraph(state.raw, keep);
  }, [
    state.raw,
    state.includedIds,
    state.searchSelectedId,
    state.learned,
    state.showNotReady,
    state.showPreReady,
    state.showReady,
    state.showLearned,
  ]);

  // Use the filtered graph as the rendered graph
  const rendered = filteredGraphForSelection;

  // ── Derive selected node ─────────────────────────────────────────
  const selectedNode = useMemo<DefNode | null>(() => {
    if (!rendered || !state.selectedLeafId) return null;
    return rendered.nodes.find((n) => n.id === state.selectedLeafId) ?? null;
  }, [rendered, state.selectedLeafId]);

  // ── One-time initialization after data + graph are ready ─────────
  const initDone = useRef(false);
  useEffect(() => {
    if (!state.raw || !rendered || initDone.current) return;
    initDone.current = true;

    // Bootstrap included set if nothing was stored.
    // NOTE: This is an optional "focus" filter. If the user is actively filtering
    // via Search selection, we must NOT apply the focus bootstrap; otherwise we
    // may hide prerequisites and collapse levels (e.g. level 0 on deep nodes).
    let includedIds: Set<string> | null = null;
    const shouldBootstrapFocusIncluded = state.includedIds === null && !state.searchSelectedId;
    if (shouldBootstrapFocusIncluded) {
      includedIds = recomputeIncludedSetFromReady(state.raw, state.learned);
    }

    // Determine first definition to show.
    // IMPORTANT: use the same currently-filtered graph that the UI renders,
    // so computed levels / ready set are consistent.
    const nextId = selectNextReady(state.raw, rendered, state.learned);

    dispatch({
      type: A.INIT_COMPLETE,
      selectedLeafId: nextId,
      includedIds,
      showInfo: state.learned.size === 0,
    });
  }, [state.raw, rendered, state.includedIds, state.learned, state.searchSelectedId]);

  // ── Auto-select next ready after marking learned ─────────────────────
  const pendingMarkId = useRef<string | null>(null);
  useEffect(() => {
    if (!pendingMarkId.current || !state.raw || !rendered) return;

    // Confirm the mark was applied (the id is now in the learned set)
    if (!state.learned.has(pendingMarkId.current)) return;
    pendingMarkId.current = null;

    // Do NOT recompute included set here; includedIds are a user filter.

    // Select next ready within the CURRENTLY FILTERED graph
    const nextId = selectNextReady(state.raw, rendered, state.learned);
    dispatch({ type: A.AUTO_SELECT_NEXT, selectedLeafId: nextId });
  }, [state.raw, rendered, state.learned]);

  // ── Action creators ──────────────────────────────────────────────

  const markLearned = useCallback((id: string) => {
    pendingMarkId.current = id;
    dispatch({ type: A.MARK_LEARNED, id });
  }, []);

  const resetProgress = useCallback(() => {
    dispatch({ type: A.RESET_PROGRESS });
  }, []);

  const setIncluded = useCallback((id: string, include: boolean) => {
    dispatch({ type: A.SET_INCLUDED, id, include });
  }, []);

  const setIncludedMany = useCallback((ids: string[], include: boolean) => {
    dispatch({ type: A.SET_INCLUDED_MANY, ids, include });
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

  const setSearchSelectedId = useCallback((id: string | null) => {
    dispatch({ type: A.SET_SEARCH_SELECTED, id });
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

  const setShowNotReady = useCallback((v: boolean) => {
    dispatch({ type: A.SET_SHOW_NOT_READY, value: v });
  }, []);

  const setShowPreReady = useCallback((v: boolean) => {
    dispatch({ type: A.SET_SHOW_PRE_READY, value: v });
  }, []);

  const setShowReady = useCallback((v: boolean) => {
    dispatch({ type: A.SET_SHOW_READY, value: v });
  }, []);

  const setShowLearned = useCallback((v: boolean) => {
    dispatch({ type: A.SET_SHOW_LEARNED, value: v });
  }, []);

  return {
    raw: state.raw,
    rendered,
    learned: state.learned,
    includedIds: state.includedIds,
    selectedLeafId: state.selectedLeafId,
    selectedNode,
    panelCollapsed: state.panelCollapsed,
    activeTab: state.activeTab,
    searchQuery: state.searchQuery,
    searchSelectedId: state.searchSelectedId,
    searchMatches,
    showNotReady: state.showNotReady,
    showPreReady: state.showPreReady,
    showReady: state.showReady,
    showLearned: state.showLearned,
    infoOpen: state.infoOpen,
    resetConfirmOpen: state.resetConfirmOpen,
    markLearned,
    resetProgress,
    setIncluded,
    setIncludedMany,
    selectLeaf,
    clearSelection,
    setPanelCollapsed,
    setActiveTab,
    setSearchQuery,
    setSearchSelectedId,
    setShowNotReady,
    setShowPreReady,
    setShowReady,
    setShowLearned,
    setInfoOpen,
    setResetConfirmOpen,
    focusMode,
    overviewMode,
    getNextReadyId,
  };
}
