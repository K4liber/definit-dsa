import {
  LEARNED_STORAGE_KEY,
  VISIBILITY_STORAGE_KEY,
  PANEL_COLLAPSED_KEY,
  CATEGORIES_OPEN_KEY,
} from './constants';

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

export function loadIncludedFromStorage(): Set<string> | null {
  try {
    const raw = localStorage.getItem(VISIBILITY_STORAGE_KEY);
    if (!raw) return null;
    const arr = JSON.parse(raw);
    if (!Array.isArray(arr)) return null;
    return new Set<string>(arr.filter((x) => typeof x === 'string'));
  } catch {
    return null;
  }
}

export function saveIncludedToStorage(set: Set<string>): void {
  try {
    localStorage.setItem(VISIBILITY_STORAGE_KEY, JSON.stringify(Array.from(set)));
  } catch {
    // ignore
  }
}

export function clearIncludedFromStorage(): void {
  try {
    localStorage.removeItem(VISIBILITY_STORAGE_KEY);
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

export function loadOpenPrefixes(): Set<string> {
  try {
    const raw = localStorage.getItem(CATEGORIES_OPEN_KEY);
    if (!raw) return new Set();
    const arr = JSON.parse(raw);
    if (!Array.isArray(arr)) return new Set();
    return new Set<string>(arr.filter((x) => typeof x === 'string'));
  } catch {
    return new Set();
  }
}

export function saveOpenPrefixes(s: Set<string>): void {
  try {
    localStorage.setItem(CATEGORIES_OPEN_KEY, JSON.stringify(Array.from(s)));
  } catch {
    // ignore
  }
}
