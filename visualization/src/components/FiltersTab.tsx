import React, { useMemo, useState, useEffect, useRef, useCallback } from 'react';
import type { Raw, DefNode, FieldGroup, LearnState } from '../types';
import { buildFieldGroups, learnStateForNode } from '../lib/graph';
import { loadOpenFields, saveOpenFields } from '../lib/storage';

type Match = { id: string; title: string };

type Props = {
  // Definition include/exclude filter
  raw: Raw;
  renderedForTree: import('../types').DefGraph; // filtered graph (after all filters) to compute visible states
  learned: Set<string>;
  includedIds: Set<string> | null;
  onSelectLeaf: (id: string) => void;
  onSetIncluded: (id: string, include: boolean) => void;
  onSetIncludedMany: (ids: string[], include: boolean) => void;

  // Search / selected definition filter
  searchQuery: string;
  searchSelectedId: string | null;
  matches: Match[];
  onSearchChange: (q: string) => void;
  onSelectMatch: (id: string | null) => void;
  includeDescendants: boolean;
  onSetIncludeDescendants: (v: boolean) => void;

  // Node state filters
  showNotReady: boolean;
  showPreReady: boolean;
  showReady: boolean;
  showLearned: boolean;
  onSetShowNotReady: (v: boolean) => void;
  onSetShowPreReady: (v: boolean) => void;
  onSetShowReady: (v: boolean) => void;
  onSetShowLearned: (v: boolean) => void;
};

