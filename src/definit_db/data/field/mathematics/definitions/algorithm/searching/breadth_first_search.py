from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.graph.weighted_graph import WEIGHTED_GRAPH


class _BreadthFirstSearch(Definition):
    def _get_content(self) -> str:
        return f"""
An {ALGORITHM.key.get_reference()} for traversing or searching 
a {GRAPH.key.get_reference()} structure. It explores all {NODE.key.get_reference("nodes")} at the current 
depth level before moving to nodes at the next depth level. The algorithm starts at a given node and 
systematically visits all neighboring nodes first, then visits all unvisited neighbors of those neighbors, 
and so on. This level-by-level exploration ensures that the shortest {PATH.key.get_reference()} 
(in terms of number of {EDGE.key.get_reference("edges")}) is found first in 
non-{WEIGHTED_GRAPH.key.get_reference("weighted graphs")}.

---

{GRAPH.key.get_reference("Graph")} {EDGE.key.get_reference("edges")}: A–B, A–C, B–D, B–E

BFS (Breadth-First Search) from {NODE.key.get_reference("node")} A:


Level 0: [A]

Level 1: [B, C] (neighbors of A)

Level 2: [D, E] (unvisited neighbors of B)


Visit order: A, B, C, D, E
"""


BREADTH_FIRST_SEARCH = _BreadthFirstSearch(
    DefinitionKey(name="breadth-first search", field=FieldName.MATHEMATICS),
    aliases=("BFS", "breadth first search"),
)
