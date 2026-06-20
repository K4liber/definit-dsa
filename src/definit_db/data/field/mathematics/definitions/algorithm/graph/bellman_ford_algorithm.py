from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.graph.dijkstras_algorithm import DIJKSTRAS_ALGORITHM
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _BellmanFordAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A {ALGORITHM.key.get_reference()} that computes shortest {PATH.key.get_reference("paths")} from a single source 
{NODE.key.get_reference()} to all other nodes in a weighted {GRAPH.key.get_reference()}. The algorithm iteratively 
relaxes all {EDGE.key.get_reference("edges")} by updating {GRAPH_DISTANCE.key.get_reference("distances")} if a 
shorter path is found, repeating this process for each node in the graph. Unlike 
{DIJKSTRAS_ALGORITHM.key.get_reference("Dijkstra's algorithm")}, Bellman-Ford can handle negative edge weights and 
can detect negative-weight {CYCLE.key.get_reference("cycles")}, making it more versatile for certain applications.

---

We have nodes A, B, C, D, E and directed weighted edges (listed in the order they are relaxed each iteration):

(B, C) = -4
(C, D) = -2
(A, B) = 3
(A, D) = 10
(D, E) = 1

Source: A. Initial distances: (A: 0, B: ∞, C: ∞, D: ∞, E: ∞)

dist[x] means the current shortest distance from A to x.

V (number of nodes) = 5, so the algorithm performs at most V-1 = 4 iterations:

Iteration 1:
  B→C=-4: dist[C] = min(∞, ∞+(−4)) = ∞   (dist[B] not yet known)
  C→D=-2: dist[D] = min(∞, ∞+(−2)) = ∞   (dist[C] not yet known)
  A→B=3:  dist[B] = min(∞, 0+3)    = 3
  A→D=10: dist[D] = min(∞, 0+10)   = 10
  D→E=1:  dist[E] = min(∞, 10+1)   = 11
  After iteration 1: (A: 0, B: 3, C: ∞, D: 10, E: 11)

Iteration 2:
  B→C=-4: dist[C] = min(∞, 3+(−4))  = −1  ← dist[B]=3 now known, path A→B→C found
  C→D=-2: dist[D] = min(10, −1+(−2)) = −3  ← dist[C]=−1 just updated, A→B→C→D found
  A→B=3:  dist[B] = min(3, 0+3)     = 3   (no change)
  A→D=10: dist[D] = min(−3, 0+10)   = −3  (no change)
  D→E=1:  dist[E] = min(11, −3+1)   = −2  ← D updated, A→B→C→D→E found
  After iteration 2: (A: 0, B: 3, C: −1, D: −3, E: −2)

Iteration 3:
  B→C=-4: dist[C] = min(−1, 3+(−4)) = −1  (no change)
  C→D=-2: dist[D] = min(−3, −1+(−2))= −3  (no change)
  A→B=3:  dist[B] = min(3, 0+3)     = 3   (no change)
  A→D=10: dist[D] = min(−3, 0+10)   = −3  (no change)
  D→E=1:  dist[E] = min(−2, −3+1)   = −2  (no change)
  No distances changed → converged early (after 3 of the maximum V-1 = 4 iterations).

Final shortest paths from A:

- A to A: 0
- A to B: 3   (A→B)
- A to C: −1  (A→B→C = 3 + (−4) = −1)
- A to D: −3  (A→B→C→D = −1 + (−2) = −3, beats the direct A→D = 10)
- A to E: −2  (A→B→C→D→E = −3 + 1 = −2)

The edge processing order shows why multiple iterations are needed: B→C and C→D appear before A→B,
so in iteration 1 dist[B] is still ∞ when B→C is first relaxed. Only after A→B sets dist[B]=3
can the path propagate further in iteration 2. A chain of k hops may need up to k iterations to
fully propagate — hence the V-1 iteration bound.
"""


BELLMAN_FORD_ALGORITHM = _BellmanFordAlgorithm(
    key=DefinitionKey(
        name="bellman_ford_algorithm",
        field=FieldName.MATHEMATICS,
    )
)
