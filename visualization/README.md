# DefinIT - Data Structures and Algorithms — Visualization

This folder contains a small TypeScript + Vite + D3 app that visualizes the definitions database as a **directed acyclic graph (DAG)** arranged in **concentric circles** (radial levels).

- **Level 0 (inner ring)**: definitions with **no dependencies**
- **Level N**: definitions that depend (directly or indirectly) on lower levels

The graph data is generated from the following markdown files:
- `src/definit_db/data_md/index.md` (list of all definitions)
- `src/definit_db/data_md/definitions/**.md` (definition content, used to extract dependencies)

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

## Interactive behavior

### Progress + learning

- Nodes are rendered in concentric rings/levels.
- Learning state is persisted in the browser (via `localStorage`).

**Focus** behavior:

- Recomputes the suggested visibility selection from the current learning progress (same as a fresh load with no stored selection).
- Then **automatically selects the next ready-to-learn definition** and opens it in the **Definition** tab.

### Search

Use the “Search node by id/title…” input to highlight matching nodes.

- Matching is performed against the node `id` (which equals the definition `category`) and title.
- Matches are indicated by a red outline around the node.

### Selection + focus + viewer

- **Hover** highlights the hovered node’s ring/level.
- **Left click** selects a node and focuses/centers the view on its ring/level.
- Selecting a node loads its markdown and shows it in the bottom panel **Definition** tab.

Selection can be triggered either manually (clicking in the graph / Categories) or automatically (startup / Focus). In all cases it behaves the same: the graph is focused on the selected node’s ring and the definition content is shown.

### Initial view / starting focus

On startup (and when entering **Focus**), if there is no already-selected definition, the app will pick the **next ready-to-learn** definition and select it immediately.

The “next” definition is chosen from all definitions in the rendered graph that are **ready-to-learn**, sorted by:

1. **Definition level** (`L#`)
2. **Parent category level** (topological level of the definition’s immediate parent folder)
3. Stable tie-breaker (definition id)

If **no** definitions are ready-to-learn, the app falls back to focusing the highest ring/level that contains at least one node that is **ready-to-learn** or **already-learned**.

## Learning states

### Node states and colors

Definition nodes (leaves) are colored by learning/progress state:

- **Off**: *barely visible* gray (high transparency)
- **Visible**: gray
- **Ready-to-learn**: yellow
- **Already-learned**: green

### State rules

- A node is **already-learned** once you explicitly mark it as learned.
- A node is **ready-to-learn** when **all of its dependencies are already-learned** (nodes with no dependencies are ready).
- A node is **visible** when it is **not learned**, **not ready**, and has **at least one incoming “on” edge**.
- Otherwise the node is **off**.

Learned state is persisted in the browser (via `localStorage`).

### Off node label fading

For nodes in the **off** state, the **label text is also faded** (lower opacity), so the background graph is present but unobtrusive.

### Mark as learned

When a definition is open, you will see a **“Mark as learned”** button.

- It is enabled only when the current node is **ready-to-learn**.
- Clicking it marks that node as **already-learned** and updates the graph.

### Reset progress

**Reset progress** clears the learned set from memory and browser storage, re-renders the graph, and re-applies the initial focus behavior.

## Edges

### Direction / meaning

Each edge is `source -> target`, meaning:

- **source depends on target**
- `target` is a prerequisite for `source`

### Styling

- Edges are rendered as **curved paths** (they arc inward toward the center).
- Edges are styled based on the **prerequisite node** (`target`) state:
  - **On edge**: prerequisite is **learned** (more visible)
  - **Off edge**: prerequisite is **not learned** (still visible but subtler, typically dashed)

## UI description

The visualization UI is designed to work well on both desktop and mobile.

### Layout overview

The UI is split into three vertical regions:

- **Top menu**: primary view controls (Focus / Overview / Reset progress)
- **Main panel**
  - **Graph canvas** (SVG visualization)
  - **Bottom panel** (details)
    - Expanded: graph and bottom panel share height (50/50 split)
    - Collapsed: graph uses full height
- **Bottom controls**: panel toggle (▲/▼) and the Search input

### Bottom panel contents (tabs)

- **Definition** tab: selected definition content + “Mark as learned” action
- **Categories** tab: folder-like tree with visibility (include/exclude) checkboxes
- **Graph** tab: statistics of the currently rendered graph

### Persistence

The UI persists state in `localStorage`:

- Bottom panel collapsed/expanded state
- Learned definitions
- Categories expand/collapse state
- Categories/definitions visibility (include) selection

## Categories tab

Between the **Definition** tab and the **Graph** tab there is a **Categories** tab.

It is an Explorer-like tree:

- Category folders are derived from definition ids (split by `/`).
- Folders can be expanded/collapsed (including top-level “fields”).
- Leaf rows list definitions and show:
  - a state dot color (ready/learned/visible/off)
  - the definition level (`L#`).
- Definitions inside a category are sorted by:
  1) state: **ready** (yellow), **learned** (green), **visible**, **off**
  2) level
  3) title

### Visibility (include/exclude) checkboxes

Each folder and each definition has a checkbox:

- **Checked = included** in the rendered graph.
- Unchecking a **folder** includes/excludes *all definitions under that category*.
- When the graph is filtered by checkboxes, **levels are recomputed** on the *rendered* graph.
- Learning state rules **do not change** with visibility:
  - A definition is **ready** when **all of its dependencies are learned**, even if some dependencies are currently hidden by checkboxes.

### Category ordering and levels

Categories are treated as a DAG and are **topologically sorted** (by computed group level).

- Each folder row shows a computed folder level (`L#`).
- The visualization assumes categories are acyclic (if a dependency implies `A -> B` at some category depth, then the reverse is not expected).

### Default selection behavior (auto-selection)

The checkbox selection is persisted, but there are moments where the app recomputes a “suggested” selection from the current learning progress:

- **On page load**: if there is **no stored selection**, the app derives the selection from the current **ready-to-learn** nodes.
- **After “Mark as learned”**: the app recomputes and **overwrites** the stored selection so the visible graph follows the newly-unlocked readiness.
- **On “Focus”**: the app recomputes and **overwrites** the stored selection the same way (equivalent to a fresh load with no stored selection).

The auto-selection targets the *specific immediate parent categories* of ready definitions (it does **not** bubble readiness to ancestor prefixes/fields).
