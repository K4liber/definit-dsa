import type { BottomTab, Raw, DefGraph, DefNode } from '../types';
import DefinitionTab from './DefinitionTab';
import FiltersTab from './FiltersTab';
import ProgressTab from './ProgressTab';

type Props = {
  expanded: boolean;
  activeTab: BottomTab;
  // Definition tab
  selectedNode: DefNode | null;
  renderedNodes: DefNode[];
  learned: Set<string>;
  onMarkLearned: (id: string) => void;
  onDepClick: (id: string) => void;
  // Filters tab
  raw: Raw | null;
  rendered: DefGraph | null;
  includedIds: Set<string> | null;
  onSelectLeaf: (id: string) => void;
  onSetIncluded: (id: string, include: boolean) => void;
  onSetIncludedMany: (ids: string[], include: boolean) => void;
  searchQuery: string;
  searchSelectedId: string | null;
  searchMatches: Array<{ id: string; title: string }>;
  onSearchChange: (q: string) => void;
  onSelectMatch: (id: string | null) => void;
  showNotReady: boolean;
  showPreReady: boolean;
  showReady: boolean;
  showLearned: boolean;
  onSetShowNotReady: (v: boolean) => void;
  onSetShowPreReady: (v: boolean) => void;
  onSetShowReady: (v: boolean) => void;
  onSetShowLearned: (v: boolean) => void;
};

const BottomPanel: React.FC<Props> = ({
  expanded,
  activeTab,
  selectedNode,
  renderedNodes,
  learned,
  onMarkLearned,
  onDepClick,
  raw,
  rendered,
  includedIds,
  onSelectLeaf,
  onSetIncluded,
  onSetIncludedMany,
  searchQuery,
  searchSelectedId,
  searchMatches,
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
  return (
    <div className={`bottomPanel ${expanded ? 'expanded' : ''}`}>
      <div className="bottomPanelContent">
        {/* Removed internal tab button row; tab switching is handled by BottomMenu */}

        <div className={`tabPage ${activeTab === 'definition' ? 'active' : ''}`} role="tabpanel">
          {activeTab === 'definition' ? (
            <DefinitionTab
              node={selectedNode}
              renderedNodes={renderedNodes}
              learned={learned}
              onMarkLearned={onMarkLearned}
              onDepClick={onDepClick}
            />
          ) : null}
        </div>

        <div className={`tabPage ${activeTab === 'filters' ? 'active' : ''}`} role="tabpanel">
          {activeTab === 'filters' && raw && rendered ? (
            <FiltersTab
              raw={raw}
              renderedForTree={rendered}
              learned={learned}
              includedIds={includedIds}
              onSelectLeaf={onSelectLeaf}
              onSetIncluded={onSetIncluded}
              onSetIncludedMany={onSetIncludedMany}
              searchQuery={searchQuery}
              searchSelectedId={searchSelectedId}
              matches={searchMatches}
              onSearchChange={onSearchChange}
              onSelectMatch={onSelectMatch}
              showNotReady={showNotReady}
              showPreReady={showPreReady}
              showReady={showReady}
              showLearned={showLearned}
              onSetShowNotReady={onSetShowNotReady}
              onSetShowPreReady={onSetShowPreReady}
              onSetShowReady={onSetShowReady}
              onSetShowLearned={onSetShowLearned}
            />
          ) : null}
        </div>

        <div className={`tabPage ${activeTab === 'progress' ? 'active' : ''}`} role="tabpanel">
          {activeTab === 'progress' && raw && rendered ? (
            <ProgressTab rendered={rendered} learned={learned} />
          ) : null}
        </div>
      </div>
    </div>
  );
};

export default BottomPanel;
