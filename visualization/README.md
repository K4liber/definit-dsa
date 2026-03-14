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

## Test groups

- **Unit tests**: verify isolated logic with small scope and minimal setup. In this repo that means pure helpers such as graph logic, storage helpers, and generator utilities.
- **Integration tests**: render React components or the whole app in `jsdom` and verify user-visible workflows across multiple parts working together.
- **E2E tests**: run the app in a real browser and verify behavior end to end, including browser-specific behavior that `jsdom` does not reproduce.
- **Manual or visual-review checks** for scenarios that are mostly about aesthetics, motion, or subjective usability.

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

If your machine blocks browser automation by policy or certificate interception, use the Vitest integration tests as the default automated check and enable Playwright on a machine where browser automation is allowed.

## Features & Test Scenarios

### #1 **Data Generation from Markdown**

**Importance**: Critical

**Test Scenario**

Run `npm run gen:data` and verify `public/defs.json` is created correctly. Verify the file contains all definitions from markdown source files.

**Automation**

Automated test: [tests/unit/gen-data.test.ts](tests/unit/gen-data.test.ts) (`generates defs.json from markdown input`).

### #2 **Cycle Detection in Generator**

**Importance**: Critical

**Test Scenario**

Run `npm run gen:data` with valid dependencies and verify successful generation. Introduce a cycle in test data and verify the generator fails with a cycle detection error message.

**Automation**

Automated test: [tests/unit/gen-data.test.ts](tests/unit/gen-data.test.ts) (`throws on cyclic dependencies in generated data`).

### #3 **Layout overview**

**Importance**: Critical

**Test Scenario**

The UI is split into three vertical regions:

- **Top menu**: primary view controls (Focus / Overview / Reset progress) and the info button
- **Graph canvas** (SVG visualization)
- **Bottom panel**
  - Expanded: graph and bottom panel share height (50/50 split)
  - Collapsed: graph uses full height and only the tab names are visible

**Automation**

Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`shows the main layout and auto-selects an initial ready definition`).

### #4 **Bottom Panel Collapse/Expand Toggle**

**Importance**: High

**Test Scenario**

Click on any tab name to expand the bottom panel. Click again on the same tab to collapse it. Verify that the collapsed state is saved to localStorage and persists after page reload.

**Automation**

Automated tests: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`persists bottom panel collapse state across remounts`) and [tests/unit/storage.test.ts](tests/unit/storage.test.ts) (`persists panel collapsed state as a boolean flag`).

### #5 **Bottom panel contents (tabs)**

**Importance**: Critical

**Test Scenario**

- **Scenario A: Definition tab shows selected definition content**
- **Scenario B: Definition tab supports “Mark as learned” for valid definitions**
- **Scenario C: Definition tab dependency links are clickable**
- **Scenario D: Filters tab search narrows the graph to the selected definition study path**
- **Scenario E: Filters tab category include/exclude checkboxes affect the rendered graph**
- **Scenario F: Filters tab node state checkboxes affect the rendered graph**
- **Scenario G: Progress tab updates definitions learned / edges unlocked / levels completed**

**Automation**

- Scenario A: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`shows the main layout and auto-selects an initial ready definition`).
- Scenario B: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`marks a definition as learned and restores progress from localStorage`).
- Scenario C: Automated tests: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`allows clicking dependency links inside a definition to navigate to that dependency`) and [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`renders dependency links as clickable spans in definition HTML`).
- Scenario D: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`filters the graph to the selected definition prerequisites from search`).
- Scenario E: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`supports including and excluding definitions via category checkboxes`).
- Scenario F: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`updates rendered graph when node state filters change`).
- Scenario G: Automated tests: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`marks a definition as learned and restores progress from localStorage`) and [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`computes progress stats for learned definitions, unlocked edges, and completed levels`).

### #6 **Categories filters**

**Importance**: Critical

**Test Scenario**

It is an Explorer-like tree:

- Category folders are derived from definition ids (split by `/`). The category level is displayed.
- Folders can be expanded/collapsed (including top-level “fields”).
- Leaf rows list definitions and show:
  - a state dot color
  - the definition level (`L#`).
- Definitions inside a category are sorted by:
  1) state
  2) level
  3) title

Verify that category folders are displayed in topologically sorted order by their computed level. Confirm folder levels are correctly computed and displayed.

**Automation**

Automated tests: [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`computes group levels from cross-group dependencies`, `sorts category groups by computed group level and leaves by state, level, and title`).

### #7 **Checkboxes behavior on categories filter**

**Importance**: Critical

**Test scenarios**

- **Scenario A: Unchecking a definition includes/excludes it from the rendered graph**
- **Scenario B: Unchecking a folder includes/excludes all definitions under that category**
- **Scenario C: Levels are recomputed on the rendered graph after checkbox filtering**
- **Scenario D: Learning state rules do not change when hidden prerequisites are filtered out**
- **Scenario E: Category expand/collapse state is restored from localStorage after reload**

**Automation**

- Scenario A: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`supports including and excluding definitions via category checkboxes`).
- Scenario B: Manual test.
- Scenario C: Automated test: [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`recomputes levels on the rendered graph after filtering hidden prerequisites`).
- Scenario D: Automated test: [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`marks partially unlocked nodes as pre-ready through the visible set`).
- Scenario E: Automated tests: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`restores category expand-collapse state from localStorage`) and [tests/unit/storage.test.ts](tests/unit/storage.test.ts) (`round-trips open category prefixes`).

### #8 **Search filter**

**Importance**: High

**Test Scenario**

Use the search input to query by node ID and title. After putting a character in a search input we should see a checkable list of all definitions that match with the current content of the input. User should be able to click on an element in the list and in such a case this is our new content of the input. User can only select a single element so the input can hold only one node (or zero) at any time. 

