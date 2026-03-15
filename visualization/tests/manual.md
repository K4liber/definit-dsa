## Manual test scenarios

### #1 **Category folder checkbox toggles all nested definitions**

**Importance**: Critical

**Manual test scenario**

In the Filters tab, uncheck a category folder and verify that all definitions under that folder disappear from the rendered graph. Check the same folder again and verify that all of its definitions return.

### #2 **Node colors match the four learning states**

**Importance**: High

**Manual test scenario**

Inspect nodes in the graph and verify that each learning state uses the expected color: learned, ready, pre-ready, and not-ready.

### #3 **Graph canvas renders every definition node**

**Importance**: Critical

**Manual test scenario**

Load the app and verify that the graph canvas renders the full set of definition nodes from `defs.json` when no search or filter narrows the dataset.

### #4 **Graph canvas renders dependency directions correctly**

**Importance**: Critical

**Manual test scenario**

Inspect several known prerequisite relationships in the graph and verify that each directed edge connects a definition to its prerequisite in the correct direction.

### #5 **Nodes are arranged into visible concentric level rings**

**Importance**: Critical

**Manual test scenario**

Verify that nodes are visually arranged into concentric rings and that each ring corresponds to a graph level in the SVG canvas.

### #6 **Learned nodes change to the learned color**

**Importance**: Critical

**Manual test scenario**

Mark a ready definition as learned and verify that the corresponding node changes to the learned color in the graph.

### #7 **Clicking a node gives it focus**

**Importance**: High

**Manual test scenario**

Click a definition node and verify that the viewport visually focuses that node and centers its level ring.

### #8 **Clicking a different node updates the visual focus**

**Importance**: High

**Manual test scenario**

After focusing one node, click a different node and verify that the viewport focus updates to the newly selected node.

### #9 **Hovering a node highlights its level ring**

**Importance**: High

**Manual test scenario**

Hover over a definition node and verify that the entire ring for that node's level becomes highlighted.

### #10 **Hover highlight moves when the pointer changes nodes**

**Importance**: High

**Manual test scenario**

Move the pointer from one node to another and verify that the ring highlight follows the hovered node and clears from the previous one.

### #11 **Initial startup view visually focuses the next ready node**

**Importance**: High

**Manual test scenario**

Reload the app with default state and verify that the initial viewport visually focuses the next ready-to-learn node or its ring.

### #12 **Edges style based on prerequisite status**

**Importance**: Medium

**Manual test scenario**

Verify that:
- edges connected to learned prerequisites use the intended active or "on" visual style.
- edges connected to unlearned prerequisites use the intended inactive or "off" visual style, such as a dashed or subtler appearance.

### #13 **Edges are rendered as inward-curving paths**

**Importance**: Medium

**Manual test scenario**

Inspect the graph and verify that edges are drawn as curved paths that arc toward the center rather than as straight line segments.

### #14 **Layout remains usable on a narrow desktop viewport**

**Importance**: Medium

**Manual test scenario**

Resize the browser window to a narrow desktop width and verify that the controls remain usable and the graph stays navigable.

### #15 **Layout remains usable on a mobile device**

**Importance**: Medium

**Manual test scenario**

Open the app on a mobile device or emulator and verify that the interface remains usable and the graph can still be navigated.