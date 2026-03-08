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

### #1 **Data Generation from Markdown**

**Importance**: Critical

**Test Scenario**

Run `npm run gen:data` and verify `public/defs.json` is created correctly. Verify the file contains all definitions from markdown source files.

### #2 **Cycle Detection in Generator**

**Importance**: Critical

**Test Scenario**

Run `npm run gen:data` with valid dependencies and verify successful generation. Introduce a cycle in test data and verify the generator fails with a cycle detection error message.

### #3 **Layout overview**

**Importance**: Critical

**Test Scenario**

The UI is split into three vertical regions:

- **Top menu**: primary view controls (Focus / Overview / Reset progress) and the info button
- **Graph canvas** (SVG visualization)
- **Bottom panel**
  - Expanded: graph and bottom panel share height (50/50 split)
  - Collapsed: graph uses full height and only the tab names are visible

### #4 **Bottom Panel Collapse/Expand Toggle**

**Importance**: High

**Test Scenario**

Click on any tab name to expand the bottom panel. Click again on the same tab to collapse it. Verify that the collapsed state is saved to localStorage and persists after page reload.

### #5 **Bottom panel contents (tabs)**

**Importance**: Critical

**Test Scenario**

- **Definition** tab: 
1) selected definition content
2) “Mark as learned” action
3) Clickable dependencies in the content.
- **Filters** tab: 
1) Definition descendants filter: render a selected definition with all of its descendants that are needed to be learned before the selected definition can be learned.
2) Categories filter: folder-like tree with visibility (include/exclude) checkboxes
3) Node state filters (checkboxes)
- **Progress** tab: learning progress on the currently rendered graph:
1) definitions learned
2) edges unlocked
3) levels completed

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

### #7 **Checkboxes behavior on categories filter**

**Importance**: Critical

**Test scenarios**

Each folder (or category) and each definition has a checkbox:

- **Checked = included** in the rendered graph.
- Unchecking a **folder** includes/excludes *all definitions under that category*.
- When the graph is filtered by checkboxes, **levels are recomputed** on the *rendered* graph.
- Learning state rules **do not change** with visibility:
  - A definition is **ready** when **all of its dependencies are learned**, even if some dependencies are currently hidden by checkboxes.

Expand and collapse category folders, reload the page, and verify the expand/collapse state is restored from localStorage.

### #8 **Search filter**

**Importance**: High

**Test Scenario**

Use the search input to query by node ID and title. After putting a character in a search input we should see a checkable list of all definitions that match with the current content of the input. User should be able to click on an element in the list and in such a case this is our new content of the input. User can only select a single element so the input can hold only one node (or zero) at any time. 

After a definition is selected, we should filter all definitions (from raw graph) and only select those who are either the selected node or any descendant. Finally, the user should only see a graph for a selected definition with all descendants that are needed to be learned before the selected definition can be learned.

### #9 **Learning State Rules**

**Importance**: High

**Test Scenario**

- A node is **already-learned** once you explicitly mark it as learned.
- A node is **ready-to-learn** when **all of its dependencies are already-learned** (nodes with no dependencies are ready).
- A node is **pre-ready-to-learn** when it is **not learned**, **not ready**, and has **at least one incoming “on” edge**.
- Otherwise the node is **not-ready-to-learn**.

Verify that node colors reflect states correctly: **Not-ready-to-learn** (faded gray), **Pre-ready-to-learn** (gray), **Ready-to-learn** (yellow), **Already-learned** (green). Transition nodes between states and verify colors update.

### #10 **Node state filters**

**Importance**: High

**Test Scenario**

There are 4 states for definitions:
- **Not-ready-to-learn**: filtered on default.
- **Pre-ready-to-learn**: shown on default.
- **Ready-to-learn**: shown on default.
- **Already-learned**: shown on default.

Check if state filters (checkboxes) correctly include/exclude nodes of each state from the rendered graph. Verify that filtering by state updates the graph and levels accordingly.

### #11 **Graph canvas display**

**Importance**: Critical

**Test Scenario**

Verify that the graph renders all definitions from `defs.json`. Ensure dependencies are correctly represented as directed edges where source depends on target.

### #12 **Graph canvas radial levels**

**Importance**: Critical

**Test Scenario**

Verify that definitions are arranged in concentric rings by level. Level 0 should contain only definitions with no dependencies. Each subsequent level should contain definitions whose all dependencies exist in lower levels.

### #13 **Dependency-Based Learning Readiness**

**Importance**: Critical

**Test Scenario**

Verify that a node is marked as "ready-to-learn" (yellow) only when all of its dependencies are marked as learned.

### #14 **Mark Definition as Learned**

**Importance**: Critical

**Test Scenario**

Open a Definition tab for a "ready-to-learn" definition, verify "Mark as learned" button is enabled. Click it, confirm the node becomes green, and progress inside "Progress" tab is updated. Confirm that the other definition states are updated accordingly.

Try to mark a definition without all dependencies learned and verify the button is disabled.

After definition has been marked, we should experience a switch to the next ready-to-learn definition if it exists

### #15 **Learning State Persistence (localStorage)**

**Importance**: Critical

**Test Scenario**

Mark nodes as learned, reload the page, and verify that the learned states are restored from browser storage. Clear localStorage and verify the app resets to initial state.

### #16 **Node Click - Focus & Center View**

**Importance**: High

**Test Scenario**

Click on a definition node and verify the view centers/focuses on that node's ring/level. Verify that clicking different nodes updates the viewport accordingly.

### #17 **Node Hover - Level Ring Highlight**

**Importance**: High

**Test Scenario**

Hover over a node and verify that its entire ring/level is highlighted. Move to another node and verify the highlight updates.

### #18 **Initial View Focus on Next Ready-to-Learn Node**

**Importance**: High

**Test Scenario**

On app startup, verify the view automatically focuses on the next ready-to-learn definition if it exists. Also the "Definition" tab for that definition should be open.

### #19 **Edge Styling Based on Prerequisite State**

**Importance**: Medium

**Test Scenario**

Verify that edges connecting to learned prerequisites are rendered as **on edges** (more visible). Edges to unlearned prerequisites are **off edges** (dashed or subtler).

### #20 **Curved Edge Paths (Arc Toward Center)**

**Importance**: Medium

**Test Scenario**

Verify that all edges are rendered as curved paths that arc inward toward the center rather than straight lines. Check visual rendering for aesthetic quality.

### #21 **Responsive UI Design (Desktop & Mobile)**

**Importance**: Medium

**Test Scenario**

Resize the browser window to simulate mobile view. Verify the UI remains usable on small screens. Test that all controls are accessible and the graph is still navigable.

Try the app on a mobile device to verify the responsiveness and the user experience.

## Bugs & Test Scenarios

### #1 **Not all dependencies are clickable**

**Importance**: High

**Test Scenario**

In k_ary_tree definition we do not have a clickable dependency to n-ary-tree definition.
