from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.iteration import ITERATION
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _FloydWarshallAlgorithm(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
An {ALGORITHM.key.get_reference()} that finds the shortest 
{PATH.key.get_reference("paths")} between all pairs of {NODE.key.get_reference("nodes")} in a weighted 
{GRAPH.key.get_reference()}. The algorithm uses {DYNAMIC_PROGRAMMING.key.get_reference("dynamic programming")} 
by {ITERATION.key.get_reference("iteratively")} considering each node as an intermediate node and updating the 
{GRAPH_DISTANCE.key.get_reference("distances")} between all pairs of nodes if a shorter path through 
the intermediate node is found. It can handle negative {EDGE.key.get_reference("edge")} weights but 
cannot handle negative-weight {CYCLE.key.get_reference("cycles")}. The algorithm has a 
{TIME_COMPLEXITY.key.get_reference("time complexity")} of O(V³) where V is the number of nodes, 
making it {EFFICIENCY.key.get_reference(phrase="efficient")} for dense graphs or when all-pairs shortest 
paths are needed.

---

Consider a directed weighted {GRAPH.key.get_reference()} with four {NODE.key.get_reference("nodes")} "A", "B", 
"C", and "D" and the {EDGE.key.get_reference("edges")} "A→B"="3", "A→D"="7", "B→A"="8", "B→C"="2", "C→A"="5", 
"C→D"="1", "D→A"="2". The initial {GRAPH_DISTANCE.key.get_reference("distance")} values are:


A: (A: 0, B: 3, C: ∞, D: 7)

B: (A: 8, B: 0, C: 2, D: ∞)

C: (A: 5, B: ∞, C: 0, D: 1)

D: (A: 2, B: ∞, C: ∞, D: 0)


The algorithm considers each node in turn as an intermediate node, shortening any {PATH.key.get_reference()} that 
becomes cheaper through it. After allowing "A" as intermediate, the updated distances are:


A: (A: 0, B: 3, C: ∞, D: 7)

B: (A: 8, B: 0, C: 2, D: 15)

C: (A: 5, B: 8, C: 0, D: 1)

D: (A: 2, B: 5, C: ∞, D: 0)


After also allowing "B", the updated distances are:


A: (A: 0, B: 3, C: 5, D: 7)

B: (A: 8, B: 0, C: 2, D: 15)

C: (A: 5, B: 8, C: 0, D: 1)

D: (A: 2, B: 5, C: 7, D: 0)


After also allowing "C", the updated distances are:


A: (A: 0, B: 3, C: 5, D: 6)

B: (A: 7, B: 0, C: 2, D: 3)

C: (A: 5, B: 8, C: 0, D: 1)

D: (A: 2, B: 5, C: 7, D: 0)

After finally allowing "D", the shortest {GRAPH_DISTANCE.key.get_reference("distance")} values between every 
pair of nodes are:


A: (A: 0, B: 3, C: 5, D: 6)

B: (A: 5, B: 0, C: 2, D: 3)

C: (A: 3, B: 6, C: 0, D: 1)

D: (A: 2, B: 5, C: 7, D: 0)

"""


FLOYD_WARSHALL_ALGORITHM = _FloydWarshallAlgorithm(
    DefinitionKey(name="Floyd-Warshall algorithm", field=FieldName.MATHEMATICS)
)
