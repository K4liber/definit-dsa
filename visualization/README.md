# DefinIT - Data Structures and Algorithms — Visualization

Visualization of the Data Structures and Algorithms definitions.

## Prerequisites

- Node.js (recommended: Node 18+)
- npm

## Install

From the repo root:

1. Go to the visualization folder:
   - `cd visualization`

2. Install dependencies:
   - `npm install`

## Generate graph data

Generate `public/defs.json` from the markdown database:

- `npm run gen:data`

This reads:
- `../src/definit_db/data_md/index.md`
- `../src/definit_db/data_md/definitions/**/*.md`

and writes:
- `visualization/public/defs.json`

If generation fails with a cycle error, it usually means dependency extraction is too permissive (e.g. self-references or non-definition links were interpreted as dependencies). See **Troubleshooting** below.

## Run the dev server

Start the app:

- `npm run dev`

Open the URL printed by Vite (typically `http://localhost:5173`).

## Build + preview

- `npm run build`
- `npm run preview`

## Tests

Directory `visualization\tests` contains tests of various types.

### Test groups

- **Unit**: verify isolated logic with small scope and minimal setup. In this repo that means pure helpers such as graph logic, storage helpers, and generator utilities.
- **Integration**: render React components or the whole app in `jsdom` and verify user-visible workflows across multiple parts working together.
- **E2E**: run the app in a real browser and verify behavior end to end, including browser-specific behavior that `jsdom` does not reproduce. These tests are currently disabled in CI and need to be fixed before they are re-enabled.
- **Manual**: for scenarios that are mostly about aesthetics, motion, or subjective usability.

### Debug e2e test

`npx playwright test --grep "persists bottom panel" --debug`

## Troubleshooting

### “Cycle detected …” during `npm run gen:data`

The generator enforces DAG constraints. A cycle error usually comes from one of:

- A real cycle in the underlying definition dependencies
- A **false-positive dependency** (most common), e.g. a definition linking to itself or using a generic markdown link that looks like a dependency.

The generator tries to reduce false positives by:

- Ignoring self-dependencies
- Only keeping dependencies that exist in `index.md`

### Playwright troubleshooting

The Playwright config starts the Vite dev server automatically and, on Windows, uses the locally installed Microsoft Edge browser so no extra browser download is required.

If your machine blocks browser automation by policy or certificate interception, use the Vitest integration tests as the default automated check. The Playwright E2E suite is currently disabled in CI until it is fixed.

## Bugs to be solved

No bugs, for now :)
