import type { TrackFilters } from './graph';

export type { TrackFilters };

/** Visualization filters: which learning states stay visible in the graph. */
export type VisualizationFilters = {
    showLearned: boolean;
    showReady: boolean;
    showPreReady: boolean;
    showNotReady: boolean;
};

/** All filters persisted together in localStorage. */
export type PersistedFilters = {
    track: TrackFilters;
    visualization: VisualizationFilters;
};

/** Id of the default group ("Data Structures and Algorithms"). */
export const DEFAULT_GROUP_ID = 'data_structures_and_algorithms';

export const DEFAULT_TRACK_FILTERS: TrackFilters = {
    includeReferences: false,
    groupIds: [DEFAULT_GROUP_ID],
    definitionIds: [],
};

export const DEFAULT_VISUALIZATION_FILTERS: VisualizationFilters = {
    showLearned: true,
    showReady: true,
    showPreReady: true,
    showNotReady: false,
};

export const DEFAULT_FILTERS: PersistedFilters = {
    track: DEFAULT_TRACK_FILTERS,
    visualization: DEFAULT_VISUALIZATION_FILTERS,
};

export function cloneFilters(f: PersistedFilters): PersistedFilters {
    return {
        track: {
            includeReferences: f.track.includeReferences,
            groupIds: [...f.track.groupIds],
            definitionIds: [...f.track.definitionIds],
        },
        visualization: { ...f.visualization },
    };
}

export function trackEquals(a: TrackFilters, b: TrackFilters): boolean {
    return (
        a.includeReferences === b.includeReferences &&
        a.groupIds.length === b.groupIds.length &&
        a.definitionIds.length === b.definitionIds.length &&
        a.groupIds.every((id) => b.groupIds.includes(id)) &&
        a.definitionIds.every((id) => b.definitionIds.includes(id))
    );
}

export function filtersEquals(a: PersistedFilters, b: PersistedFilters): boolean {
    return trackEquals(a.track, b.track) && JSON.stringify(a.visualization) === JSON.stringify(b.visualization);
}

/** `id -> label` map for known groups plus nodes. */
export function sanitizePersistedFilters(
    persisted: unknown,
    knownGroupIds: Set<string>,
    knownNodeIds: Set<string>,
): PersistedFilters {
    const out = cloneFilters(DEFAULT_FILTERS);

    if (typeof persisted !== 'object' || persisted === null) return out;

    const p = persisted as {
        track?: {
            includeReferences?: unknown;
            groupIds?: unknown;
            definitionIds?: unknown;
        };
        visualization?: Record<string, unknown>;
    };

    if (typeof p.track?.includeReferences === 'boolean') {
        out.track.includeReferences = p.track.includeReferences;
    }

    if (Array.isArray(p.track?.groupIds)) {
        const ids = p.track.groupIds.filter(
            (x): x is string => typeof x === 'string' && knownGroupIds.has(x),
        );
        out.track.groupIds = Array.from(new Set(ids));
    }

    if (Array.isArray(p.track?.definitionIds)) {
        const ids = p.track.definitionIds.filter(
            (x): x is string => typeof x === 'string' && knownNodeIds.has(x),
        );
        out.track.definitionIds = Array.from(new Set(ids));
    }

    const v = p.visualization ?? {};
    if (typeof v.showLearned === 'boolean') out.visualization.showLearned = v.showLearned;
    if (typeof v.showReady === 'boolean') out.visualization.showReady = v.showReady;
    if (typeof v.showPreReady === 'boolean') out.visualization.showPreReady = v.showPreReady;
    if (typeof v.showNotReady === 'boolean') out.visualization.showNotReady = v.showNotReady;

    return out;
}
