export type DefNode = {
  /**
   * Unique id used throughout the visualization, in the `<field>/<name>` form.
   */
  id: string;

  title: string;

  /** Common alternative names, extracted from the serialized heading. */
  aliases?: string[];

  /** dependency ids */
  deps: string[];

  /**
   * Level used for the radial ring layout. Mirrors `absLevel` (assigned in
   * `renderGraph` from the absolute value); recomputed only by `buildRaw`
   * on the full database graph. Never reflects a filtered subgraph.
   */
  level?: number;

  /**
   * Absolute level in the full database graph (longest dependency chain
   * below the definition). Computed once in `buildRaw`, preserved through
   * filtering, and used for both display and ring placement. Readiness is
   * always computed from full `deps`, never from visibility.
   */
  absLevel?: number;

  /** Preloaded markdown content for viewer */
  content: string;
};

export type DefGroup = {
  id: string;
  name: string;
  definitions: string[];
};

export type DefGraph = {
  nodes: DefNode[];
  edges: Array<{ source: string; target: string }>; // source -> target (source depends on target)
  groups?: DefGroup[];
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
