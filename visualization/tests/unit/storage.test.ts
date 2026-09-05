import { describe, expect, it } from 'vitest';

import {
  clearFiltersFromStorage,
  clearLearnedFromStorage,
  loadFiltersFromStorage,
  loadLearnedFromStorage,
  loadOpenFields,
  loadPanelCollapsed,
  saveFiltersToStorage,
  saveLearnedToStorage,
  saveOpenFields,
  savePanelCollapsed,
} from '../../src/lib/storage';
import {
  OPEN_FIELDS_KEY,
  LEARNED_STORAGE_KEY,
  FILTERS_STORAGE_KEY,
} from '../../src/lib/constants';
import { DEFAULT_FILTERS, cloneFilters } from '../../src/lib/filters';

const KNOWN_GROUPS = new Set(['data_structures_and_algorithms', 'extra_group']);
const KNOWN_NODES = new Set(['mathematics/fibonacci', 'computer_science/array']);

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

  it('round-trips filters and sanitizes unknown ids from malformed payloads', () => {
    const filters = cloneFilters(DEFAULT_FILTERS);
    filters.track.groupIds = ['data_structures_and_algorithms'];
    filters.track.definitionIds = ['mathematics/fibonacci'];
    filters.visualization.showNotReady = true;

    saveFiltersToStorage(filters);
    expect(loadFiltersFromStorage(KNOWN_GROUPS, KNOWN_NODES)).toEqual(filters);

    // Unknown group/definition ids are dropped, unknown flags ignored.
    localStorage.setItem(
      FILTERS_STORAGE_KEY,
      JSON.stringify({
        track: {
          includeReferences: 'nope',
          groupIds: ['extra_group', 'ghost_group'],
          definitionIds: ['computer_science/array', 'ghost/id'],
        },
        visualization: { showLearned: false, somethingElse: 1 },
      }),
    );

    expect(loadFiltersFromStorage(KNOWN_GROUPS, KNOWN_NODES)).toEqual({
      track: {
        includeReferences: false,
        groupIds: ['extra_group'],
        definitionIds: ['computer_science/array'],
      },
      visualization: {
        showLearned: false,
        showReady: true,
        showPreReady: true,
        showNotReady: false,
      },
    });

    localStorage.setItem(FILTERS_STORAGE_KEY, '"nope"');
    expect(loadFiltersFromStorage(KNOWN_GROUPS, KNOWN_NODES)).toEqual(DEFAULT_FILTERS);

    clearFiltersFromStorage();
    expect(loadFiltersFromStorage(KNOWN_GROUPS, KNOWN_NODES)).toEqual(DEFAULT_FILTERS);
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