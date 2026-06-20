from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.greedy_algorithm import GREEDY_ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.heuristic import HEURISTIC
from definit_db.data.field.mathematics.definitions.algorithm.graph.dijkstras_algorithm import DIJKSTRAS_ALGORITHM
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _AStarAlgorithm(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is a {GREEDY_ALGORITHM.key.get_reference("greedy")} 
{ALGORITHM.key.get_reference()} that finds the shortest {PATH.key.get_reference()} between two 
{NODE.key.get_reference("nodes")} in a weighted {GRAPH.key.get_reference()}. It extends 
{DIJKSTRAS_ALGORITHM.key.get_reference("Dijkstra's algorithm")} by using a 
{HEURISTIC.key.get_reference("heuristic function")} to estimate the {GRAPH_DISTANCE.key.get_reference("distance")} 
from the current node to the goal node, allowing it to prioritize more promising paths and find the shortest path more 
efficiently. The algorithm maintains two costs: the actual cost from the start node (g-score) and the estimated 
total cost through the current node to the goal (f-score = g-score + heuristic). 
It requires the heuristic to be admissible (never overestimating the actual cost) to guarantee 
finding the optimal path.

---

We have nodes A, B, C, D, E and weighted {EDGE.key.get_reference("edges")}:

(A, B) = 1
(A, C) = 2
(B, C) = 2
(B, D) = 5
(C, D) = 1
(D, E) = 3

Goal: find the shortest path from A (start) to E (goal).

Using the {DIJKSTRAS_ALGORITHM.key.get_reference("Dijkstra's algorithm")} we find the following paths:

- A → B → C → D → E = 1 + 2 + 1 + 3 = 7
- A → C → D → E     = 2 + 1 + 3     = 6  ← optimal

Let's assume, we have some heuristic h(n) that estimates the remaining distance from node n to E:

h(A) = 6, h(B) = 6, h(C) = 4, h(D) = 3, h(E) = 0

At each step we expand the node with the lowest f-score (f = g + h), where g is the known cost from A:

Start: g(A)=0, h(A)=6, f(A)=6 → Open: {{A:6}}, Closed: {{}}

Visit A (f=6):
  → B: g=1, h=6, f=7
  → C: g=2, h=4, f=6
  Open: {{C:6, B:7}}, Closed: {{A}}

Visit C (f=6):
  → D: g=3, h=3, f=6
  Open: {{D:6, B:7}}, Closed: {{A, C}}

Visit D (f=6):
  → E: g=6, h=0, f=6
  Open: {{E:6, B:7}}, Closed: {{A, C, D}}

Visit E (f=6) → goal reached!

The shortest path is A → C → D → E with a total cost of 6. Node B was never expanded — 
its f-score of 7 was always worse than the optimal path's f-score of 6, so the heuristic 
correctly steered the search away from it and made the final algorithm more efficient.

"""


A_STAR_ALGORITHM = _AStarAlgorithm(DefinitionKey(name="A-star algorithm", field=FieldName.MATHEMATICS))
