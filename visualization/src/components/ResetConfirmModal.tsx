import { useEffect, useCallback } from 'react';

type Props = {
  open: boolean;
  onConfirm: () => void;
  onCancel: () => void;
};

const ResetConfirmModal: React.FC<Props> = ({ open, onConfirm, onCancel }) => {
  const handleKeyDown = useCallback(
    (ev: KeyboardEvent) => {
      if (ev.key === 'Escape' && open) onCancel();
    },
    [open, onCancel],
  );

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);

  return (
    <div
      className={`dangerOverlay ${open ? 'open' : ''}`}
      role="dialog"
      aria-modal="true"
      onClick={(ev) => {
        if (ev.target === ev.currentTarget) onCancel();
      }}
    >
      <div className="dangerModal">
        <div className="dangerHeader">
          <h2>Reset progress?</h2>
          <button className="infoClose" onClick={onCancel}>
            Close
          </button>
        </div>
        <div className="dangerBody">
          This will remove all "learned" markers and return every definition to the initial state.
          {'\n\n'}
          This action cannot be undone.
        </div>
        <div className="dangerActions">
          <button className="btn" onClick={onCancel}>
            Cancel
          </button>
          <button className="btnDanger" onClick={onConfirm}>
            Reset
          </button>
        </div>
      </div>
    </div>
  );
};

export default ResetConfirmModal;
