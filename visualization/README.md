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

The build reads the graph data from `../docs/defs.json` (imported in
`src/hooks/useAppState.ts`) and outputs the production bundle to
`visualization/dist`.

## Update GitHub Pages (`docs/`)

GitHub Pages serves the repo-root `docs/` folder. To publish a new build:

1. (Only if the definition data changed) regenerate the graph data and refresh
   `docs/defs.json` so the build picks it up:
   - `npm run gen:data`
   - copy `visualization/public/defs.json` to `../docs/defs.json`

2. Build the app (outputs to `visualization/dist`):
   - `npm run build`

3. Replace the contents of `docs/` with the new build, keeping `docs/defs.json`:
   - delete `docs/assets` (removes the previous hashed bundles)
   - copy `dist/index.html` to `docs/index.html`
   - copy `dist/assets` to `docs/assets`

   PowerShell, from the repo root:

   ```powershell
   $dist = 'visualization\dist'
   $docs = 'docs'
   Remove-Item -Recurse -Force "$docs\assets"
   Copy-Item "$dist\index.html" "$docs\index.html" -Force
   Copy-Item -Recurse "$dist\assets" "$docs\assets" -Force
   ```

4. Confirm `docs/index.html` references the new hashed bundle under
   `/definit-dsa/assets/`, then commit and push `docs/`. GitHub Pages will pick
   up the change automatically.

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

## Bugs to be solved

No bugs, for now :)
