import { expect, test, type Page } from '@playwright/test';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { buildRaw, prerequisiteClosure } from '../../src/lib/graph';
import type { DefGraph } from '../../src/types';

const defsPath = fileURLToPath(new URL('../../public/defs.json', import.meta.url));
const defs = JSON.parse(readFileSync(defsPath, 'utf8')) as DefGraph;

async function gotoApp(page: Page): Promise<void> {
  await page.goto('/');
  await expect(page.getByRole('img', { name: 'Definitions graph' })).toBeVisible();
  await page.waitForFunction(() => {
    return document.querySelectorAll('g.node').length > 0;
  });
}

async function closeInfoModalIfVisible(page: Page): Promise<void> {
  const dialog = page.getByRole('dialog').filter({ has: page.getByRole('heading', { name: 'Info' }) });
  if (await dialog.isVisible()) {
    await dialog.getByRole('button', { name: 'Close' }).click();
  }
}

test.beforeEach(async ({ page }) => {
  await page.addInitScript(() => {
    localStorage.clear();
  });
});

test('shows the main layout and auto-selects an initial ready definition', async ({ page }) => {
  await gotoApp(page);
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

  await page.getByRole('button', { name: 'Definition' }).click();
  await expect(page.locator('.bottomPanel[aria-label="Bottom panel"]')).toBeHidden();

  await expect
    .poll(async () => page.evaluate(() => localStorage.getItem('definit-db.ui.bottomPanelCollapsed')))
    .toBe('1');

  await page.reload();
  await closeInfoModalIfVisible(page);

  await expect(page.locator('.bottomPanel[aria-label="Bottom panel"]')).toBeHidden();
  await page.getByRole('button', { name: 'Filters' }).click();
  await expect(page.locator('.bottomPanel[aria-label="Bottom panel"]')).toBeVisible();
});

test('filters the graph to the selected definition prerequisites from search', async ({ page }) => {
  const selectedId = 'mathematics/fibonacci';
  const expectedNodeCount = prerequisiteClosure(buildRaw(defs), selectedId).size;

  await gotoApp(page);
  await closeInfoModalIfVisible(page);

  await page.getByRole('button', { name: 'Filters' }).click();
  await page.getByLabel('Show not-ready nodes').check();

  const searchInput = page.getByLabel('Search definition');
  await searchInput.fill('fibonacci');
  await expect(page.getByRole('listbox', { name: 'Definition matches' })).toBeVisible();
  await page.getByText(selectedId, { exact: true }).click();

  await expect(page.getByRole('heading', { level: 3, name: 'fibonacci' })).toBeVisible();
  await expect
    .poll(async () => page.evaluate(() => document.querySelectorAll('g.node').length))
    .toBe(expectedNodeCount);
});

test('marks a definition as learned and restores progress from localStorage', async ({ page }) => {
  await gotoApp(page);
  await closeInfoModalIfVisible(page);

  const markLearnedButton = page.getByRole('button', { name: /Mark .* as learned/ });
  await expect(markLearnedButton).toBeEnabled();
  await markLearnedButton.click();

  await page.getByRole('button', { name: 'Progress' }).click();
  await expect(page.getByText(/Definitions learned/i)).toBeVisible();
  await expect(page.getByText(/^1 out of \d+$/)).toBeVisible();

  await expect
    .poll(async () => page.evaluate(() => JSON.parse(localStorage.getItem('definit-db.learned') ?? '[]').length))
    .toBe(1);

  await page.reload();
  await page.getByRole('button', { name: 'Progress' }).click();
  await expect(page.getByText(/^1 out of \d+$/)).toBeVisible();
});