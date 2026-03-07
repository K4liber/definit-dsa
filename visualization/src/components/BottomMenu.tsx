type Props = {
  panelCollapsed: boolean;
  searchQuery: string;
  onTogglePanel: () => void;
  onSearchChange: (q: string) => void;
};

const BottomMenu: React.FC<Props> = ({
  panelCollapsed,
  searchQuery,
  onTogglePanel,
  onSearchChange,
}) => {
  return (
    <div className="bottomMenu">
      <button
        className="btn"
        aria-expanded={!panelCollapsed}
        aria-label="Toggle bottom panel"
        onClick={onTogglePanel}
      >
        {panelCollapsed ? '▲' : '▼'}
      </button>
      <input
        type="text"
        placeholder="Search node by id/title..."
        value={searchQuery}
        onChange={(e) => onSearchChange(e.target.value)}
      />
    </div>
  );
};

export default BottomMenu;