After a definition is selected, we should filter all definitions (from raw graph) and only select those who are either the selected node or any descendant. Finally, the user should only see a graph for a selected definition with all descendants that are needed to be learned before the selected definition can be learned.

**Automation**

Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`filters the graph to the selected definition prerequisites from search`).

### #9 **Learning State Rules**

**Importance**: High

**Test Scenario**

- **Scenario A: A node becomes already-learned after explicit marking**
- **Scenario B: A node is ready-to-learn only when all dependencies are learned**
- **Scenario C: A node becomes pre-ready-to-learn when it is partially unlocked by learned prerequisites**
- **Scenario D: Node colors reflect the four learning states correctly**

**Automation**

- Scenario A: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`marks a definition as learned and restores progress from localStorage`).
- Scenario B: Automated tests: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`disables learning for a not-ready definition selected from search`) and [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`selects the next ready definition using rendered levels and stable ordering`).
- Scenario C: Automated test: [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`marks partially unlocked nodes as pre-ready through the visible set`).
- Scenario D: Manual test.

### #10 **Node state filters**

**Importance**: High

**Test Scenario**

- **Scenario A: State filter checkboxes include/exclude matching nodes from the rendered graph**
- **Scenario B: Filtering by state recomputes rendered graph levels**

**Automation**

- Scenario A: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`updates rendered graph when node state filters change`).
- Scenario B: Automated test: [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`recomputes levels on the rendered graph after filtering hidden prerequisites`).

### #11 **Graph canvas display**

**Importance**: Critical

**Test Scenario**

Verify that the graph renders all definitions from `defs.json`. Ensure dependencies are correctly represented as directed edges where source depends on target.

**Automation**

Manual test.

### #12 **Graph canvas radial levels**

**Importance**: Critical

**Test Scenario**

- **Scenario A: Computed levels follow dependency ordering**
- **Scenario B: Nodes are arranged into concentric visual rings by level in the SVG canvas**

**Automation**

- Scenario A: Automated test: [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`recomputes levels on the rendered graph after filtering hidden prerequisites`).
- Scenario B: Manual test.

### #13 **Dependency-Based Learning Readiness**

**Importance**: Critical

**Test Scenario**

- **Scenario A: A definition with unmet prerequisites is not learnable**
- **Scenario B: A definition becomes learnable only after its prerequisites are learned**

**Automation**

- Scenario A: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`disables learning for a not-ready definition selected from search`).
- Scenario B: Automated tests: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`marks a definition as learned and restores progress from localStorage`) and [tests/unit/graph.test.ts](tests/unit/graph.test.ts) (`selects the next ready definition using rendered levels and stable ordering`).

### #14 **Mark Definition as Learned**

**Importance**: Critical

**Test Scenario**

- **Scenario A: A ready-to-learn definition has an enabled "Mark as learned" button**
- **Scenario B: Marking a definition updates progress and selects the next ready definition when available**
- **Scenario C: A not-ready definition has a disabled "Mark as learned" button**
- **Scenario D: The learned node color updates to the learned color**

**Automation**

- Scenario A: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`shows the main layout and auto-selects an initial ready definition`).
- Scenario B: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`marks a definition as learned and restores progress from localStorage`).
- Scenario C: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`disables learning for a not-ready definition selected from search`).
- Scenario D: Manual test.

### #15 **Learning State Persistence (localStorage)**

**Importance**: Critical

**Test Scenario**

- **Scenario A: Learned nodes are restored after reload from browser storage**
- **Scenario B: Resetting progress clears learned state**

**Automation**

- Scenario A: Automated tests: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`marks a definition as learned and restores progress from localStorage`) and [tests/unit/storage.test.ts](tests/unit/storage.test.ts) (`round-trips learned ids through localStorage`).
- Scenario B: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`resets learned progress after confirmation`).

### #16 **Node Click - Focus & Center View**

**Importance**: High

**Test Scenario**

Click on a definition node and verify the view centers/focuses on that node's ring/level. Verify that clicking different nodes updates the viewport accordingly.

**Automation**

Manual test.

### #17 **Node Hover - Level Ring Highlight**

**Importance**: High

**Test Scenario**

Hover over a node and verify that its entire ring/level is highlighted. Move to another node and verify the highlight updates.

**Automation**

Manual test.

### #18 **Initial View Focus on Next Ready-to-Learn Node**

**Importance**: High

**Test Scenario**

- **Scenario A: On startup, the next ready-to-learn definition is selected and its Definition tab is open**
- **Scenario B: On startup, the graph viewport focuses that node/ring visually**

**Automation**

- Scenario A: Automated test: [tests/integration/app.test.tsx](tests/integration/app.test.tsx) (`shows the main layout and auto-selects an initial ready definition`).
- Scenario B: Manual test.

### #19 **Edge Styling Based on Prerequisite State**

**Importance**: Medium

**Test Scenario**

Verify that edges connecting to learned prerequisites are rendered as **on edges** (more visible). Edges to unlearned prerequisites are **off edges** (dashed or subtler).

**Automation**

Manual test.

### #20 **Curved Edge Paths (Arc Toward Center)**

**Importance**: Medium

**Test Scenario**

Verify that all edges are rendered as curved paths that arc inward toward the center rather than straight lines. Check visual rendering for aesthetic quality.

**Automation**

Manual test.

### #21 **Responsive UI Design (Desktop & Mobile)**

**Importance**: Medium

**Test Scenario**

Resize the browser window to simulate mobile view. Verify the UI remains usable on small screens. Test that all controls are accessible and the graph is still navigable.

Try the app on a mobile device to verify the responsiveness and the user experience.

**Automation**

Manual test.

## Bugs & Test Scenarios

No bugs, for now :)
