import {
  LEARNED_STORAGE_KEY,
  FILTERS_STORAGE_KEY,
  PANEL_COLLAPSED_KEY,
  OPEN_FIELDS_KEY,
} from './constants';
import {
  DEFAULT_FILTERS,
  cloneFilters,
  sanitizePersistedFilters,
  type PersistedFilters,
} from './filters';

export function loadLearnedFromStorage(): Set<string> {
  try {
    const raw = localStorage.getItem(LEARNED_STORAGE_KEY);
    if (!raw) return new Set();
    const arr = JSON.parse(raw);
    if (!Array.isArray(arr)) return new Set();
    return new Set<string>(arr.filter((x) => typeof x === 'string'));
  } catch {
    return new Set();
  }
}

export function saveLearnedToStorage(learned: Set<string>): void {
  try {
    localStorage.setItem(LEARNED_STORAGE_KEY, JSON.stringify(Array.from(learned)));
  } catch {
    // ignore
  }
}

export function clearLearnedFromStorage(): void {
  try {
    localStorage.removeItem(LEARNED_STORAGE_KEY);
  } catch {
    // ignore
  }
}

export function loadFiltersFromStorage(
  knownGroupIds: Set<string>,
  knownNodeIds: Set<string>,
): PersistedFilters {
  try {
    const raw = localStorage.getItem(FILTERS_STORAGE_KEY);
    if (!raw) return cloneFilters(DEFAULT_FILTERS);
    return sanitizePersistedFilters(JSON.parse(raw), knownGroupIds, knownNodeIds);
  } catch {
    return cloneFilters(DEFAULT_FILTERS);
  }
}

export function saveFiltersToStorage(filters: PersistedFilters): void {
  try {
    localStorage.setItem(FILTERS_STORAGE_KEY, JSON.stringify(filters));
  } catch {
    // ignore
  }
}

export function clearFiltersFromStorage(): void {
  try {
    localStorage.removeItem(FILTERS_STORAGE_KEY);
  } catch {
    // ignore
  }
}

export function loadPanelCollapsed(): boolean {
  try {
    return localStorage.getItem(PANEL_COLLAPSED_KEY) === '1';
  } catch {
    return false;
  }
}

export function savePanelCollapsed(collapsed: boolean): void {
  try {
    localStorage.setItem(PANEL_COLLAPSED_KEY, collapsed ? '1' : '0');
  } catch {
    // ignore
  }
}

export function loadOpenFields(): Set<string> {
  try {
    const raw = localStorage.getItem(OPEN_FIELDS_KEY);
    if (!raw) return new Set();
    const arr = JSON.parse(raw);
    if (!Array.isArray(arr)) return new Set();
    return new Set<string>(arr.filter((x) => typeof x === 'string'));
  } catch {
    return new Set();
  }
}

export function saveOpenFields(s: Set<string>): void {
  try {
    localStorage.setItem(OPEN_FIELDS_KEY, JSON.stringify(Array.from(s)));
  } catch {
    // ignore
  }
}