const FiltersTab: React.FC<Props> = ({
  raw,
  renderedForTree,
  learned,
  includedIds,
  onSelectLeaf,
  onSetIncluded,
  onSetIncludedMany,
  searchQuery,
  searchSelectedId,
  matches,
  onSearchChange,
  onSelectMatch,
  includeDescendants,
  onSetIncludeDescendants,
  showNotReady,
  showPreReady,
  showReady,
  showLearned,
  onSetShowNotReady,
  onSetShowPreReady,
  onSetShowReady,
  onSetShowLearned,
}) => {
  // --- Definition tree state (grouped by field) ---
  const [openPrefixes, setOpenPrefixes] = useState<Set<string>>(() => loadOpenFields());

  const isOpen = useCallback(
    (prefix: string) => {
      if (!prefix) return true;
      // We store "collapsed" prefixes. Open by default.
      return !openPrefixes.has(prefix);
    },
    [openPrefixes],
  );

  const toggleOpen = useCallback((prefix: string) => {
    if (!prefix) return;
    setOpenPrefixes((prev) => {
      const next = new Set(prev);
      if (next.has(prefix)) next.delete(prefix);
      else next.add(prefix);
      saveOpenFields(next);
      return next;
    });
  }, []);

  const isIncluded = useCallback(
    (id: string) => {
      if (!includedIds) return true;
      return includedIds.has(id);
    },
    [includedIds],
  );

  const { groups, visibleNodeIds } = useMemo(
    () => buildFieldGroups(raw, renderedForTree, learned),
    [raw, renderedForTree, learned],
  );

  const stateForCat = useCallback(
    (leaf: DefNode): LearnState => {
      const base = learnStateForNode(leaf, learned);
      return base === 'not-ready' && visibleNodeIds.has(leaf.id) ? 'pre-ready' : base;
    },
    [learned, visibleNodeIds],
  );

  const renderGroup = useCallback(
    (group: FieldGroup): React.ReactNode => {
      const open = isOpen(group.field);
      const definitionIds = group.definitions.map((d) => d.id);
      const allInc = definitionIds.length ? definitionIds.every(isIncluded) : true;
      const anyInc = definitionIds.some(isIncluded);

      return (
        <div key={group.field}>
          <div
            className="treeRow hasChildren clickable"
            onClick={(ev) => {
              const t = ev.target as HTMLElement;
              if (t.tagName === 'INPUT') return;
              toggleOpen(group.field);
            }}
          >
            <span className="treeIndent" />
            <span className={`treeChevron ${open ? 'open' : ''}`}>▶</span>
            <input
              type="checkbox"
              className="treeCheckbox"
              checked={allInc}
              ref={(el) => {
                if (el) el.indeterminate = anyInc && !allInc;
              }}
              onChange={(ev) => {
                onSetIncludedMany(definitionIds, ev.target.checked);
              }}
            />
            <span className="treeLabel">{group.field}</span>
            <span className="treeMeta">
              <span>{group.definitions.length}</span>
            </span>
          </div>
          {open &&
            group.definitions.map((def) => {
              const st = stateForCat(def);

              return (
                <div
                  key={def.id}
                  className="treeRow clickable"
                  style={{ '--indent': 1 } as React.CSSProperties}
                  onClick={(ev) => {
                    const t = ev.target as HTMLElement;
                    if (t.tagName === 'INPUT') return;
                    onSelectLeaf(def.id);
                  }}
                >
                  <span className="treeIndent" />
                  <span className="treeChevron" />
                  <input
                    type="checkbox"
                    className="treeCheckbox"
                    checked={isIncluded(def.id)}
                    onChange={(ev) => {
                      onSetIncluded(def.id, ev.target.checked);
                    }}
                  />
                  <span className="treeLabel">{def.title}</span>
                  <span className="treeMeta">
                    <span className={`stateDot ${st}`} />
                    <span>L{def.level ?? 0}</span>
                  </span>
                </div>
              );
            })}
        </div>
      );
    },
    [isOpen, isIncluded, onSelectLeaf, onSetIncluded, onSetIncludedMany, stateForCat, toggleOpen],
  );

  // Hide search results list after selecting an item; reopen on typing/focus.
  const [searchOpen, setSearchOpen] = useState(false);
  const lastSelectedRef = useRef<string | null>(null);

  useEffect(() => {
    if (searchSelectedId && searchSelectedId !== lastSelectedRef.current) {
      lastSelectedRef.current = searchSelectedId;
      setSearchOpen(false);
    }
    if (!searchSelectedId) {
      lastSelectedRef.current = null;
    }
  }, [searchSelectedId]);

  return (
    <div className="panelSection">
      <h3>Filters</h3>

      <div style={{ display: 'grid', gap: 12 }}>
        <div>
          <h4 style={{ margin: '0 0 6px 0', fontSize: 12, color: '#a9b4c0' }}>Selected definition</h4>
          <div className="searchBox" role="combobox" aria-expanded={matches.length > 0}>
            <input
              type="text"
              aria-label="Search definition"
              placeholder="Search node by id/title..."
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
                  const checked = m.id === searchSelectedId;
                  return (
                    <label key={m.id} className="searchMatch">
                      <input
                        type="checkbox"
                        checked={checked}
                        onChange={(ev) => {
                          onSelectMatch(ev.target.checked ? m.id : null);
                          setSearchOpen(false);
                        }}
                      />
                      <span className="searchItemText">
                        <span className="searchItemId">{m.id}</span>
                        <span className="searchItemTitle">{m.title}</span>
                      </span>
                    </label>
                  );
                })}
              </div>
            )}
          </div>
          <label style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 8 }}>
            <input
              type="checkbox"
              checked={includeDescendants}
              onChange={(e) => onSetIncludeDescendants(e.target.checked)}
            />
            Include all descendants
          </label>
        </div>

        <div>
          <h4 style={{ margin: '0 0 6px 0', fontSize: 12, color: '#a9b4c0' }}>Node states</h4>

          <label style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <input
              type="checkbox"
              checked={showLearned}
              onChange={(e) => onSetShowLearned(e.target.checked)}
            />
            Show learned nodes
          </label>
          <label style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <input
              type="checkbox"
              checked={showReady}
              onChange={(e) => onSetShowReady(e.target.checked)}
            />
            Show ready-to-learn nodes
          </label>
          <label style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <input
              type="checkbox"
              checked={showPreReady}
              onChange={(e) => onSetShowPreReady(e.target.checked)}
            />
            Show pre-ready nodes
          </label>
          <label style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <input
              type="checkbox"
              checked={showNotReady}
              onChange={(e) => onSetShowNotReady(e.target.checked)}
            />
            Show not-ready nodes
          </label>
        </div>

        <div>
          <h4 style={{ margin: '0 0 6px 0', fontSize: 12, color: '#a9b4c0' }}>Definitions include/exclude</h4>
          <div className="categoriesTree" role="region" aria-label="Definitions include/exclude">{groups.map(renderGroup)}</div>
        </div>
      </div>
    </div>
  );
};

export default FiltersTab;
