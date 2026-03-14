import React, { useMemo, useState, useEffect, useRef, useCallback } from 'react';
import type { Raw, DefNode, TreeNode, LearnState } from '../types';
import { buildCategoryTree, learnStateForNode } from '../lib/graph';
import { loadOpenPrefixes, saveOpenPrefixes } from '../lib/storage';

type Match = { id: string; title: string };

type Props = {
  // Category filter
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
  showNotReady,
  showPreReady,
  showReady,
  showLearned,
  onSetShowNotReady,
  onSetShowPreReady,
  onSetShowReady,
  onSetShowLearned,
}) => {
  // --- Category tree state ---
  const [openPrefixes, setOpenPrefixes] = useState<Set<string>>(() => loadOpenPrefixes());

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
      saveOpenPrefixes(next);
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

  const leafIdsUnder = useCallback(
    (prefix: string) => {
      if (!prefix) return raw.def.nodes.map((n) => n.id);
      return raw.childrenByPrefix.get(prefix) ?? [];
    },
    [raw],
  );

  const { root, visibleNodeIds } = useMemo(
    () => buildCategoryTree(raw, renderedForTree, learned),
    [raw, renderedForTree, learned],
  );

  const stateForCat = useCallback(
    (leaf: DefNode): LearnState => {
      const base = learnStateForNode(leaf, learned);
      return base === 'not-ready' && visibleNodeIds.has(leaf.id) ? 'pre-ready' : base;
    },
    [learned, visibleNodeIds],
  );

  const renderTreeNode = useCallback(
    (node: TreeNode): React.ReactNode => {
      if (node.id === '') {
        // Root – render children only
        return node.children.map((c) => renderTreeNode(c));
      }

      const open = node.kind === 'group' ? isOpen(node.id) : true;

      if (node.kind === 'group') {
        const childLeafIds = leafIdsUnder(node.id);
        const allInc = childLeafIds.length ? childLeafIds.every(isIncluded) : true;
        const anyInc = childLeafIds.some(isIncluded);

        return (
          <div key={node.id}>
            <div
              className="treeRow hasChildren clickable"
              style={{ '--indent': Math.max(0, node.depth - 1) } as React.CSSProperties}
              onClick={(ev) => {
                const t = ev.target as HTMLElement;
                if (t.tagName === 'INPUT') return;
                toggleOpen(node.id);
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
                  onSetIncludedMany(childLeafIds, ev.target.checked);
                }}
              />
              <span className="treeLabel">{node.name}</span>
              <span className="treeMeta">
                <span>L{node.groupLevel ?? 0}</span>
              </span>
            </div>
            {open && node.children.map((c) => renderTreeNode(c))}
          </div>
        );
      }

      // Leaf
      const leaf = node.leaf!;
      const st = stateForCat(leaf);

      return (
        <div key={node.id}>
          <div
            className="treeRow clickable"
            style={{ '--indent': Math.max(0, node.depth - 1) } as React.CSSProperties}
            onClick={(ev) => {
              const t = ev.target as HTMLElement;
              if (t.tagName === 'INPUT') return;
              onSelectLeaf(leaf.id);
            }}
          >
            <span className="treeIndent" />
            <span className="treeChevron" />
            <input
              type="checkbox"
              className="treeCheckbox"
              checked={isIncluded(leaf.id)}
              onChange={(ev) => {
                onSetIncluded(leaf.id, ev.target.checked);
              }}
            />
            <span className="treeLabel">{leaf.title}</span>
            <span className="treeMeta">
              <span className={`stateDot ${st}`} />
              <span>L{leaf.level ?? 0}</span>
            </span>
          </div>
        </div>
      );
    },
    [isOpen, isIncluded, leafIdsUnder, onSelectLeaf, onSetIncluded, onSetIncludedMany, stateForCat, toggleOpen],
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
              data-testid="definition-search-input"
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
              <div className="searchMatches" role="listbox" aria-label="Definition matches" data-testid="definition-search-matches">
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
          <h4 style={{ margin: '0 0 6px 0', fontSize: 12, color: '#a9b4c0' }}>Category include/exclude</h4>
          <div className="categoriesTree" data-testid="categories-tree">{renderTreeNode(root)}</div>
        </div>
      </div>
    </div>
  );
};

export default FiltersTab;
