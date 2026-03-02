import { useReducer, useCallback, useEffect, useMemo, useRef } from 'react';
import type { DefGraph, DefNode, Raw } from '../types';
import type { BottomTab } from '../types';
import {
  buildRaw,
  renderGraph,
  recomputeIncludedSetFromReady,
  selectNextReady,
  computeLevels,
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
/*  State shape                                                        */
/* ------------------------------------------------------------------ */

type State = {
  raw: Raw | null;
  learned: Set<string>;
  includedIds: Set<string> | null;
  selectedLeafId: string | null;
  panelCollapsed: boolean;
  activeTab: BottomTab;
  searchQuery: string;
  infoOpen: boolean;
  resetConfirmOpen: boolean;
};

function initialState(): State {
  return {
    raw: null,
    learned: loadLearnedFromStorage(),
    includedIds: loadIncludedFromStorage(),
    selectedLeafId: null,
    panelCollapsed: loadPanelCollapsed(),
    activeTab: 'definition',
    searchQuery: '',
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
  SET_INFO_OPEN = 'SET_INFO_OPEN',
  SET_RESET_CONFIRM_OPEN = 'SET_RESET_CONFIRM_OPEN',
  FOCUS_MODE = 'FOCUS_MODE',
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
  | { type: A.SET_INFO_OPEN; open: boolean }
  | { type: A.SET_RESET_CONFIRM_OPEN; open: boolean }
  | { type: A.FOCUS_MODE; includedIds: Set<string> | null };

/* ------------------------------------------------------------------ */
/*  Reducer                                                            */
/* ------------------------------------------------------------------ */

function reducer(state: State, action: Action): State {
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
      return { ...state, searchQuery: action.query };

    case A.SET_INFO_OPEN:
      return { ...state, infoOpen: action.open };

    case A.SET_RESET_CONFIRM_OPEN:
      return { ...state, resetConfirmOpen: action.open };

    case A.FOCUS_MODE:
      if (action.includedIds) {
        saveIncludedToStorage(action.includedIds);
      } else {
        clearIncludedFromStorage();
      }
      return {
        ...state,
        selectedLeafId: null,
        includedIds: action.includedIds,
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
  learned: Set<string>;
  includedIds: Set<string> | null;
  selectedLeafId: string | null;
  selectedNode: DefNode | null;
  panelCollapsed: boolean;
  activeTab: BottomTab;
  searchQuery: string;
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
  setInfoOpen: (open: boolean) => void;
  setResetConfirmOpen: (open: boolean) => void;
  focusMode: () => void;
  overviewMode: () => void;
  getNextReadyId: () => string | null;
};

/* ------------------------------------------------------------------ */
/*  Hook                                                               */
/* ------------------------------------------------------------------ */

export function useAppState(): AppState & AppActions {
  const [state, dispatch] = useReducer(reducer, undefined, initialState);

  // ── Fetch data on mount ──────────────────────────────────────────
  useEffect(() => {
    fetch('./defs.json')
      .then((r) => r.json())
      .then((def: DefGraph) => {
        const raw = buildRaw(def);
        computeLevels(raw.def.nodes);
        dispatch({ type: A.DATA_LOADED, raw });
      })
      .catch(console.error);
  }, []);

  // ── Derive rendered graph (pure computation, no side-effects) ────
  const rendered = useMemo<DefGraph | null>(() => {
    if (!state.raw) return null;
    return renderGraph(state.raw, state.includedIds);
  }, [state.raw, state.includedIds, state.learned]);

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

    // Bootstrap included set if nothing was stored
    let includedIds: Set<string> | null = null;
    if (state.includedIds === null) {
      includedIds = recomputeIncludedSetFromReady(state.raw, state.learned);
    }

    // Determine first definition to show
    const graphForSelection = includedIds
      ? renderGraph(state.raw, includedIds)
      : rendered;
    const nextId = selectNextReady(state.raw, graphForSelection, state.learned);

    dispatch({
      type: A.INIT_COMPLETE,
      selectedLeafId: nextId,
      includedIds,
      showInfo: state.learned.size === 0,
    });
  }, [state.raw, rendered, state.includedIds, state.learned]);

  // ── Auto-select next ready after marking learned ─────────────────
  const pendingMarkId = useRef<string | null>(null);
  useEffect(() => {
    if (!pendingMarkId.current || !state.raw || !rendered) return;

    // Confirm the mark was applied (the id is now in the learned set)
    if (!state.learned.has(pendingMarkId.current)) return;
    pendingMarkId.current = null;

    // Recompute included set for the new learned state
    const newIncluded = recomputeIncludedSetFromReady(state.raw, state.learned);
    dispatch({ type: A.RECOMPUTE_INCLUDED, includedIds: newIncluded });

    // Select next ready (use fresh graph with new included set)
    const graphForSelection = newIncluded
      ? renderGraph(state.raw, newIncluded)
      : rendered;
    const nextId = selectNextReady(state.raw, graphForSelection, state.learned);
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

  const setInfoOpen = useCallback((open: boolean) => {
    dispatch({ type: A.SET_INFO_OPEN, open });
  }, []);

  const setResetConfirmOpen = useCallback((open: boolean) => {
    dispatch({ type: A.SET_RESET_CONFIRM_OPEN, open });
  }, []);

  const focusMode = useCallback(() => {
    if (!state.raw) return;
    const newIncluded = recomputeIncludedSetFromReady(state.raw, state.learned);
    dispatch({ type: A.FOCUS_MODE, includedIds: newIncluded });
  }, [state.raw, state.learned]);

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
    learned: state.learned,
    includedIds: state.includedIds,
    selectedLeafId: state.selectedLeafId,
    selectedNode,
    panelCollapsed: state.panelCollapsed,
    activeTab: state.activeTab,
    searchQuery: state.searchQuery,
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
    setInfoOpen,
    setResetConfirmOpen,
    focusMode,
    overviewMode,
    getNextReadyId,
  };
}
