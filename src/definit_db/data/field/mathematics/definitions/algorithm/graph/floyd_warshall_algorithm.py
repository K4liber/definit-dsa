from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
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
The {self.key.get_reference()} is an {ALGORITHM.key.get_reference()} that finds the shortest 
{PATH.key.get_reference("paths")} between all pairs of {NODE.key.get_reference("nodes")} in a weighted 
{GRAPH.key.get_reference()}. The algorithm uses {DYNAMIC_PROGRAMMING.key.get_reference("dynamic programming")} 
by iteratively considering each node as an intermediate node and updating the 
{GRAPH_DISTANCE.key.get_reference("distances")} between all pairs of nodes if a shorter path through 
the intermediate node is found. It can handle negative {EDGE.key.get_reference("edge")} weights but 
cannot handle negative-weight {CYCLE.key.get_reference("cycles")}. The algorithm has a {TIME_COMPLEXITY.key.get_reference("time complexity")} 
of O(V³) where V is the number of nodes, making it efficient for dense graphs or when all-pairs shortest paths are needed.

---

Consider a directed weighted {GRAPH.key.get_reference()} with four {NODE.key.get_reference("nodes")} "A", "B", 
"C", and "D" and the {EDGE.key.get_reference("edges")} "A→B"="3", "A→D"="7", "B→A"="8", "B→C"="2", "C→A"="5", 
"C→D"="1", "D→A"="2". The initial {GRAPH_DISTANCE.key.get_reference("distance")} matrix (rows = source, 
columns = target, "∞" = no direct edge) is:

         A    B    C    D
    A    0    3    ∞    7
    B    8    0    2    ∞
    C    5    ∞    0    1
    D    2    ∞    ∞    0

The algorithm considers each node in turn as an intermediate node, shortening any {PATH.key.get_reference()} that 
becomes cheaper through it. After allowing "A" as intermediate ("B→D"="15" via "B→A→D", "C→B"="8", "D→B"="5"):

         A    B    C    D
    A    0    3    ∞    7
    B    8    0    2   15
    C    5    8    0    1
    D    2    5    ∞    0

After also allowing "B" ("A→C"="5" via "A→B→C", "D→C"="7"):

         A    B    C    D
    A    0    3    5    7
    B    8    0    2   15
    C    5    8    0    1
    D    2    5    7    0

After also allowing "C" ("A→D"="6", "B→A"="7", "B→D"="3"):

         A    B    C    D
    A    0    3    5    6
    B    7    0    2    3
    C    5    8    0    1
    D    2    5    7    0

After finally allowing "D" ("B→A"="5", "C→A"="3", "C→B"="6"), the matrix holds the shortest 
{GRAPH_DISTANCE.key.get_reference("distance")} between every pair of nodes:

         A    B    C    D
    A    0    3    5    6
    B    5    0    2    3
    C    3    6    0    1
    D    2    5    7    0
"""


FLOYD_WARSHALL_ALGORITHM = _FloydWarshallAlgorithm(
    DefinitionKey(name="Floyd-Warshall algorithm", field=FieldName.MATHEMATICS)
)
