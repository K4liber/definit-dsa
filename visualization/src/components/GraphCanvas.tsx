import { useEffect, useRef, useCallback, useImperativeHandle, forwardRef } from 'react';
import * as d3 from 'd3';
import type { DefGraph, DefNode, LearnState } from '../types';
import {
  radialLayout,
  computeLevels,
  learnStateForNode,
  colorForLearnState,
  computeVisibleSet,
  type RadialLayout,
} from '../lib/graph';

export type GraphCanvasHandle = {
  focusRing: (level: number) => void;
  focusRingOfNode: (id: string) => void;
  focusHighestActiveRing: () => void;
};

type Props = {
  graph: DefGraph | null;
  learned: Set<string>;
  selectedNodeId: string | null;
  onNodeClick: (id: string) => void;
};

const GraphCanvas = forwardRef<GraphCanvasHandle, Props>(
  ({ graph, learned, selectedNodeId, onNodeClick }, ref) => {
    const svgRef = useRef<SVGSVGElement>(null);
    const gRootRef = useRef<d3.Selection<SVGGElement, unknown, null, undefined> | null>(null);
    const gRingsRef = useRef<d3.Selection<SVGGElement, unknown, null, undefined> | null>(null);
    const gLinksRef = useRef<d3.Selection<SVGGElement, unknown, null, undefined> | null>(null);
    const gNodesRef = useRef<d3.Selection<SVGGElement, unknown, null, undefined> | null>(null);
    const zoomRef = useRef<d3.ZoomBehavior<SVGSVGElement, unknown> | null>(null);
    const layoutRef = useRef<RadialLayout | null>(null);
    const graphRef = useRef<DefGraph | null>(null);
    const hoveredLevelRef = useRef<number | null>(null);

    const W = useCallback(() => svgRef.current?.clientWidth ?? 800, []);
    const H = useCallback(() => svgRef.current?.clientHeight ?? 600, []);

    // Initialize SVG groups and zoom
    useEffect(() => {
      if (!svgRef.current) return;
      const svg = d3.select(svgRef.current);

      // Clear any previous content
      svg.selectAll('*').remove();

      const gRoot = svg.append('g');
      const gRings = gRoot.append('g').attr('class', 'rings');
      const gLinks = gRoot.append('g').attr('class', 'links');
      const gNodes = gRoot.append('g').attr('class', 'nodes');

      gRootRef.current = gRoot;
      gRingsRef.current = gRings;
      gLinksRef.current = gLinks;
      gNodesRef.current = gNodes;

      const zoom = d3
        .zoom<SVGSVGElement, unknown>()
        .scaleExtent([0.1, 6])
        .on('zoom', (ev: d3.D3ZoomEvent<SVGSVGElement, unknown>) => {
          gRoot.attr('transform', ev.transform.toString());
        });

      svg.call(zoom);
      zoomRef.current = zoom;
    }, []);

    const applyRingHighlight = useCallback(() => {
      const gRings = gRingsRef.current;
      if (!gRings) return;

      let level: number | null = hoveredLevelRef.current;

      if (level === null && selectedNodeId && graphRef.current) {
        const n = graphRef.current.nodes.find((x) => x.id === selectedNodeId);
        level = n?.level ?? null;
      }

      gRings
        .selectAll<SVGCircleElement, { level: number; r: number }>('circle.ring')
        .classed('hovered', (d) => level !== null && d.level === level);
    }, [selectedNodeId]);

    const focusRing = useCallback(
      (level: number) => {
        if (!svgRef.current || !zoomRef.current || !layoutRef.current) return;
        const layout = layoutRef.current;
        const r = layout.base + level * layout.ringGap;
        const pad = 60;
        const width = W();
        const height = H();
        const diameter = 2 * r + pad;
        const scale = Math.max(0.12, Math.min(6, Math.min(width / diameter, height / diameter)));
        const tx = width / 2 - layout.cx * scale;
        const ty = height / 2 - layout.cy * scale;

        const svg = d3.select(svgRef.current);
        svg
          .transition()
          .duration(650)
          .call(
            zoomRef.current.transform as any,
            d3.zoomIdentity.translate(tx, ty).scale(scale),
          );
      },
      [W, H],
    );

    const focusRingOfNode = useCallback(
      (id: string) => {
        if (!graphRef.current) return;
        const n = graphRef.current.nodes.find((x) => x.id === id);
        if (n) focusRing(n.level ?? 0);
      },
      [focusRing],
    );

    const focusHighestActiveRing = useCallback(() => {
      if (!graphRef.current) return;
      const g = graphRef.current;
      const maxLevel = Math.max(0, ...g.nodes.map((n) => n.level ?? 0));
      let best = maxLevel;
      for (let level = maxLevel; level >= 0; level--) {
        const has = g.nodes.some((n) => {
          if ((n.level ?? 0) !== level) return false;
          const s = learnStateForNode(n, learned);
          return s === 'ready' || s === 'learned';
        });
        if (has) {
          best = level;
          break;
        }
      }
      focusRing(best);
      hoveredLevelRef.current = best;
      applyRingHighlight();
    }, [learned, focusRing, applyRingHighlight]);

    useImperativeHandle(ref, () => ({
      focusRing,
      focusRingOfNode,
      focusHighestActiveRing,
    }), [focusRing, focusRingOfNode, focusHighestActiveRing]);

    // Draw graph whenever graph or learned changes
    useEffect(() => {
      if (!graph || !gRingsRef.current || !gLinksRef.current || !gNodesRef.current) return;

      const gRings = gRingsRef.current;
      const gLinks = gLinksRef.current;
      const gNodes = gNodesRef.current;

      graphRef.current = graph;

      computeLevels(graph.nodes);

      const width = W();
      const height = H();
      const layout = radialLayout(graph, width, height);
      layoutRef.current = layout;

      const visibleNodeIds = computeVisibleSet(graph, learned);

      // Rings
      const ringData = d3.range(0, layout.maxLevel + 1).map((level: number) => ({
        level,
        r: layout.base + level * layout.ringGap,
      }));

      gRings
        .selectAll<SVGCircleElement, { level: number; r: number }>('circle.ring')
        .data(ringData, (d) => String(d.level))
        .join((enter) => enter.append('circle').attr('class', 'ring'))
        .attr('cx', layout.cx)
        .attr('cy', layout.cy)
        .attr('r', (d) => d.r);

      applyRingHighlight();

      // Edges
      type Edge = { source: string; target: string };

      const edgePath = (d: Edge) => {
        const s = layout.pos.get(d.source);
        const t = layout.pos.get(d.target);
        if (!s || !t) return '';
        const mx = (s.x + t.x) / 2;
        const my = (s.y + t.y) / 2;
        const k = 0.55;
        const cx = mx + (layout.cx - mx) * k;
        const cy = my + (layout.cy - my) * k;
        return `M${s.x},${s.y} Q${cx},${cy} ${t.x},${t.y}`;
      };

      const byId = new Map(graph.nodes.map((n) => [n.id, n] as const));

      const linkSel = gLinks
        .selectAll<SVGPathElement, Edge>('path.link')
        .data(graph.edges as Edge[], (d) => `${d.source}->${d.target}`)
        .join((enter) =>
          enter
            .append('path')
            .attr('class', 'link')
            .attr('fill', 'none')
            .attr('stroke-linecap', 'round')
            .attr('stroke-linejoin', 'round'),
        );

      linkSel
        .attr('d', edgePath)
        .classed('link-on', (d) => {
          const prereq = byId.get(d.target);
          const s = prereq ? learnStateForNode(prereq, learned) : 'not-ready';
          return s === 'learned';
        })
        .classed('link-off', (d) => {
          const prereq = byId.get(d.target);
          const s = prereq ? learnStateForNode(prereq, learned) : 'not-ready';
          return s !== 'learned';
        })
        .attr('stroke', (d) => {
          const prereq = byId.get(d.target);
          const s = prereq ? learnStateForNode(prereq, learned) : 'not-ready';
          return s === 'learned' ? 'rgba(226, 232, 240, 0.85)' : 'rgba(148, 163, 184, 0.16)';
        })
        .attr('stroke-width', (d) => {
          const prereq = byId.get(d.target);
          const s = prereq ? learnStateForNode(prereq, learned) : 'not-ready';
          return s === 'learned' ? 2.2 : 1.0;
        })
        .attr('stroke-dasharray', (d) => {
          const prereq = byId.get(d.target);
          const s = prereq ? learnStateForNode(prereq, learned) : 'not-ready';
          return s === 'learned' ? null : '3 5';
        })
        .attr('opacity', 1);

      // Nodes
      const fillFor = (d: DefNode) => {
        const base = learnStateForNode(d, learned);
        const s: LearnState = base === 'not-ready' && visibleNodeIds.has(d.id) ? 'pre-ready' : base;
        return colorForLearnState(s);
      };

      const stateFor = (d: DefNode): LearnState => {
        const base = learnStateForNode(d, learned);
        return base === 'not-ready' && visibleNodeIds.has(d.id) ? 'pre-ready' : base;
      };

      const nodeSel = gNodes
        .selectAll<SVGGElement, DefNode>('g.node')
        .data(graph.nodes, (d) => d.id)
        .join((enter) => {
          const g = enter.append('g').attr('class', 'node');
          g.append('circle').attr('class', 'node-circle').attr('r', 8);
          g.append('circle').attr('class', 'leaf-underline').attr('r', 15);
          g.append('text').attr('dx', 12).attr('dy', 5);
          g.append('title');
          return g;
        });

      nodeSel
        .select('title')
        .text((d: DefNode) => `${d.title} (level: ${d.level ?? 0})\n${d.category}`);

      nodeSel
        .on('mouseenter', (ev: MouseEvent, d: DefNode) => {
          d3.select(ev.currentTarget as SVGGElement).classed('hovering', true);
          hoveredLevelRef.current = d.level ?? 0;
          applyRingHighlight();
        })
        .on('mouseleave', (ev: MouseEvent) => {
          d3.select(ev.currentTarget as SVGGElement).classed('hovering', false);
          hoveredLevelRef.current = null;
          applyRingHighlight();

          if (selectedNodeId) {
            gNodes
              .selectAll<SVGGElement, DefNode>('g.node')
              .filter((n) => n.id === selectedNodeId)
              .classed('hovering', true);
          }
        })
        .on('click', (ev: MouseEvent, d: DefNode) => {
          ev.preventDefault();
          ev.stopPropagation();
          onNodeClick(d.id);
        });

      if (selectedNodeId) {
        gNodes
          .selectAll<SVGGElement, DefNode>('g.node')
          .classed('hovering', (n) => hoveredLevelRef.current === null && n.id === selectedNodeId);
      }

      nodeSel.attr('transform', (d) => {
        const p = layout.pos.get(d.id)!;
        return `translate(${p.x},${p.y})`;
      });

      nodeSel
        .select<SVGCircleElement>('circle.node-circle')
        .attr('fill', fillFor)
        .attr('opacity', 1);

      nodeSel
        .select<SVGCircleElement>('circle.leaf-underline')
        .attr('fill', 'none')
        .attr('stroke', fillFor)
        .attr('stroke-width', 2)
        .attr('opacity', 0.9);

      nodeSel
        .select('text')
        .text((d: DefNode) => d.title)
        .attr('fill', '#e6edf3')
        .attr('opacity', (d: DefNode) => (stateFor(d) === 'not-ready' ? 0.22 : 1));
    }, [graph, learned, selectedNodeId, onNodeClick, W, H, applyRingHighlight]);

    return (
      <div className="canvasArea">
        <div className="canvasWrap">
          <svg
            ref={svgRef}
            role="img"
            aria-label="Definitions graph"
          />
        </div>
      </div>
    );
  },
);

GraphCanvas.displayName = 'GraphCanvas';

export default GraphCanvas;
