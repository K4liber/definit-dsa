import type { BottomTab, Raw, DefGraph, DefNode } from '../types';
import DefinitionTab from './DefinitionTab';
import CategoriesTab from './CategoriesTab';
import ProgressTab from './ProgressTab';

type Props = {
  expanded: boolean;
  activeTab: BottomTab;
  onTabChange: (tab: BottomTab) => void;
  // Definition tab
  selectedNode: DefNode | null;
  renderedNodes: DefNode[];
  learned: Set<string>;
  onMarkLearned: (id: string) => void;
  onDepClick: (id: string) => void;
  // Categories tab
  raw: Raw | null;
  rendered: DefGraph | null;
  includedIds: Set<string> | null;
  onSelectLeaf: (id: string) => void;
  onSetIncluded: (id: string, include: boolean) => void;
  onSetIncludedMany: (ids: string[], include: boolean) => void;
};

const BottomPanel: React.FC<Props> = ({
  expanded,
  activeTab,
  onTabChange,
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
}) => {
  return (
    <div className={`bottomPanel ${expanded ? 'expanded' : ''}`}>
      <div className="bottomPanelContent">
        <div className="bottomPanelMenu" role="tablist" aria-label="Bottom panel tabs">
          <button
            className={`tabBtn ${activeTab === 'definition' ? 'active' : ''}`}
            role="tab"
            aria-selected={activeTab === 'definition'}
            onClick={() => onTabChange('definition')}
          >
            Definition
          </button>
          <button
            className={`tabBtn ${activeTab === 'categories' ? 'active' : ''}`}
            role="tab"
            aria-selected={activeTab === 'categories'}
            onClick={() => onTabChange('categories')}
          >
            Categories
          </button>
          <button
            className={`tabBtn ${activeTab === 'progress' ? 'active' : ''}`}
            role="tab"
            aria-selected={activeTab === 'progress'}
            onClick={() => onTabChange('progress')}
          >
            Progress
          </button>
        </div>

        <div
          className={`tabPage ${activeTab === 'definition' ? 'active' : ''}`}
          role="tabpanel"
        >
          <DefinitionTab
            node={selectedNode}
            renderedNodes={renderedNodes}
            learned={learned}
            onMarkLearned={onMarkLearned}
            onDepClick={onDepClick}
          />
        </div>

        <div
          className={`tabPage ${activeTab === 'categories' ? 'active' : ''}`}
          role="tabpanel"
        >
          {raw && rendered && (
            <CategoriesTab
              raw={raw}
              rendered={rendered}
              learned={learned}
              includedIds={includedIds}
              onSelectLeaf={onSelectLeaf}
              onSetIncluded={onSetIncluded}
              onSetIncludedMany={onSetIncludedMany}
            />
          )}
        </div>

        <div
          className={`tabPage ${activeTab === 'progress' ? 'active' : ''}`}
          role="tabpanel"
        >
          {raw && rendered && (
            <ProgressTab raw={raw} rendered={rendered} learned={learned} />
          )}
        </div>
      </div>
    </div>
  );
};

export default BottomPanel;
