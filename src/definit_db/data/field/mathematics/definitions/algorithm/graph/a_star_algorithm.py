from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.greedy_algorithm import GREEDY_ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.heuristic import HEURISTIC
from definit_db.data.field.mathematics.definitions.algorithm.graph.dijkstras_algorithm import DIJKSTRAS_ALGORITHM
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION


class _AStarAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A {GREEDY_ALGORITHM.key.get_reference("greedy")} 
{ALGORITHM.key.get_reference()} that finds the shortest {PATH.key.get_reference()} between two 
{NODE.key.get_reference("nodes")} in a weighted {GRAPH.key.get_reference()}. It extends 
{DIJKSTRAS_ALGORITHM.key.get_reference("Dijkstra's algorithm")} by using a 
{HEURISTIC.key.get_reference("heuristic function")} to estimate the 
{GRAPH_DISTANCE.key.get_reference("distance")} 
from the current node to the goal node, allowing it to prioritize more promising paths and find the shortest path more 
{EFFICIENCY.key.get_reference(phrase="efficiently")}. The algorithm maintains two costs: the actual cost from 
the start node (g-score) and the estimated 
total cost through the current node to the goal (f-score = g-score + heuristic). 
It requires the heuristic to be admissible (never overestimating the actual cost) to guarantee 
finding the {OPTIMAL_SOLUTION.key.get_reference("optimal")} path.

---

Consider nodes A, B, C, D, E with weighted {EDGE.key.get_reference("edges")}: 
(A, B)=1, (A, C)=2, (B, C)=2, (B, D)=5, (C, D)=1, (D, E)=3.


Goal: find the shortest {PATH.key.get_reference()} from A (start) to E (goal).


Candidate path 1: A -> B -> C -> D -> E has cost 1 + 2 + 1 + 3 = 7.

Candidate path 2: A -> C -> D -> E has cost 2 + 1 + 3 = 6, which is 
{OPTIMAL_SOLUTION.key.get_reference("optimal")}.

Because this is a tiny example, we can compute those two path costs by hand at the start.
That is only a quick sanity check. In general, the {ALGORITHM.key.get_reference()} does not
know the best path cost in advance, so it must still explore step by step.


Assume heuristic estimates to E are: h(A)=6, h(B)=6, h(C)=4, h(D)=3, h(E)=0.

These heuristic values are chosen only for this small worked example to illustrate
how A* ranks nodes. They are not a fixed built-in heuristic; for a real problem,
the heuristic function is defined from domain knowledge (for example, geometry or
other problem-specific structure).


At each step, expand the node with lowest f-score, where f = g + h and g is known cost from A.


Step 1: start at A with g(A)=0, h(A)=6, f(A)=6. Open={{A:6}}, Closed={{}}.

Step 2: visit A. Discover B with g=1, h=6, f=7 and C with g=2, h=4, f=6. Open={{C:6, B:7}}, Closed={{A}}.

Step 3: visit C. Discover D with g=3, h=3, f=6. Open={{D:6, B:7}}, Closed={{A, C}}.

Step 4: visit D. Discover E with g=6, h=0, f=6. Open={{E:6, B:7}}, Closed={{A, C, D}}.

Step 5: visit E. Goal reached.


Result: the shortest path is A -> C -> D -> E with total cost 6. Node B is never expanded because its f-score (7) 
stays worse than the {OPTIMAL_SOLUTION.key.get_reference("optimal")} path score (6), 
so the heuristic steers the search and improves {EFFICIENCY.key.get_reference("efficiency")}.

"""


A_STAR_ALGORITHM = _AStarAlgorithm(
    DefinitionKey(name="A-star algorithm", field=FieldName.MATHEMATICS),
    aliases=("A*", "A-star"),
)
