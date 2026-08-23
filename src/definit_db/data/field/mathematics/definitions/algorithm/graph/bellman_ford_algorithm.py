from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.graph.dijkstras_algorithm import DIJKSTRAS_ALGORITHM
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.iteration import ITERATION
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.graph.weighted_graph import WEIGHTED_GRAPH


class _BellmanFordAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A {ALGORITHM.key.get_reference()} that {COMPUTATION.key.get_reference("computes")} shortest 
{PATH.key.get_reference("paths")} from a single source 
{NODE.key.get_reference()} to all other nodes in a {WEIGHTED_GRAPH.key.get_reference()}. The algorithm
{ITERATION.key.get_reference("iteratively")} applies edge-relaxation 
{OPERATION.key.get_reference("operations")} on
{EDGE.key.get_reference("edges")} by updating {GRAPH_DISTANCE.key.get_reference("distances")} if a
shorter path is found, repeating this process for each node in the graph. Unlike 
{DIJKSTRAS_ALGORITHM.key.get_reference("Dijkstra's algorithm")}, Bellman-Ford can handle negative edge weights 
and can detect negative-weight {CYCLE.key.get_reference("cycles")}, making it more versatile 
for certain applications.

---

We have nodes A, B, C, D, E and directed weighted {EDGE.key.get_reference("edges")} (listed in the order they are
relaxed each {ITERATION.key.get_reference()}):

(B, C) = -4

(C, D) = -2

(A, B) = 3

(A, D) = 10

(D, E) = 1

Source: A. Initial distances: (A: 0, B: ∞, C: ∞, D: ∞, E: ∞)

Goal: find the shortest {PATH.key.get_reference("paths")} from source A to all nodes.

dist[x] means the current shortest distance from A to x.

V (number of nodes) = 5, so the algorithm performs at most V-1 = 4 {ITERATION.key.get_reference("iterations")}.

Iteration 1 applies relaxations in the listed edge order.

Relax B->C with weight -4: dist[C] = min(∞, ∞ + (-4)) = ∞, because dist[B] is still unknown.

Relax C->D with weight -2: dist[D] = min(∞, ∞ + (-2)) = ∞, because dist[C] is still unknown.

Relax A->B with weight 3: dist[B] = min(∞, 0 + 3) = 3.

Relax A->D with weight 10: dist[D] = min(∞, 0 + 10) = 10.

Relax D->E with weight 1: dist[E] = min(∞, 10 + 1) = 11.

After iteration 1: (A: 0, B: 3, C: ∞, D: 10, E: 11).

Iteration 2 repeats the same relaxation order.

Relax B->C: dist[C] = min(∞, 3 + (-4)) = -1, so path A->B->C is discovered.

Relax C->D: dist[D] = min(10, -1 + (-2)) = -3, so path A->B->C->D is discovered.

Relax A->B: dist[B] = min(3, 0 + 3) = 3 (no change).

Relax A->D: dist[D] = min(-3, 0 + 10) = -3 (no change).

Relax D->E: dist[E] = min(11, -3 + 1) = -2, so path A->B->C->D->E is discovered.

After iteration 2: (A: 0, B: 3, C: -1, D: -3, E: -2).

Iteration 3 again applies all relaxations.

Relax B->C: dist[C] stays -1.

Relax C->D: dist[D] stays -3.

Relax A->B: dist[B] stays 3.

Relax A->D: dist[D] stays -3.

Relax D->E: dist[E] stays -2.

No distance changes in iteration 3, so the algorithm converges early (after 3 of at most 4 iterations).

Final shortest paths from A:

A to A: 0.

A to B: 3 via A->B.

A to C: -1 via A->B->C.

A to D: -3 via A->B->C->D (better than direct A->D = 10).

A to E: -2 via A->B->C->D->E.

This edge order explains why multiple iterations are needed: B->C and C->D are processed before A->B, so dist[B] 
is still ∞ when B->C is first relaxed in iteration 1. Only after A->B sets dist[B] = 3 
can improvements propagate in iteration 2. 
In general, a chain of k hops may need up to k iterations to fully propagate, which is why the V-1 bound appears.
"""


BELLMAN_FORD_ALGORITHM = _BellmanFordAlgorithm(
    key=DefinitionKey(
        name="bellman_ford_algorithm",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("Bellman-Ford",),
)
