import type { BottomTab } from '../types';

type Props = {
  panelCollapsed: boolean;
  activeTab: BottomTab;
  onTabClick: (tab: BottomTab) => void;
};

const BottomMenu: React.FC<Props> = ({ panelCollapsed, activeTab, onTabClick }) => {
  const mkBtn = (tab: Exclude<BottomTab, null>, label: string) => {
    const isActive = activeTab === tab && !panelCollapsed;
    return (
      <button
        key={tab}
        type="button"
        className={`tabBtn ${isActive ? 'active' : ''}`}
        aria-pressed={isActive}
        onClick={() => onTabClick(tab)}
      >
        {label}
      </button>
    );
  };

  return (
    <div className="bottomMenu" role="toolbar" aria-label="Bottom panel">
      {mkBtn('definition', 'Definition')}
      {mkBtn('filters', 'Filters')}
      {mkBtn('progress', 'Progress')}
    </div>
  );
};

export default BottomMenu;
