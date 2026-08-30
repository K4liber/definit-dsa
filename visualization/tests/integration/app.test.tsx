import { forwardRef, useImperativeHandle } from 'react';
import { cleanup, fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import defs from '../../../docs/defs.json';
import App from '../../src/App';
import { buildRaw, dependentsClosure } from '../../src/lib/graph';
import { describe, expect, it, vi } from 'vitest';

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
        role="img"
        aria-label="Definitions graph"
      >
        {props.graph?.nodes.map((node) => (
          <button
            key={node.id}
            type="button"
            aria-pressed={props.selectedNodeId === node.id}
            onClick={() => props.onNodeClick(node.id)}
          >
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

async function renderApp() {
  const user = userEvent.setup();
  render(<App />);
  await screen.findByRole('img', { name: 'Definitions graph' });
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
  return within(screen.getByRole('img', { name: 'Definitions graph' })).getAllByRole('button').length;
}

function getSelectedGraphNodeButton(): HTMLButtonElement | null {
  const graph = screen.getByRole('img', { name: 'Definitions graph' });
  return (
    within(graph)
      .queryAllByRole('button')
      .find((button): button is HTMLButtonElement => button instanceof HTMLButtonElement && button.getAttribute('aria-pressed') === 'true') ?? null
  );
}

function getBottomPanel(): HTMLElement {
  const panel = screen
    .getAllByRole('region', { hidden: true })
    .find((region) => region.getAttribute('aria-label') === 'Bottom panel');

  if (!panel) throw new Error('Bottom panel not found');
  return panel;
}

function openFilters() {
  fireEvent.click(screen.getByRole('button', { name: 'Filters' }));
  return screen.getByRole('region', { name: 'Track filtering' });
}

async function searchAndToggleDefinition(query: string, id: string) {
  const searchInput = screen.getByLabelText('Search definition');
  fireEvent.change(searchInput, { target: { value: query } });

  const matches = await screen.findByRole('listbox', { name: 'Definition matches' });
  const matchText = within(matches).getByText(id, { exact: true });
  const matchLabel = matchText.closest('label');
  if (!matchLabel) throw new Error(`Search match label not found for ${id}`);

  const checkbox = matchLabel.querySelector('input[type="checkbox"]');
  if (!(checkbox instanceof HTMLInputElement)) throw new Error(`Search match checkbox not found for ${id}`);
  fireEvent.click(checkbox);
}

function getGraphNodeButtonByTitle(title: string): HTMLButtonElement | null {
  const graph = screen.getByRole('img', { name: 'Definitions graph' });
  return (
    within(graph)
      .queryAllByRole('button')
      .find((button): button is HTMLButtonElement => button.textContent === title) ?? null
  );
}

describe('App integration scenarios', () => {
  it('shows the main layout and auto-selects an initial ready definition', async () => {
    await renderApp();

    expect(screen.getByRole('toolbar', { name: 'Top menu' })).toBeInTheDocument();
    expect(getBottomPanel()).toBeVisible();
    expect(screen.getByRole('img', { name: 'Definitions graph' })).toBeInTheDocument();

    expect(screen.getByRole('heading', { level: 3 })).not.toHaveTextContent(/^\s*$/);
    expect(screen.getByRole('button', { name: /Mark .* as learned/ })).toBeEnabled();

    expect(getSelectedGraphNodeButton()).toBeTruthy();
  });

  it('persists bottom panel collapse state across remounts', async () => {
    const firstRender = await renderApp();
    await firstRender.user.click(screen.getByRole('button', { name: 'Definition' }));

    expect(getBottomPanel()).toHaveAttribute('aria-hidden', 'true');
    expect(localStorage.getItem('definit-db.ui.bottomPanelCollapsed')).toBe('1');

    cleanup();
    await renderApp();

    expect(getBottomPanel()).toHaveAttribute('aria-hidden', 'true');
  });

  it('adds a definition to the track and expands it with its descendants', async () => {
    const selectedId = 'mathematics/observable'; // root definition
    const expectedCount = dependentsClosure(buildRaw(defs), [selectedId]).size;
    await renderApp();

    openFilters();
    // Remove the default group so only the searched definition (plus its
    // descendants) defines the track, and show not-ready nodes so all
    // descendants are visible.
    fireEvent.click(screen.getByRole('checkbox', { name: 'Group Data Structures and Algorithms' }));
    fireEvent.click(screen.getByLabelText('Show not-ready definitions'));

    await searchAndToggleDefinition('observable', selectedId);

    await waitFor(() => {
      expect(graphCount()).toBe(expectedCount);
    });
  });

  it('marks a definition as learned and restores progress from localStorage', async () => {
    const { user } = await renderApp();
    const selectedBefore = getSelectedGraphNodeButton()?.textContent;

    await user.click(screen.getByRole('button', { name: /Mark .* as learned/ }));

    await waitFor(() => {
      expect(getSelectedGraphNodeButton()?.textContent).not.toBe(selectedBefore);
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
    await renderApp();

    openFilters();
    fireEvent.click(screen.getByLabelText('Show not-ready definitions'));
    await searchAndToggleDefinition('fibonacci', 'mathematics/fibonacci');
    // Select the fibonacci node (clicking a node opens the Definition tab).
    fireEvent.click(getGraphNodeButtonByTitle('fibonacci')!);

    const depLink = (await screen.findAllByText('sequence', { selector: 'span.dep' }))[0];
    fireEvent.click(depLink);

    await waitFor(
      () => {
        expect(screen.getByRole('heading', { level: 3, name: 'sequence' })).toBeInTheDocument();
        expect(getSelectedGraphNodeButton()).toHaveTextContent('sequence');
      },
      { timeout: 5000 },
    );
  }, 20000);

  it('updates rendered graph when node state filters change', async () => {
    await renderApp();
    const initialCount = graphCount();

    openFilters();
    fireEvent.click(screen.getByLabelText('Show not-ready definitions'));

    await waitFor(() => {
      expect(graphCount()).toBeGreaterThan(initialCount);
    });

    const afterNotReady = graphCount();
    fireEvent.click(screen.getByLabelText('Show ready-to-learn definitions'));

    await waitFor(() => {
      expect(graphCount()).toBeLessThan(afterNotReady);
    });
  });

  it('excludes learned definitions from the graph when unchecking show learned', async () => {
    const { user } = await renderApp();
    const markedTitle = getSelectedGraphNodeButton()?.textContent ?? '';
    expect(markedTitle).not.toBe('');

    await user.click(screen.getByRole('button', { name: /Mark .* as learned/ }));
    // The learned node disappears from the graph only after "Show learned" is off.
    expect(getGraphNodeButtonByTitle(markedTitle)).not.toBeNull();

    openFilters();
    fireEvent.click(screen.getByLabelText('Show learned definitions'));

    await waitFor(() => {
      expect(getGraphNodeButtonByTitle(markedTitle)).toBeNull();
    });
  });

  it('finds definitions by alias in the search input', async () => {
    await renderApp();

    openFilters();
    const searchInput = screen.getByLabelText('Search definition');
    fireEvent.change(searchInput, { target: { value: 'dfs' } });

    const matches = await screen.findByRole('listbox', { name: 'Definition matches' });
    expect(within(matches).getByText('mathematics/depth_first_search')).toBeInTheDocument();
  });

  it('resets filters to the default values', async () => {
    await renderApp();

    openFilters();
    fireEvent.click(screen.getByLabelText('Show learned definitions'));
    fireEvent.click(screen.getByLabelText('Show ready-to-learn definitions'));
    fireEvent.click(screen.getByRole('checkbox', { name: 'Group Data Structures and Algorithms' }));
    fireEvent.click(screen.getByLabelText('Include descendants'));

    const stored = JSON.parse(localStorage.getItem('definit-db.ui.filters') ?? '{}');
    expect(stored.track.groupIds).toEqual([]);
    expect(stored.track.includeDescendants).toBe(false);

    fireEvent.click(screen.getByRole('button', { name: 'Reset filters' }));

    await waitFor(() => {
      expect((screen.getByLabelText('Show learned definitions') as HTMLInputElement).checked).toBe(true);
      expect(
        (
          screen.getByRole('checkbox', {
            name: 'Group Data Structures and Algorithms',
          }) as HTMLInputElement
        ).checked,
      ).toBe(true);
      expect((screen.getByLabelText('Include descendants') as HTMLInputElement).checked).toBe(true);

      const reset = JSON.parse(localStorage.getItem('definit-db.ui.filters') ?? '{}');
      expect(reset.track.groupIds).toEqual(['data_structures_and_algorithms']);
      expect(reset.track.includeDescendants).toBe(true);
      expect(reset.visualization).toEqual({
        showLearned: true,
        showReady: true,
        showPreReady: true,
        showNotReady: false,
      });
    });
  });

  it('disables learning for a not-ready definition selected via dependency link', async () => {
    await renderApp();

    openFilters();
    fireEvent.click(screen.getByLabelText('Show not-ready definitions'));
    await searchAndToggleDefinition('fibonacci', 'mathematics/fibonacci');
    // Select the fibonacci node (clicking a node opens the Definition tab).
    fireEvent.click(getGraphNodeButtonByTitle('fibonacci')!);

    await waitFor(
      () => {
        expect(screen.getByRole('heading', { level: 3, name: 'fibonacci' })).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /Mark .* as learned/ })).toBeDisabled();
      },
      { timeout: 5000 },
    );
  }, 20000);

  it('resets learned progress after confirmation', async () => {
    const { user } = await renderApp();

    await user.click(screen.getByRole('button', { name: /Mark .* as learned/ }));
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