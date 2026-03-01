import type { Raw, DefGraph } from '../types';
import { computeStats } from '../lib/graph';

type Props = {
  raw: Raw;
  rendered: DefGraph;
  learned: Set<string>;
};

const ProgressTab: React.FC<Props> = ({ raw, rendered, learned }) => {
  const stats = computeStats(raw, rendered, learned);

  return (
    <div className="panelSection">
      <h3>Progress statistics</h3>
      <div className="dagStats">
        <div>Definitions learned</div>
        <div>{stats.learnedDefs} out of {stats.totalDefs}</div>
        <div>Edges unlocked</div>
        <div>{stats.unlockedEdges} out of {stats.totalEdges}</div>
        <div>Levels completed</div>
        <div>{stats.completedLevels} out of {stats.totalLevels}</div>
      </div>
    </div>
  );
};

export default ProgressTab;
