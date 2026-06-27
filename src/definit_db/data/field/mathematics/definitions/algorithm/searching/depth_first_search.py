from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _DepthFirstSearch(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is an {ALGORITHM.key.get_reference()} for traversing or searching 
a {GRAPH.key.get_reference()} structure. It explores as far as possible along each {PATH.key.get_reference()} 
before backtracking. Starting at a given {NODE.key.get_reference()}, it follows 
{EDGE.key.get_reference("edges")} to visit a neighbor and continues exploring that neighbor's unvisited
neighbors, going deeper into the graph until reaching a dead end, then backtracks to explore other paths.

---

{GRAPH.key.get_reference("Graph")} edges: A–B, A–C, B–D, B–E

DFS from {NODE.key.get_reference("node")} A:

  Visit A → go deep to B → go deep to D (dead end) → backtrack to B
  → visit E (dead end) → backtrack to A → visit C (dead end)

  Visit order: A, B, D, E, C
"""


DEPTH_FIRST_SEARCH = _DepthFirstSearch(DefinitionKey(name="depth-first search", field=FieldName.MATHEMATICS))
