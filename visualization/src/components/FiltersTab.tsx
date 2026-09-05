import React, { useMemo, useState, useEffect, useRef, useCallback } from 'react';
import type { Raw, DefNode, DefGroup } from '../types';
import { nodeSearchLabel } from '../lib/graph';
import type { TrackFilters, VisualizationFilters } from '../lib/filters';

type Props = {
  // Track filtering
  raw: Raw;
  trackFilters: TrackFilters;
  onSetTrackFilters: (track: TrackFilters) => void;

  // Visualization filtering
  visualizationFilters: VisualizationFilters;
  onSetVisualizationFilters: (visualization: VisualizationFilters) => void;

  // Filtering results: nodes currently visible on the graph
  visibleNodes: DefNode[];

  // Reset
  onResetFilters: () => void;

  // Search (definition multi-select within the track)
  searchQuery: string;
  matches: DefNode[];
  onSearchChange: (q: string) => void;

  // Filtering results: select a visible definition (same as clicking its node)
  onSelectDefinition: (id: string) => void;
};

const FiltersTab: React.FC<Props> = ({
  raw,
  trackFilters,
  onSetTrackFilters,
  visualizationFilters,
  onSetVisualizationFilters,
  visibleNodes,
  onResetFilters,
  searchQuery,
  matches,
  onSearchChange,
  onSelectDefinition,
}) => {
  // ── Groups ────────────────────────────────────────────────────────
  const groups = useMemo<DefGroup[]>(
    () => [...(raw.def.groups ?? [])].sort((a, b) => a.name.localeCompare(b.name)),
    [raw],
  );

  const selectedGroupIds = useMemo(() => new Set(trackFilters.groupIds), [trackFilters.groupIds]);

  const toggleGroup = useCallback(
    (groupId: string, checked: boolean) => {
      const next = new Set(trackFilters.groupIds);
      if (checked) next.add(groupId);
      else next.delete(groupId);
      onSetTrackFilters({ ...trackFilters, groupIds: Array.from(next).sort() });
    },
    [trackFilters, onSetTrackFilters],
  );

  // ── Definitions multi-select ──────────────────────────────────────
  const selectedDefinitionIds = useMemo(
    () => new Set(trackFilters.definitionIds),
    [trackFilters.definitionIds],
  );

  const toggleDefinition = useCallback(
    (id: string, checked: boolean) => {
      const next = new Set(trackFilters.definitionIds);
      if (checked) next.add(id);
      else next.delete(id);
      onSetTrackFilters({ ...trackFilters, definitionIds: Array.from(next).sort() });
    },
    [trackFilters, onSetTrackFilters],
  );

  // ── Search dropdown (search by id, title and aliases) ─────────────
  const [searchOpen, setSearchOpen] = useState(false);
  const searchBoxRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!searchOpen) return;
    const onDocClick = (ev: MouseEvent) => {
      if (searchBoxRef.current && !searchBoxRef.current.contains(ev.target as Node)) {
        setSearchOpen(false);
      }
    };
    document.addEventListener('mousedown', onDocClick);
    return () => document.removeEventListener('mousedown', onDocClick);
  }, [searchOpen]);

  // Number of directly selected definitions (groups + explicit ids, no references).
  const trackSize = useMemo(() => {
    const direct = new Set<string>();
    const groupsById = new Map(groups.map((g) => [g.id, g] as const));
    for (const groupId of trackFilters.groupIds) {
      for (const id of groupsById.get(groupId)?.definitions ?? []) direct.add(id);
    }
    for (const id of trackFilters.definitionIds) direct.add(id);
    return direct.size;
  }, [groups, trackFilters.groupIds, trackFilters.definitionIds]);

  return (
    <div className="panelSection">
      <h3>Filters</h3>

      <div style={{ display: 'grid', gap: 12 }}>
        {/* ── Track filtering ─────────────────────────────────────── */}
        <section aria-label="Track filtering">
          <h4 style={{ margin: '0 0 6px 0', fontSize: 12, color: '#a9b4c0' }}>
            Track ({trackSize} definitions selected)
          </h4>

          <label className="filterCheck">
            <input
              type="checkbox"
              aria-label="Include references"
              checked={trackFilters.includeReferences}
              onChange={(e) =>
                onSetTrackFilters({ ...trackFilters, includeReferences: e.target.checked })
              }
            />
            Include references
          </label>

          <h5 style={{ margin: '8px 0 4px 0', fontSize: 11, color: '#a9b4c0' }}>Groups</h5>
          {groups.map((group) => (
            <label key={group.id} className="filterCheck">
              <input
                type="checkbox"
                aria-label={`Group ${group.name}`}
                checked={selectedGroupIds.has(group.id)}
                onChange={(e) => toggleGroup(group.id, e.target.checked)}
              />
              {group.name} ({group.definitions.length})
            </label>
          ))}

          <h5 style={{ margin: '8px 0 4px 0', fontSize: 11, color: '#a9b4c0' }}>Definitions</h5>
          <div className="searchBox" ref={searchBoxRef} role="combobox" aria-expanded={searchOpen}>
            <input
              type="text"
              aria-label="Search definition"
              placeholder="Search definition by id/title/alias..."
              value={searchQuery}
              onChange={(e) => {
                onSearchChange(e.target.value);
                setSearchOpen(true);
              }}
              onFocus={() => {
                if (matches.length) setSearchOpen(true);
              }}
            />

            {searchOpen && matches.length > 0 && (
              <div className="searchMatches" role="listbox" aria-label="Definition matches">
                {matches.map((m) => {
                  const checked = selectedDefinitionIds.has(m.id);
                  return (
                    <label key={m.id} className="searchMatch">
                      <input
                        type="checkbox"
                        checked={checked}
                        onChange={(ev) => {
                          toggleDefinition(m.id, ev.target.checked);
                        }}
                      />
                      <span className="searchItemText">
                        <span className="searchItemId">{m.id}</span>
                        <span className="searchItemTitle">{nodeSearchLabel(m)}</span>
                      </span>
                    </label>
                  );
                })}
              </div>
            )}
          </div>

          {trackFilters.definitionIds.length > 0 && (
            <div className="selectedDefinitions" role="list" aria-label="Selected definitions">
              {trackFilters.definitionIds.map((id) => {
                const node = raw.byId.get(id);
                const label = node ? nodeSearchLabel(node) : id;
                return (
                  <span key={id} className="selectedDefinitionChip" role="listitem">
                    {label}
                    <button
                      type="button"
                      className="chipRemove"
                      aria-label={`Remove ${id} from track`}
                      onClick={() => toggleDefinition(id, false)}
                    >
                      ×
                    </button>
                  </span>
                );
              })}
            </div>
          )}
        </section>

        {/* ── Visualization filtering ──────────────────────────────── */}
        <section aria-label="Visualization filtering">
          <h4 style={{ margin: '0 0 6px 0', fontSize: 12, color: '#a9b4c0' }}>Visualization</h4>

          <p className="filterNote">
            These checkboxes only reduce the number of nodes shown on the graph, so you can
            focus on the most relevant definitions at the moment. They do not affect your
            progress statistics or the learning track.
          </p>

          <label className="filterCheck">
            <input
              type="checkbox"
              aria-label="Show learned definitions"
              checked={visualizationFilters.showLearned}
              onChange={(e) =>
                onSetVisualizationFilters({ ...visualizationFilters, showLearned: e.target.checked })
              }
            />
            Show learned definitions
          </label>
          <label className="filterCheck">
            <input
              type="checkbox"
              aria-label="Show ready-to-learn definitions"
              checked={visualizationFilters.showReady}
              onChange={(e) =>
                onSetVisualizationFilters({ ...visualizationFilters, showReady: e.target.checked })
              }
            />
            Show ready-to-learn definitions
          </label>
          <label className="filterCheck">
            <input
              type="checkbox"
              aria-label="Show pre-ready definitions"
              checked={visualizationFilters.showPreReady}
              onChange={(e) =>
                onSetVisualizationFilters({
                  ...visualizationFilters,
                  showPreReady: e.target.checked,
                })
              }
            />
            Show pre-ready definitions
          </label>
          <label className="filterCheck">
            <input
              type="checkbox"
              aria-label="Show not-ready definitions"
              checked={visualizationFilters.showNotReady}
              onChange={(e) =>
                onSetVisualizationFilters({
                  ...visualizationFilters,
                  showNotReady: e.target.checked,
                })
              }
            />
            Show not-ready definitions
          </label>
        </section>
        {/* ── Filtering results ────────────────────────────────────── */}
        <section aria-label="Filtering results">
          <h4 style={{ margin: '0 0 6px 0', fontSize: 12, color: '#a9b4c0' }}>
            Filtering results ({visibleNodes.length} definitions on the graph)
          </h4>

          {visibleNodes.length === 0 ? (
            <p className="filterNote">No definitions match the current filters.</p>
          ) : (
            <ul className="filterResults" role="list">
              {visibleNodes.map((n) => (
                <li key={n.id}>
                  <button
                    type="button"
                    className="filterResultItem"
                    aria-label={`Select ${n.id} on the graph`}
                    onClick={() => onSelectDefinition(n.id)}
                  >
                    <span className="filterResultLevel">L{n.level ?? 0}</span>
                    <span className="searchItemText">
                      <span className="searchItemId">{n.id}</span>
                      <span className="searchItemTitle">{nodeSearchLabel(n)}</span>
                    </span>
                  </button>
                </li>
              ))}
            </ul>
          )}
        </section>
        {/* ── Reset ────────────────────────────────────────────────── */}
        <div>
          <button type="button" className="btn" aria-label="Reset filters" onClick={onResetFilters}>
            Reset filters
          </button>
        </div>
      </div>
    </div>
  );
};

export default FiltersTab;
