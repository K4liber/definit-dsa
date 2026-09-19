import { expect, test, type Page } from '@playwright/test';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { buildRaw, prerequisiteClosure } from '../../src/lib/graph';
import type { DefGraph } from '../../src/types';

const defsPath = fileURLToPath(new URL('../../../docs/defs.json', import.meta.url));
const defs = JSON.parse(readFileSync(defsPath, 'utf8')) as DefGraph;

async function gotoApp(page: Page): Promise<void> {
  await page.goto('/');
  await expect(page.getByRole('img', { name: 'Definitions graph' })).toBeVisible();
  await page.waitForFunction(() => {
    return document.querySelectorAll('g.node').length > 0;
  });
}

async function closeInfoModalIfVisible(page: Page): Promise<void> {
  // Initialization (INIT_COMPLETE) both decides the info modal and writes the
  // `sel` routing param. Waiting for that signal avoids probing for the modal
  // before the app decided whether to show it (it can appear late on slow
  // machines and would then block every following interaction).
  await page.waitForURL(/([?&])sel=/, { timeout: 15000 }).catch(() => undefined);
  const dialog = page.getByRole('dialog').filter({ has: page.getByRole('heading', { name: 'Info' }) });
  // The modal opens after the app initializes (only when nothing is learned),
  // which can happen slightly after the graph becomes visible — give it a
  // moment to appear before deciding it will not show.
  await dialog.waitFor({ state: 'visible', timeout: 3000 }).catch(() => undefined);
  if (await dialog.isVisible()) {
    await dialog.getByRole('button', { name: 'Close' }).click();
    await dialog.waitFor({ state: 'hidden', timeout: 5000 }).catch(() => undefined);
  }
}

test('shows the main layout and auto-selects an initial ready definition', async ({ page }) => {
  await gotoApp(page);
  await page.evaluate(() => localStorage.clear()); // initial clear
  await closeInfoModalIfVisible(page);

  await expect(page.getByRole('toolbar', { name: 'Top menu' })).toBeVisible();
  await expect(page.getByRole('img', { name: 'Definitions graph' })).toBeVisible();
  await expect(page.locator('.bottomPanel[aria-label="Bottom panel"]')).toBeVisible();
  await expect(page.getByRole('toolbar', { name: 'Bottom panel tabs' })).toBeVisible();

  await expect(page.getByRole('heading', { level: 3 })).not.toHaveText('');
  await expect(page.getByRole('button', { name: /Mark .* as learned/ })).toBeEnabled();
});

test('persists bottom panel collapse state across reloads', async ({ page }) => {
  await gotoApp(page);
  await closeInfoModalIfVisible(page);
  // we need to have at least one definition learned to not automatically collapse the panel
  await page.getByRole('button', { name: /Mark .* as learned/ }).click();
  // now we can hide the bottom panel by reselecting the open tab
  await page.getByRole('button', { name: 'Definition' }).click();
  await expect(page.locator('.bottomPanel[aria-label="Bottom panel"]')).toBeHidden();
  // and reload the page
  await page.reload();
  // bottom panel should be hidden
  await expect(page.locator('.bottomPanel[aria-label="Bottom panel"]')).toBeHidden();
  await page.getByRole('button', { name: 'Filters' }).click();
  await expect(page.locator('.bottomPanel[aria-label="Bottom panel"]')).toBeVisible();
});

test('adds a definition to the track and expands it with its references', async ({ page }) => {
  const selectedId = 'mathematics/fibonacci'; // references: sequence, ...
  const expectedNodeCount = prerequisiteClosure(buildRaw(defs), selectedId).size;

  await gotoApp(page);
  await page.evaluate(() => localStorage.clear()); // initial clear
  await closeInfoModalIfVisible(page);

  await page.getByRole('button', { name: 'Filters' }).click();
  await page.getByRole('checkbox', { name: 'Group Data Structures and Algorithms' }).uncheck();
  // pull in the referenced (more basic) definitions the user should learn first
  await page.getByRole('checkbox', { name: 'Include references' }).check();
  // with nothing learned, the track is mostly not-ready, which is hidden by default
  await page.getByRole('checkbox', { name: 'Show not-ready definitions' }).check();

  const searchInput = page.getByLabel('Search definition');
  await searchInput.fill('fibonacci');
  await expect(page.getByRole('listbox', { name: 'Definition matches' })).toBeVisible();
  await page.getByText(selectedId, { exact: true }).click();

  await expect
    .poll(async () => page.evaluate(() => document.querySelectorAll('g.node').length))
    .toBe(expectedNodeCount);
});

