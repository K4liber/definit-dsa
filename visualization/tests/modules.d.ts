declare module '../../scripts/*.mjs' {
  import type { DefGraph } from '../src/types';

  export function generateData(options?: {
    indexPath?: string;
    defsRoot?: string;
    outPath?: string;
  }): Promise<{
    graph: DefGraph;
    stats: { unresolvedHref: number };
    outPath: string;
  }>;
}
