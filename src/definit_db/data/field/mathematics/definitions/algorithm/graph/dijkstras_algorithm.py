from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.greedy_algorithm import GREEDY_ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.iteration import ITERATION
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _DijkstrasAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A {GREEDY_ALGORITHM.key.get_reference(phrase="greedy")} {ALGORITHM.key.get_reference()} that finds the shortest 
{PATH.key.get_reference("paths")} from a single source {NODE.key.get_reference()} to all other 
nodes in a weighted {GRAPH.key.get_reference()} with non-negative 
{EDGE.key.get_reference("edge")} weights. The algorithm maintains a set of nodes for which the shortest 
{GRAPH_DISTANCE.key.get_reference("distance")} from the source is known, and 
{ITERATION.key.get_reference("iteratively")} selects the node with the minimum distance to expand the set until 
all nodes are processed.

---

We have nodes A, B, C, D, E and weighted edges:


(A, B) = 1

(A, C) = 4

(B, C) = 2

(B, D) = 5

(C, D) = 1

(D, E) = 3

From a single source A, at the beginning, we have a following distances only considering nodes from the source (A):


A: (A: 0, B: 1, C: 4, D: ∞, E: ∞)


So the the next node to visit is B (we did not visit it yet and it has the smallest distance from the source).

Visit B: (A: 0, B: 1, C: 3, D: 6, E: ∞)

Visit C: (A: 0, B: 1, C: 3, D: 4, E: ∞)

Visit D: (A: 0, B: 1, C: 3, D: 4, E: 7)

Visit E: (A: 0, B: 1, C: 3, D: 4, E: 7)


At this point all nodes have been visited and the shortest paths from A to all other nodes have been found:


- A to A: 0

- A to B: 1

- A to C: 3

- A to D: 4

- A to E: 7

"""


DIJKSTRAS_ALGORITHM = _DijkstrasAlgorithm(
    key=DefinitionKey(
        name="dijkstras_algorithm",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("Dijkstra's algorithm",),
)
