import {
    DEFAULT_FILTERS,
    cloneFilters,
    type PersistedFilters,
} from './filters';

/**
 * URL query-string encoding of the filter state.
 *
 * Only values that differ from the defaults are written, so a default view
 * has a clean URL and shared links stay short. An absent parameter always
 * means "use the default value".
 */

/** Query-string keys; short but readable since they are user-visible. */
export const URL_KEYS = {
    includeReferences: 'ref',
    groups: 'groups',
    definitions: 'defs',
    showLearned: 'learned',
    showReady: 'ready',
    showPreReady: 'preready',
    showNotReady: 'notready',
} as const;

/** Serialize filters into query params, omitting values equal to defaults. */
export function filtersToSearchParams(filters: PersistedFilters): URLSearchParams {
    const params = new URLSearchParams();
    const defaults = DEFAULT_FILTERS;

    if (filters.track.includeReferences !== defaults.track.includeReferences) {
        params.set(URL_KEYS.includeReferences, encodeBool(filters.track.includeReferences));
    }

    if (!idListsEqual(filters.track.groupIds, defaults.track.groupIds)) {
        params.set(URL_KEYS.groups, filters.track.groupIds.join(','));
    }

    if (!idListsEqual(filters.track.definitionIds, defaults.track.definitionIds)) {
        params.set(URL_KEYS.definitions, filters.track.definitionIds.join(','));
    }

    if (filters.visualization.showLearned !== defaults.visualization.showLearned) {
        params.set(URL_KEYS.showLearned, encodeBool(filters.visualization.showLearned));
    }
    if (filters.visualization.showReady !== defaults.visualization.showReady) {
        params.set(URL_KEYS.showReady, encodeBool(filters.visualization.showReady));
    }
    if (filters.visualization.showPreReady !== defaults.visualization.showPreReady) {
        params.set(URL_KEYS.showPreReady, encodeBool(filters.visualization.showPreReady));
    }
    if (filters.visualization.showNotReady !== defaults.visualization.showNotReady) {
        params.set(URL_KEYS.showNotReady, encodeBool(filters.visualization.showNotReady));
    }

    return params;
}

/**
 * Parse filters from query params; absent or invalid values fall back to the
 * defaults. `present` tells whether the URL contained any filter parameter at
 * all (used to decide URL-over-storage precedence on load).
 */
export function filtersFromSearchParams(params: URLSearchParams): {
    filters: PersistedFilters;
    present: boolean;
} {
    const out = cloneFilters(DEFAULT_FILTERS);

    const includeReferences = decodeBool(params.get(URL_KEYS.includeReferences));
    if (includeReferences !== undefined) out.track.includeReferences = includeReferences;

    const groupIds = decodeIds(params.get(URL_KEYS.groups));
    if (groupIds !== undefined) out.track.groupIds = groupIds;

    const definitionIds = decodeIds(params.get(URL_KEYS.definitions));
    if (definitionIds !== undefined) out.track.definitionIds = definitionIds;

    const showLearned = decodeBool(params.get(URL_KEYS.showLearned));
    if (showLearned !== undefined) out.visualization.showLearned = showLearned;

    const showReady = decodeBool(params.get(URL_KEYS.showReady));
    if (showReady !== undefined) out.visualization.showReady = showReady;

    const showPreReady = decodeBool(params.get(URL_KEYS.showPreReady));
    if (showPreReady !== undefined) out.visualization.showPreReady = showPreReady;

    const showNotReady = decodeBool(params.get(URL_KEYS.showNotReady));
    if (showNotReady !== undefined) out.visualization.showNotReady = showNotReady;

    const present = Object.values(URL_KEYS).some((key) => params.has(key));
    return { filters: out, present };
}

function encodeBool(v: boolean): string {
    return v ? '1' : '0';
}

/** '1'/'true' → true, '0'/'false' → false, absent/invalid → undefined. */
function decodeBool(raw: string | null): boolean | undefined {
    if (raw === null) return undefined;
    const v = raw.trim().toLowerCase();
    if (v === '1' || v === 'true') return true;
    if (v === '0' || v === 'false') return false;
    return undefined;
}

/** Comma-separated ids → deduplicated list; absent → undefined; empty → []. */
function decodeIds(raw: string | null): string[] | undefined {
    if (raw === null) return undefined;
    const ids = raw
        .split(',')
        .map((s) => s.trim())
        .filter((s) => s.length > 0);
    return Array.from(new Set(ids));
}

/** Order-insensitive list equality. */
function idListsEqual(a: string[], b: string[]): boolean {
    if (a.length !== b.length) return false;
    const sb = new Set(b);
    return a.every((x) => sb.has(x));
}
