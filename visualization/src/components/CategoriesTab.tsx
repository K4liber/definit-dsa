import { useState, useCallback } from 'react';
import type { Raw, DefGraph, DefNode, TreeNode, LearnState } from '../types';
import {
  buildCategoryTree,
  learnStateForNode,
} from '../lib/graph';
import { loadOpenPrefixes, saveOpenPrefixes } from '../lib/storage';

type Props = {
  raw: Raw;
  rendered: DefGraph;
  learned: Set<string>;
  includedIds: Set<string> | null;
  onSelectLeaf: (id: string) => void;
  onSetIncluded: (id: string, include: boolean) => void;
  onSetIncludedMany: (ids: string[], include: boolean) => void;
};

const CategoriesTab: React.FC<Props> = ({
  raw,
  rendered,
  learned,
  includedIds,
  onSelectLeaf,
  onSetIncluded,
  onSetIncludedMany,
}) => {
  const [openPrefixes, setOpenPrefixes] = useState<Set<string>>(() => loadOpenPrefixes());

  const isOpen = useCallback(
    (prefix: string) => {
      if (!prefix) return true;
      // We store "collapsed" prefixes. Open by default.
      return !openPrefixes.has(prefix);
    },
    [openPrefixes],
  );

  const toggleOpen = useCallback(
    (prefix: string) => {
      if (!prefix) return;
      setOpenPrefixes((prev) => {
        const next = new Set(prev);
        if (next.has(prefix)) next.delete(prefix);
        else next.add(prefix);
        saveOpenPrefixes(next);
        return next;
      });
    },
    [],
  );

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

  const { root, visibleNodeIds } = buildCategoryTree(raw, rendered, learned);

  const stateForCat = (leaf: DefNode): LearnState => {
    const base = learnStateForNode(leaf, learned);
    return base === 'off' && visibleNodeIds.has(leaf.id) ? 'visible' : base;
  };

  const renderNode = (node: TreeNode): React.ReactNode => {
    if (node.id === '') {
      // Root – render children only
      return node.children.map((c) => renderNode(c));
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
          {open && node.children.map((c) => renderNode(c))}
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
  };

  return (
    <div className="panelSection">
      <h3>Categories</h3>
      <div className="categoriesTree">{renderNode(root)}</div>
    </div>
  );
};

export default CategoriesTab;
