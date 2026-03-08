import type { DefGraph } from '../types';
import { computeStats } from '../lib/graph';

type Props = {
  rendered: DefGraph;
  learned: Set<string>;
};

const ProgressTab: React.FC<Props> = ({ rendered, learned }) => {
  const stats = computeStats(rendered, learned);

  return (
    <div className="panelSection">
      <h3>Progress</h3>
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
