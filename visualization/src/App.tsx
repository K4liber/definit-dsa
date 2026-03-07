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
    // Focus should not change bottom panel visibility or tabs.
    // It only advances selection to the next ready-to-learn node (if any).
    state.focusMode();

    requestAnimationFrame(() => {
      setTimeout(() => {
        const nextId = state.selectedLeafId;
        if (nextId) {
          graphRef.current?.focusRingOfNode(nextId);
        } else {
          graphRef.current?.focusHighestActiveRing();
        }
      }, 50);
    });
  }, [state.focusMode, state.selectedLeafId]);

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

  const handleBottomMenuTabClick = useCallback(
    (tab: import('./types').BottomTab) => {
      const isSameTab = state.activeTab === tab;

      if (state.panelCollapsed) {
        state.setPanelCollapsed(false);
        state.setActiveTab(tab);
        return;
      }

      // Panel is expanded
      if (isSameTab) {
        // Turn all tabs off and collapse
        state.setActiveTab(null);
        state.setPanelCollapsed(true);
      } else {
        state.setActiveTab(tab);
      }
    },
    [state.activeTab, state.panelCollapsed, state.setActiveTab, state.setPanelCollapsed],
  );

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
            activeTab={state.activeTab ?? 'definition'}
            onTabChange={state.setActiveTab as any}
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
            searchQuery={state.searchQuery}
            searchSelectedId={state.searchSelectedId}
            searchMatches={state.searchMatches}
            onSearchChange={state.setSearchQuery}
            onSelectMatch={(id) => {
              state.setSearchSelectedId(id);
              if (id) state.selectLeaf(id);
            }}
            showNotReady={state.showNotReady}
            showPreReady={state.showPreReady}
            showReady={state.showReady}
            showLearned={state.showLearned}
            onSetShowNotReady={state.setShowNotReady}
            onSetShowPreReady={state.setShowPreReady}
            onSetShowReady={state.setShowReady}
            onSetShowLearned={state.setShowLearned}
          />
        </div>

        <BottomMenu
          panelCollapsed={state.panelCollapsed}
          activeTab={state.activeTab}
          onTabClick={handleBottomMenuTabClick}
        />
      </div>
    </div>
  );
};

export default App;
