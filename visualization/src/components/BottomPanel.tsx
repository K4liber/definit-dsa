import type { BottomTab, Raw, DefGraph, DefNode } from '../types';
import type { TrackFilters, VisualizationFilters } from '../lib/filters';
import DefinitionTab from './DefinitionTab';
import FiltersTab from './FiltersTab';
import ProgressTab from './ProgressTab';

/** Visible nodes sorted by definition level (low-level first), then id. */
function sortVisibleNodes(nodes: DefNode[]): DefNode[] {
  return [...nodes].sort((a, b) => (a.level ?? 0) - (b.level ?? 0) || a.id.localeCompare(b.id));
}

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
  trackGraph: DefGraph | null;
  trackFilters: TrackFilters;
  visualizationFilters: VisualizationFilters;
  onSetTrackFilters: (track: TrackFilters) => void;
  onSetVisualizationFilters: (visualization: VisualizationFilters) => void;
  onResetFilters: () => void;
  searchQuery: string;
  searchMatches: DefNode[];
  onSearchChange: (q: string) => void;
  onSelectDefinition: (id: string) => void;
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
  trackGraph,
  trackFilters,
  visualizationFilters,
  onSetTrackFilters,
  onSetVisualizationFilters,
  onResetFilters,
  searchQuery,
  searchMatches,
  onSearchChange,
  onSelectDefinition,
}) => {
  return (
    <div
      className={`bottomPanel ${expanded ? 'expanded' : ''}`}
      role="region"
      aria-label="Bottom panel"
      aria-hidden={expanded ? 'false' : 'true'}
    >
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
              trackFilters={trackFilters}
              onSetTrackFilters={onSetTrackFilters}
              visualizationFilters={visualizationFilters}
              onSetVisualizationFilters={onSetVisualizationFilters}
              visibleNodes={sortVisibleNodes(rendered?.nodes ?? [])}
              onResetFilters={onResetFilters}
              searchQuery={searchQuery}
              matches={searchMatches}
              onSearchChange={onSearchChange}
              onSelectDefinition={onSelectDefinition}
            />
          ) : null}
        </div>

        <div className={`tabPage ${activeTab === 'progress' ? 'active' : ''}`} role="tabpanel">
          {activeTab === 'progress' && raw && rendered ? (
            <ProgressTab trackGraph={trackGraph ?? rendered} learned={learned} />
          ) : null}
        </div>
      </div>
    </div>
  );
};

export default BottomPanel;
