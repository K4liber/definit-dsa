export type DefNode = {
  /**
   * Unique id used throughout the visualization, in the `<field>/<name>` form.
   */
  id: string;

  title: string;

  /** dependency ids */
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

export type LearnState = 'not-ready' | 'pre-ready' | 'ready' | 'learned';

export type Raw = {
  def: DefGraph;
  byId: Map<string, DefNode>;
  fields: string[]; // top-level fields (e.g. mathematics, computer_science)
};

export type UIState = {
  selectedLeaf?: string; // leaf id
};

export type FieldGroup = {
  /** Field name, e.g. `mathematics` */
  field: string;

  /** Definitions in this field, sorted for display */
  definitions: DefNode[];
};

export type BottomTab = 'definition' | 'filters' | 'progress' | null;
