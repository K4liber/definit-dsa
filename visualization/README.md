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


## Troubleshooting

### “Cycle detected …” during `npm run gen:data`

The generator enforces DAG constraints. A cycle error usually comes from one of:

- A real cycle in the underlying definition dependencies
- A **false-positive dependency** (most common), e.g. a definition linking to itself or using a generic markdown link that looks like a dependency.

The generator tries to reduce false positives by:

- Ignoring self-dependencies
- Only keeping dependencies that exist in `index.md`


## Features & Test Scenarios

### # **Data Generation from Markdown**

**Importance**: Critical

**Test Scenario**

Run `npm run gen:data` and verify `public/defs.json` is created correctly. Verify the file contains all definitions from markdown source files.

### # **Cycle Detection in Generator**

**Importance**: Critical

**Test Scenario**

Run `npm run gen:data` with valid dependencies and verify successful generation. Introduce a cycle in test data and verify the generator fails with a cycle detection error message.

### # **Layout overview**

**Importance**: Critical

**Test Scenario**

The UI is split into three vertical regions:

- **Top menu**: primary view controls (Focus / Overview / Reset progress) and the info button
- **Main panel**
  - **Graph canvas** (SVG visualization)
  - **Bottom panel** (details)
    - Expanded: graph and bottom panel share height (50/50 split)
    - Collapsed: graph uses full height
- **Bottom controls**: panel toggle (▲/▼) and the Search input

### # **Bottom panel contents (tabs)**

**Importance**: Critical

**Test Scenario**

- **Definition** tab: 
1) selected definition content
2) “Mark as learned” action
3) Clickable dependencies in the content.
- **Categories** tab: folder-like tree with visibility (include/exclude) checkboxes
- **Progress** tab: overall learning progress:
1) definitions learned
2) edges unlocked
3) levels completed

### # **Categories tab details**

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

### # **Graph canvas display**

**Importance**: Critical

**Test Scenario**

Verify that the graph renders all definitions from `defs.json` without cycles. Ensure dependencies are correctly represented as directed edges where source depends on target.

### # **Graph canvas radial levels**

**Importance**: Critical

**Test Scenario**

Verify that definitions are arranged in concentric rings by level. Level 0 should contain only definitions with no dependencies. Each subsequent level should contain definitions whose all dependencies exist in lower levels.

### # **Mark Definition as Learned**

**Importance**: Critical

**Test Scenario**

Open a definition with all dependencies learned, verify "Mark as learned" button is enabled. Click it, confirm the node becomes green, and the graph is updated. Try to mark a definition without all dependencies learned and verify the button is disabled.

After definition has been marked, we should switch to the next ready-to-learn definition if it exists

### # **Learning State Persistence (localStorage)**

**Importance**: Critical

**Test Scenario**

Mark nodes as learned, reload the page, and verify that the learned states are restored from browser storage. Clear localStorage and verify the app resets to initial state.

### # **Dependency-Based Learning Readiness**

**Importance**: Critical

**Test Scenario**

Verify that a node is marked as "ready-to-learn" (yellow) only when all of its dependencies are marked as learned. Mark a dependency as learned and verify dependent nodes transition to ready state.

### # **Tree Explorer on categories tab**

**Importance**: Critical

**Test Scenario**

Expand and collapse category folders in the Categories tab. Verify that leaf definitions display state dots (ready/learned/visible/off) and levels. Confirm definitions are sorted by state first, then level, then title.

### # **Checkboxes behavior on categories tab**

**Importance**: Critical

**Test scenarios**

Each folder and each definition has a checkbox:

- **Checked = included** in the rendered graph.
- Unchecking a **folder** includes/excludes *all definitions under that category*.
- When the graph is filtered by checkboxes, **levels are recomputed** on the *rendered* graph.
- Learning state rules **do not change** with visibility:
  - A definition is **ready** when **all of its dependencies are learned**, even if some dependencies are currently hidden by checkboxes.

### # **Search & Node Highlighting**

**Importance**: High

**Test Scenario**

Use the search input to query by node ID and title. Verify that matching nodes are highlighted with a red outline. Test partial matches and verify search works for both category IDs and titles.

### # **Node Click - Focus & Center View**

**Importance**: High

**Test Scenario**

Click on a definition node and verify the view centers/focuses on that node's ring/level. Verify that clicking different nodes updates the viewport accordingly.

### # **Node Hover - Level Ring Highlight**

**Importance**: High

**Test Scenario**

Hover over a node and verify that its entire ring/level is highlighted. Move to another node and verify the highlight updates.

### # **Learning State Rules**

**Importance**: High

**Test Scenario**

- A node is **already-learned** once you explicitly mark it as learned.
- A node is **ready-to-learn** when **all of its dependencies are already-learned** (nodes with no dependencies are ready).
- A node is **visible** when it is **not learned**, **not ready**, and has **at least one incoming “on” edge**.
- Otherwise the node is **off**.

Verify that node colors reflect states correctly: **Off** (faded gray), **Visible** (gray), **Ready-to-learn** (yellow), **Already-learned** (green). Transition nodes between states and verify colors update.

### # **Initial View Focus on Next Ready-to-Learn Node**

**Importance**: High

**Test Scenario**

On app startup, verify the view automatically focuses on the next ready-to-learn definition if it exists.

### # **Category Topological Sorting**

**Importance**: High

**Test Scenario**

Verify that category folders are displayed in topologically sorted order by their computed level. Confirm folder levels are correctly computed and displayed.

### # **Bottom Panel Collapse/Expand Toggle**

**Importance**: High

**Test Scenario**

Click the panel toggle (▲/▼) to expand/collapse the bottom panel. Verify the collapsed state saves to localStorage. Reload the page and confirm the state persists.

### # **Edge Styling Based on Prerequisite State**

**Importance**: Medium

**Test Scenario**

Verify that edges connecting to learned prerequisites are rendered as **on edges** (more visible). Edges to unlearned prerequisites are **off edges** (dashed or subtler).

### # **Curved Edge Paths (Arc Toward Center)**

**Importance**: Medium

**Test Scenario**

Verify that all edges are rendered as curved paths that arc inward toward the center rather than straight lines. Check visual rendering for aesthetic quality.

### # **Responsive UI Design (Desktop & Mobile)**

**Importance**: Medium

**Test Scenario**

Resize the browser window to simulate mobile view. Verify the UI remains usable on small screens. Test that all controls are accessible and the graph is still navigable.

### # **Category Expand/Collapse Persistence**

**Importance**: Low

**Test Scenario**

Expand and collapse category folders, reload the page, and verify the expand/collapse state is restored from localStorage.
