import { forwardRef, useImperativeHandle } from 'react';
import { cleanup, render, screen, waitFor, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import defs from '../../public/defs.json';
import App from '../../src/App';
import { vi } from 'vitest';

type DefNode = {
  id: string;
  title: string;
  deps: string[];
};

type DefGraph = {
  nodes: DefNode[];
};

vi.mock('../../src/components/GraphCanvas', () => {
  const MockGraphCanvas = forwardRef(function MockGraphCanvas(
    props: {
      graph: { nodes: Array<{ id: string; title: string }>; edges: Array<unknown> } | null;
      selectedNodeId: string | null;
      onNodeClick: (id: string) => void;
    },
    ref,
  ) {
    useImperativeHandle(ref, () => ({
      focusRing: () => undefined,
      focusRingOfNode: () => undefined,
      focusHighestActiveRing: () => undefined,
    }));

    return (
      <div
        data-testid="graph-canvas"
        data-rendered-node-count={String(props.graph?.nodes.length ?? 0)}
        data-rendered-edge-count={String(props.graph?.edges.length ?? 0)}
        data-selected-node-id={props.selectedNodeId ?? ''}
      >
        {props.graph?.nodes.map((node) => (
          <button key={node.id} type="button" onClick={() => props.onNodeClick(node.id)}>
            {node.title}
          </button>
        ))}
      </div>
    );
  });

  return {
    __esModule: true,
    default: MockGraphCanvas,
  };
});

function prerequisiteClosure(graph: DefGraph, startId: string): Set<string> {
  const byId = new Map(graph.nodes.map((node) => [node.id, node] as const));
  const visited = new Set<string>();
  const stack = [startId];

  while (stack.length > 0) {
    const currentId = stack.pop()!;
    if (visited.has(currentId)) continue;

    const current = byId.get(currentId);
    if (!current) continue;

    visited.add(currentId);
    for (const depId of current.deps ?? []) {
      stack.push(depId);
    }
  }

  return visited;
}

async function renderApp() {
  const user = userEvent.setup();
  render(<App />);
  await screen.findByTestId('graph-canvas');
  await screen.findByTestId('definition-title');
  await closeInfoModal(user);

  return { user };
}

async function closeInfoModal(user: ReturnType<typeof userEvent.setup>) {
  const infoDialog = screen
    .queryAllByRole('dialog')
    .find((dialog) => within(dialog).queryByRole('heading', { name: 'Info' }));

  if (infoDialog) {
    await user.click(within(infoDialog).getByRole('button', { name: 'Close' }));
  }
}

function graphCount(): number {
  return Number(screen.getByTestId('graph-canvas').getAttribute('data-rendered-node-count') ?? '0');
}

async function openFilters(user: ReturnType<typeof userEvent.setup>) {
  await user.click(screen.getByRole('button', { name: 'Filters' }));
  return screen.getByTestId('categories-tree');
}

function getTreeRowCheckboxByText(text: string): HTMLInputElement {
  const tree = screen.getByTestId('categories-tree');
  const label = within(tree).getByText(text);
  const row = label.closest('.treeRow');
  if (!row) throw new Error(`Tree row not found for ${text}`);
  const checkbox = row.querySelector('input[type="checkbox"]');
  if (!(checkbox instanceof HTMLInputElement)) throw new Error(`Checkbox not found for ${text}`);
  return checkbox;
}

describe('App integration scenarios', () => {
  it('shows the main layout and auto-selects an initial ready definition', async () => {
    await renderApp();

    expect(screen.getByTestId('top-menu')).toBeInTheDocument();
    expect(screen.getByTestId('bottom-panel')).toHaveAttribute('data-expanded', 'true');
    expect(screen.getByTestId('graph-canvas')).toBeInTheDocument();

    expect(screen.getByTestId('definition-title')).not.toHaveTextContent(/^\s*$/);
    expect(screen.getByTestId('mark-learned-button')).toBeEnabled();

    expect(screen.getByTestId('graph-canvas').getAttribute('data-selected-node-id')).toBeTruthy();
  });

  it('persists bottom panel collapse state across remounts', async () => {
    const firstRender = await renderApp();
    await firstRender.user.click(screen.getByRole('button', { name: 'Definition' }));

    expect(screen.getByTestId('bottom-panel')).toHaveAttribute('data-expanded', 'false');
    expect(localStorage.getItem('definit-db.ui.bottomPanelCollapsed')).toBe('1');

    cleanup();
    await renderApp();

    expect(screen.getByTestId('bottom-panel')).toHaveAttribute('data-expanded', 'false');
  });

  it('filters the graph to the selected definition prerequisites from search', async () => {
    const selectedId = 'mathematics/fibonacci';
    const expectedNodeCount = prerequisiteClosure(defs as DefGraph, selectedId).size;
    const { user } = await renderApp();

    await user.click(screen.getByRole('button', { name: 'Filters' }));
    await user.click(screen.getByLabelText('Show not-ready nodes'));

    const searchInput = screen.getByLabelText('Search definition');
    await user.clear(searchInput);
    await user.type(searchInput, 'fibonacci');

    const matches = await screen.findByTestId('definition-search-matches');
    await user.click(within(matches).getByText(selectedId, { exact: true }));

    await waitFor(() => {
      expect(screen.getByTestId('graph-canvas')).toHaveAttribute('data-selected-node-id', selectedId);
      expect(screen.getByTestId('definition-title')).toHaveTextContent('fibonacci');
      expect(screen.getByTestId('graph-canvas')).toHaveAttribute(
        'data-rendered-node-count',
        String(expectedNodeCount),
      );
    });
  });

  it('marks a definition as learned and restores progress from localStorage', async () => {
    const { user } = await renderApp();
    const selectedBefore = screen.getByTestId('graph-canvas').getAttribute('data-selected-node-id');

    await user.click(screen.getByTestId('mark-learned-button'));

    await waitFor(() => {
      expect(screen.getByTestId('graph-canvas').getAttribute('data-selected-node-id')).not.toBe(selectedBefore);
    });

    await user.click(screen.getByRole('button', { name: 'Progress' }));

    await waitFor(() => {
      expect(screen.getByText(/^1 out of \d+$/)).toBeInTheDocument();
    });

    expect(JSON.parse(localStorage.getItem('definit-db.learned') ?? '[]')).toHaveLength(1);

    cleanup();
    const secondRender = await renderApp();

    await secondRender.user.click(screen.getByRole('button', { name: 'Progress' }));
    await waitFor(() => {
      expect(screen.getByText(/^1 out of \d+$/)).toBeInTheDocument();
    });
  });

  it('allows clicking dependency links inside a definition to navigate to that dependency', async () => {
    const { user } = await renderApp();

    await openFilters(user);
    await user.click(screen.getByLabelText('Show not-ready nodes'));
    const searchInput = screen.getByLabelText('Search definition');
    await user.type(searchInput, 'fibonacci');
    const matches = await screen.findByTestId('definition-search-matches');
    await user.click(within(matches).getByText('mathematics/fibonacci', { exact: true }));

    await user.click(within(screen.getByTestId('definition-body')).getByText('sequence'));

    await waitFor(() => {
      expect(screen.getByTestId('definition-title')).toHaveTextContent('sequence');
      expect(screen.getByTestId('graph-canvas')).toHaveAttribute('data-selected-node-id', 'mathematics/sequence');
    });
  });

  it('updates rendered graph when node state filters change', async () => {
    const { user } = await renderApp();
    const initialCount = graphCount();

    await openFilters(user);
    await user.click(screen.getByLabelText('Show not-ready nodes'));

    await waitFor(() => {
      expect(graphCount()).toBeGreaterThan(initialCount);
    });

    const afterNotReady = graphCount();
    await user.click(screen.getByLabelText('Show ready-to-learn nodes'));

    await waitFor(() => {
      expect(graphCount()).toBeLessThan(afterNotReady);
    });
  });

  it('supports including and excluding definitions via category checkboxes', async () => {
    const { user } = await renderApp();
    const initialCount = graphCount();

    await openFilters(user);
    await user.click(getTreeRowCheckboxByText('criterion'));

    await waitFor(() => {
      expect(graphCount()).toBe(initialCount - 1);
    });

    await user.click(getTreeRowCheckboxByText('criterion'));

    await waitFor(() => {
      expect(graphCount()).toBe(initialCount);
    });
  });

  it('restores category expand-collapse state from localStorage', async () => {
    const { user } = await renderApp();

    const tree = await openFilters(user);
    expect(within(tree).getByText('criterion')).toBeInTheDocument();

    await user.click(within(tree).getByText('mathematics'));

    await waitFor(() => {
      expect(within(tree).queryByText('criterion')).not.toBeInTheDocument();
    });

    cleanup();
    const second = await renderApp();
    const secondTree = await openFilters(second.user);

    expect(within(secondTree).queryByText('criterion')).not.toBeInTheDocument();
  });

  it('disables learning for a not-ready definition selected from search', async () => {
    const { user } = await renderApp();

    await openFilters(user);
    await user.click(screen.getByLabelText('Show not-ready nodes'));
    const searchInput = screen.getByLabelText('Search definition');
    await user.type(searchInput, 'fibonacci');
    const matches = await screen.findByTestId('definition-search-matches');
    await user.click(within(matches).getByText('mathematics/fibonacci', { exact: true }));

    await waitFor(() => {
      expect(screen.getByTestId('mark-learned-button')).toBeDisabled();
    });
  });

  it('resets learned progress after confirmation', async () => {
    const { user } = await renderApp();

    await user.click(screen.getByTestId('mark-learned-button'));
    await waitFor(() => {
      expect(JSON.parse(localStorage.getItem('definit-db.learned') ?? '[]')).toHaveLength(1);
    });

    await user.click(screen.getByRole('button', { name: 'Reset progress' }));
    const resetDialog = screen
      .queryAllByRole('dialog')
      .find((dialog) => within(dialog).queryByRole('heading', { name: 'Reset progress?' }));
    expect(resetDialog).toBeTruthy();
    await user.click(within(resetDialog!).getByRole('button', { name: 'Reset' }));

    await waitFor(() => {
      expect(JSON.parse(localStorage.getItem('definit-db.learned') ?? '[]')).toHaveLength(0);
      expect(screen.getByRole('button', { name: 'Reset progress' })).toBeDisabled();
    });
  });
});