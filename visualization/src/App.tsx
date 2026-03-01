import { useRef, useCallback, useEffect } from 'react';
import { useAppState } from './hooks/useAppState';
import TopMenu from './components/TopMenu';
import GraphCanvas, { type GraphCanvasHandle } from './components/GraphCanvas';
import BottomPanel from './components/BottomPanel';
import BottomMenu from './components/BottomMenu';
import InfoModal from './components/InfoModal';
import ResetConfirmModal from './components/ResetConfirmModal';

const App = () => {
  const state = useAppState();
  const graphRef = useRef<GraphCanvasHandle>(null);

  // After learning, switch to the next ready-to-learn definition if one exists
  const handleMarkLearned = useCallback(
    (id: string) => {
      state.markLearned(id);
    },
    [state.markLearned],
  );

  const handleNodeClick = useCallback(
    (id: string) => {
      state.selectLeaf(id);
      requestAnimationFrame(() => {
        graphRef.current?.focusRingOfNode(id);
      });
    },
    [state.selectLeaf],
  );

  const handleDepClick = useCallback(
    (id: string) => {
      state.selectLeaf(id);
      requestAnimationFrame(() => {
        graphRef.current?.focusRingOfNode(id);
      });
    },
    [state.selectLeaf],
  );

  const handleCategorySelect = useCallback(
    (id: string) => {
      state.selectLeaf(id);
      state.setActiveTab('definition');
      if (state.panelCollapsed) {
        state.setPanelCollapsed(false);
      }
      requestAnimationFrame(() => {
        graphRef.current?.focusRingOfNode(id);
      });
    },
    [state.selectLeaf, state.setActiveTab, state.panelCollapsed, state.setPanelCollapsed],
  );

  const handleFocus = useCallback(() => {
    state.focusMode();
    requestAnimationFrame(() => {
      // After focus mode rerender, select next ready
      setTimeout(() => {
        const nextId = state.getNextReadyId();
        if (nextId) {
          state.selectLeaf(nextId);
          requestAnimationFrame(() => {
            graphRef.current?.focusRingOfNode(nextId);
          });
        } else {
          graphRef.current?.focusHighestActiveRing();
        }
      }, 50);
    });
  }, [state.focusMode, state.getNextReadyId, state.selectLeaf]);

  const handleOverview = useCallback(() => {
    if (!state.rendered) return;
    const maxLevel = Math.max(0, ...state.rendered.nodes.map((n) => n.level ?? 0));
    graphRef.current?.focusRing(maxLevel);
  }, [state.rendered]);

  const handleResetProgress = useCallback(() => {
    if (state.learned.size === 0) return;
    state.setResetConfirmOpen(true);
  }, [state.learned.size, state.setResetConfirmOpen]);

  // Focus on selected node when it changes
  useEffect(() => {
    if (state.selectedLeafId) {
      requestAnimationFrame(() => {
        graphRef.current?.focusRingOfNode(state.selectedLeafId!);
      });
    }
  }, [state.selectedLeafId]);

  // Initial focus after first render
  const initialFocusDone = useRef(false);
  useEffect(() => {
    if (state.rendered && !initialFocusDone.current) {
      initialFocusDone.current = true;
      requestAnimationFrame(() => {
        if (state.selectedLeafId) {
          graphRef.current?.focusRingOfNode(state.selectedLeafId);
        } else {
          graphRef.current?.focusHighestActiveRing();
        }
      });
    }
  }, [state.rendered, state.selectedLeafId]);

  return (
    <div id="app">
      <div className="viewport">
        <button
          className="infoFab"
          type="button"
          aria-label="Show info"
          title="Info"
          onClick={() => state.setInfoOpen(true)}
        >
          i
        </button>

        <InfoModal open={state.infoOpen} onClose={() => state.setInfoOpen(false)} />

        <ResetConfirmModal
          open={state.resetConfirmOpen}
          onConfirm={() => state.resetProgress()}
          onCancel={() => state.setResetConfirmOpen(false)}
        />

        <TopMenu
          hasLearned={state.learned.size > 0}
          onFocus={handleFocus}
          onOverview={handleOverview}
          onResetProgress={handleResetProgress}
        />

        <div className={`mainPanel ${!state.panelCollapsed ? 'expanded' : ''}`}>
          <GraphCanvas
            ref={graphRef}
            graph={state.rendered}
            learned={state.learned}
            searchQuery={state.searchQuery}
            selectedNodeId={state.selectedLeafId}
            onNodeClick={handleNodeClick}
          />

          <BottomPanel
            expanded={!state.panelCollapsed}
            activeTab={state.activeTab}
            onTabChange={state.setActiveTab}
            selectedNode={state.selectedNode}
            renderedNodes={state.rendered?.nodes ?? []}
            learned={state.learned}
            onMarkLearned={handleMarkLearned}
            onDepClick={handleDepClick}
            raw={state.raw}
            rendered={state.rendered}
            includedIds={state.includedIds}
            onSelectLeaf={handleCategorySelect}
            onSetIncluded={state.setIncluded}
            onSetIncludedMany={state.setIncludedMany}
          />
        </div>

        <BottomMenu
          panelCollapsed={state.panelCollapsed}
          searchQuery={state.searchQuery}
          onTogglePanel={() => state.setPanelCollapsed(!state.panelCollapsed)}
          onSearchChange={state.setSearchQuery}
        />
      </div>
    </div>
  );
};

export default App;
