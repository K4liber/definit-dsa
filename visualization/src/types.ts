export type DefNode = {
  /**
   * Unique id used throughout the visualization.
   */
  id: string;

  title: string;

  category: string;

  /** dependency ids (ids resolve to categories) */
  deps: string[];

  /**
   * Dynamic layout level (computed in the UI on the current projected graph).
   * Not persisted in defs.json.
   */
  level?: number;

  /** Preloaded markdown content for viewer */
  content: string;
};

export type DefGraph = {
  nodes: DefNode[];
  edges: Array<{ source: string; target: string }>; // source -> target (source depends on target)
};

// --- UI / visualization internal types ---

export type Pos = { x: number; y: number };

export type LearnState = 'off' | 'visible' | 'ready' | 'learned';

export type Raw = {
  def: DefGraph;
  byId: Map<string, DefNode>;
  childrenByPrefix: Map<string, string[]>; // prefix -> ids under that prefix
  fields: string[]; // top-level fields (e.g. mathematics, computer_science)
};

export type UIState = {
  selectedLeaf?: string; // leaf id
};

export type TreeNode = {
  id: string; // prefix (group) or leaf id
  name: string;
  kind: 'group' | 'leaf';
  depth: number;
  children: TreeNode[];
  // leaf metadata
  leaf?: DefNode;
  // group metadata
  groupLevel?: number;
};

export type BottomTab = 'definition' | 'categories' | 'graph';
