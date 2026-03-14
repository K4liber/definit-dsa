import { describe, expect, it } from 'vitest';

import {
  clearIncludedFromStorage,
  clearLearnedFromStorage,
  loadIncludedFromStorage,
  loadLearnedFromStorage,
  loadOpenPrefixes,
  loadPanelCollapsed,
  saveIncludedToStorage,
  saveLearnedToStorage,
  saveOpenPrefixes,
  savePanelCollapsed,
} from '../../src/lib/storage';
import {
  CATEGORIES_OPEN_KEY,
  LEARNED_STORAGE_KEY,
  VISIBILITY_STORAGE_KEY,
} from '../../src/lib/constants';

describe('storage helpers', () => {
  it('round-trips learned ids through localStorage', () => {
    saveLearnedToStorage(new Set(['a', 'b']));

    expect(Array.from(loadLearnedFromStorage()).sort()).toEqual(['a', 'b']);

    clearLearnedFromStorage();
    expect(Array.from(loadLearnedFromStorage())).toEqual([]);
  });

  it('returns empty learned state for malformed payloads', () => {
    localStorage.setItem(LEARNED_STORAGE_KEY, '{bad json');

    expect(Array.from(loadLearnedFromStorage())).toEqual([]);
  });

  it('round-trips included ids and treats malformed payloads as null', () => {
    saveIncludedToStorage(new Set(['x', 'y']));
    expect(Array.from(loadIncludedFromStorage() ?? []).sort()).toEqual(['x', 'y']);

    localStorage.setItem(VISIBILITY_STORAGE_KEY, '"nope"');
    expect(loadIncludedFromStorage()).toBeNull();

    clearIncludedFromStorage();
    expect(loadIncludedFromStorage()).toBeNull();
  });

  it('persists panel collapsed state as a boolean flag', () => {
    savePanelCollapsed(true);
    expect(loadPanelCollapsed()).toBe(true);

    savePanelCollapsed(false);
    expect(loadPanelCollapsed()).toBe(false);
  });

  it('round-trips open category prefixes', () => {
    saveOpenPrefixes(new Set(['mathematics', 'computer_science/algorithms']));

    expect(Array.from(loadOpenPrefixes()).sort()).toEqual([
      'computer_science/algorithms',
      'mathematics',
    ]);

    localStorage.setItem(CATEGORIES_OPEN_KEY, '123');
    expect(Array.from(loadOpenPrefixes())).toEqual([]);
  });
});