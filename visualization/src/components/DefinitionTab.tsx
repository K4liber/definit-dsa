import { useRef, useEffect } from 'react';
import type { DefNode } from '../types';
import { learnStateForNode, renderMdToHtml } from '../lib/graph';

type Props = {
  node: DefNode | null;
  renderedNodes: DefNode[];
  learned: Set<string>;
  onMarkLearned: (id: string) => void;
  onDepClick: (id: string) => void;
};

const DefinitionTab: React.FC<Props> = ({ node, renderedNodes, learned, onMarkLearned, onDepClick }) => {
  const bodyRef = useRef<HTMLDivElement>(null);

  // Bind dep click handlers after rendering HTML
  useEffect(() => {
    if (!bodyRef.current) return;
    const els = bodyRef.current.querySelectorAll<HTMLElement>('span.dep[data-dep]');
    els.forEach((el) => {
      el.onclick = (ev) => {
        ev.preventDefault();
        ev.stopPropagation();
        const id = el.dataset.dep;
        if (id) onDepClick(id);
      };
    });
  });

  if (!node) {
    return (
      <div className="panelSection viewer" data-testid="definition-tab-empty">
        <h3>Content</h3>
        <div className="viewerBody">
          <p style={{ margin: 0, color: '#a9b4c0' }}>Select a definition to show the content.</p>
        </div>
      </div>
    );
  }

  const state = learnStateForNode(node, learned);
  const isReady = state === 'ready';
  const isLearned = state === 'learned';
  const html = renderMdToHtml(node.content || '(no content)', node.deps ?? [], renderedNodes);

  return (
    <div className="panelSection viewer" data-testid="definition-tab">
      <h3 data-testid="definition-title">{node.title}</h3>
      <div
        className="path"
        data-testid="definition-category"
        style={{ display: 'block' }}
      >
        {node.category}
      </div>
      <div
        ref={bodyRef}
        className="viewerBody"
        data-testid="definition-body"
        dangerouslySetInnerHTML={{ __html: html }}
      />
      <div className="viewerActions">
        {!isLearned && (
          <button
            className="btn"
            data-testid="mark-learned-button"
            aria-label={`Mark ${node.title} as learned`}
            disabled={!isReady}
            onClick={() => onMarkLearned(node.id)}
          >
            Mark as learned
          </button>
        )}
      </div>
    </div>
  );
};

export default DefinitionTab;
