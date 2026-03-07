import { useEffect, useCallback } from 'react';
import { INFO_TEXT } from '../lib/constants';

type Props = {
  open: boolean;
  onClose: () => void;
};

const InfoModal: React.FC<Props> = ({ open, onClose }) => {
  const handleKeyDown = useCallback(
    (ev: KeyboardEvent) => {
      if (ev.key === 'Escape' && open) onClose();
    },
    [open, onClose],
  );

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);

  return (
    <div
      className={`infoOverlay ${open ? 'open' : ''}`}
      role="dialog"
      aria-modal="true"
      onClick={(ev) => {
        if (ev.target === ev.currentTarget) onClose();
      }}
    >
      <div className="infoModal">
        <div className="infoHeader">
          <h2>Info</h2>
          <button className="infoClose" onClick={onClose}>
            Close
          </button>
        </div>
        <div className="infoBody">{INFO_TEXT}</div>
      </div>
    </div>
  );
};

export default InfoModal;