test('marks a definition as learned and restores progress from localStorage', async ({ page }) => {
  await gotoApp(page);
  await page.evaluate(() => localStorage.clear()); // initial clear
  await closeInfoModalIfVisible(page);

  const markLearnedButton = page.getByRole('button', { name: /Mark .* as learned/ });
  await expect(markLearnedButton).toBeEnabled();
  await markLearnedButton.click();

  await page.getByRole('button', { name: 'Progress', exact: true }).click();
  await expect(page.getByText(/Definitions learned/i)).toBeVisible();
  await expect(page.getByText(/^1 out of \d+$/)).toBeVisible();

  await expect
    .poll(async () => page.evaluate(() => JSON.parse(localStorage.getItem('definit-db.learned') ?? '[]').length))
    .toBe(1);

  await page.reload();
  await page.getByRole('button', { name: 'Progress', exact: true }).click();
  await expect(page.getByText(/^1 out of \d+$/)).toBeVisible();
});

test('shares a filtered view through URL params and survives a reload', async ({ page }) => {
  test.setTimeout(90000); // multiple reloads; slow machine
  await gotoApp(page);
  await page.evaluate(() => localStorage.clear()); // initial clear
  await closeInfoModalIfVisible(page);

  // Change filters through the UI; the URL must follow.
  await page.getByRole('button', { name: 'Filters' }).click();
  await page.getByRole('checkbox', { name: 'Include references' }).check();
  await page.getByRole('checkbox', { name: 'Show not-ready definitions' }).check();

  await expect(page).toHaveURL(/ref=1/);
  await expect(page).toHaveURL(/notready=1/);

  // The filtered view survives a reload (persisted in browser storage).
  await page.reload();
  await closeInfoModalIfVisible(page);
  await page.getByRole('button', { name: 'Filters' }).click();
  await expect(page.getByRole('checkbox', { name: 'Include references' })).toBeChecked();
  await expect(page.getByRole('checkbox', { name: 'Show not-ready definitions' })).toBeChecked();

  // A shared link with only URL params (fresh storage) applies the same view.
  await page.evaluate(() => localStorage.clear());
  await page.goto('/?notready=1');
  // Wait for the app to load before the info modal can appear, then close it.
  await expect(page.getByRole('img', { name: 'Definitions graph' })).toBeVisible();
  await closeInfoModalIfVisible(page);
  await page.getByRole('button', { name: 'Filters' }).click();
  await expect(page.getByRole('checkbox', { name: 'Show not-ready definitions' })).toBeChecked();
  await expect(page.getByRole('checkbox', { name: 'Include references' })).not.toBeChecked();

  // "Reset filters" restores defaults, cleans filter params from the URL and
  // clears storage (only the routing param of the selected definition, `sel`,
  // may remain).
  await page.getByRole('button', { name: 'Reset filters' }).click();
  await expect(page).not.toHaveURL(/(ref|groups|defs|learned|ready|preready|notready)=/);
  await expect(page.getByRole('checkbox', { name: 'Show not-ready definitions' })).not.toBeChecked();
  await expect(
    page.evaluate(() => localStorage.getItem('definit-db.ui.filters')),
  ).resolves.toBeNull();
});
function nodeCircle(page: Page, title: string) {
  // The `g.node` bounding box includes offset label text, so its center can
  // fall on empty SVG space; the circle itself is the reliable click target.
  return page.locator(`g.node`, { hasText: title }).locator('circle.node-circle');
}

test('routes to a definition and goes back to the previous one', async ({ page }) => {
  await gotoApp(page);
  await page.evaluate(() => localStorage.clear()); // initial clear
  await closeInfoModalIfVisible(page);
  // Let the initial camera transition (focus ring, 650ms) settle so node
  // clicks are not blocked by the moving graph.
  await page.waitForTimeout(1000);

  // Clicking a node in the visualization routes the URL to that definition.
  await nodeCircle(page, 'observable').click();
  await expect(page).toHaveURL(/sel=mathematics%2Fobservable/);
  await expect(page.getByRole('heading', { level: 3, name: 'observable' })).toBeVisible();

  // Clicking a second node pushes another history entry.
  await page.waitForTimeout(1000); // camera refocus after selection
  await nodeCircle(page, 'trade_off').click();
  await expect(page).toHaveURL(/sel=mathematics%2Ftrade_off/);
  await expect(page.getByRole('heading', { level: 3, name: 'trade_off' })).toBeVisible();

  // Browser back returns to the previously viewed definition.
  await page.goBack();
  await expect(page).toHaveURL(/sel=mathematics%2Fobservable/);
  await expect(page.getByRole('heading', { level: 3, name: 'observable' })).toBeVisible();

  // Browser forward returns to the next definition again.
  await page.goForward();
  await expect(page).toHaveURL(/sel=mathematics%2Ftrade_off/);
  await expect(page.getByRole('heading', { level: 3, name: 'trade_off' })).toBeVisible();
});

test('opens a shared definition link directly', async ({ page }) => {
  await page.goto('/?sel=mathematics%2Fobservable');
  await expect(page.getByRole('img', { name: 'Definitions graph' })).toBeVisible();
  await closeInfoModalIfVisible(page);

  await expect(page.getByRole('heading', { level: 3, name: 'observable' })).toBeVisible();
  await expect(page).toHaveURL(/sel=mathematics%2Fobservable/);
});