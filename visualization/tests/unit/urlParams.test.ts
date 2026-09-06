import { describe, expect, it } from 'vitest';

import { DEFAULT_FILTERS, cloneFilters, type PersistedFilters } from '../../src/lib/filters';
import {
    URL_KEYS,
    filtersFromSearchParams,
    filtersToSearchParams,
} from '../../src/lib/urlParams';

function withVisualization(
    partial: Partial<PersistedFilters['visualization']>,
): PersistedFilters {
    return {
        ...cloneFilters(DEFAULT_FILTERS),
        visualization: { ...DEFAULT_FILTERS.visualization, ...partial },
    };
}

describe('filtersToSearchParams', () => {
    it('produces an empty query for the default filters', () => {
        expect(filtersToSearchParams(cloneFilters(DEFAULT_FILTERS)).toString()).toBe('');
    });

    it('omits values equal to the defaults', () => {
        // showLearned: true is the default → absent from the query.
        const params = filtersToSearchParams(withVisualization({ showLearned: true }));
        expect(params.has(URL_KEYS.showLearned)).toBe(false);
    });

    it('encodes every non-default option', () => {
        const filters: PersistedFilters = {
            track: {
                includeReferences: true,
                groupIds: [],
                definitionIds: ['mathematics/fibonacci', 'computer_science/array'],
            },
            visualization: {
                showLearned: false,
                showReady: false,
                showPreReady: false,
                showNotReady: true,
            },
        };

        const params = filtersToSearchParams(filters);
        expect(params.get(URL_KEYS.includeReferences)).toBe('1');
        expect(params.get(URL_KEYS.groups)).toBe('');
        expect(params.get(URL_KEYS.definitions)).toBe('mathematics/fibonacci,computer_science/array');
        expect(params.get(URL_KEYS.showLearned)).toBe('0');
        expect(params.get(URL_KEYS.showReady)).toBe('0');
        expect(params.get(URL_KEYS.showPreReady)).toBe('0');
        expect(params.get(URL_KEYS.showNotReady)).toBe('1');
    });
});

describe('filtersFromSearchParams', () => {
    it('returns defaults and present=false for an empty query', () => {
        const { filters, present } = filtersFromSearchParams(new URLSearchParams());
        expect(present).toBe(false);
        expect(filters).toEqual(cloneFilters(DEFAULT_FILTERS));
    });

    it('returns defaults for unknown query keys', () => {
        const { filters, present } = filtersFromSearchParams(new URLSearchParams('foo=1'));
        expect(present).toBe(false);
        expect(filters).toEqual(cloneFilters(DEFAULT_FILTERS));
    });

    it('accepts 1/0 and true/false boolean spellings', () => {
        const query = `?${URL_KEYS.includeReferences}=true&${URL_KEYS.showNotReady}=1`;
        const { filters, present } = filtersFromSearchParams(new URLSearchParams(query));
        expect(present).toBe(true);
        expect(filters.track.includeReferences).toBe(true);
        expect(filters.visualization.showNotReady).toBe(true);
    });

    it('treats invalid booleans as absent (defaults win)', () => {
        const query = `?${URL_KEYS.showLearned}=maybe`;
        const { filters, present } = filtersFromSearchParams(new URLSearchParams(query));
        expect(present).toBe(true);
        expect(filters.visualization.showLearned).toBe(DEFAULT_FILTERS.visualization.showLearned);
    });

    it('parses comma-separated id lists and deduplicates them', () => {
        const query = `?${URL_KEYS.groups}=a,b,a&${URL_KEYS.definitions}=mathematics/fibonacci`;
        const { filters } = filtersFromSearchParams(new URLSearchParams(query));
        expect(filters.track.groupIds).toEqual(['a', 'b']);
        expect(filters.track.definitionIds).toEqual(['mathematics/fibonacci']);
    });

    it('parses an explicit empty id list as empty (not as the default)', () => {
        const query = `?${URL_KEYS.groups}=`;
        const { filters } = filtersFromSearchParams(new URLSearchParams(query));
        expect(filters.track.groupIds).toEqual([]);
    });

    it('round-trips non-default filters through encode → decode', () => {
        const filters: PersistedFilters = {
            track: {
                includeReferences: false,
                groupIds: ['data_structures_and_algorithms', 'mathematics'],
                definitionIds: ['computer_science/array'],
            },
            visualization: { ...DEFAULT_FILTERS.visualization, showNotReady: true },
        };

        const encoded = filtersToSearchParams(filters);
        const { filters: decoded, present } = filtersFromSearchParams(encoded);
        expect(present).toBe(true);
        expect(decoded).toEqual(filters);
    });
});
