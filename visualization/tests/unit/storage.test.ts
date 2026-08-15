import { describe, expect, it } from 'vitest';

import {
  clearIncludedFromStorage,
  clearLearnedFromStorage,
  loadIncludedFromStorage,
  loadLearnedFromStorage,
  loadOpenFields,
  loadPanelCollapsed,
  saveIncludedToStorage,
  saveLearnedToStorage,
  saveOpenFields,
  savePanelCollapsed,
} from '../../src/lib/storage';
import {
  OPEN_FIELDS_KEY,
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

    saveIncludedToStorage(new Set(['x', 'y']));
    clearIncludedFromStorage();
    expect(loadIncludedFromStorage()).toBeNull();
  });

  it('persists panel collapsed state as a boolean flag', () => {
    savePanelCollapsed(true);
    expect(loadPanelCollapsed()).toBe(true);

    savePanelCollapsed(false);
    expect(loadPanelCollapsed()).toBe(false);
  });

  it('round-trips open field prefixes', () => {
    saveOpenFields(new Set(['mathematics', 'computer_science']));

    expect(Array.from(loadOpenFields()).sort()).toEqual([
      'computer_science',
      'mathematics',
    ]);

    localStorage.setItem(OPEN_FIELDS_KEY, '123');
    expect(Array.from(loadOpenFields())).toEqual([]);
  });
});