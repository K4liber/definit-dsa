import type React from 'react';

type Props = {
  hasLearned: boolean;
  onFocus: () => void;
  onOverview: () => void;
  onResetProgress: () => void;
};

const TopMenu: React.FC<Props> = ({ hasLearned, onFocus, onOverview, onResetProgress }) => {
  return (
    <div className="topMenu">
      <button className="btn" onClick={onFocus}>
        Focus
      </button>
      <button className="btn" onClick={onOverview}>
        Overview
      </button>
      <button
        className="btn"
        disabled={!hasLearned}
        title={hasLearned ? 'Reset progress' : 'Nothing to reset yet'}
        onClick={onResetProgress}
      >
        Reset progress
      </button>
    </div>
  );
};

export default TopMenu;
