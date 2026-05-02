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
before backtracking. The algorithm starts at a given {NODE.key.get_reference()} and follows 
{EDGE.key.get_reference("edges")} to visit a neighbor, then recursively visits that neighbor's unvisited neighbors, 
and so on, until it reaches a {NODE.key.get_reference()} with no unvisited neighbors, at which point it backtracks. 
This approach goes deep into the graph structure before exploring other paths.
"""


DEPTH_FIRST_SEARCH = _DepthFirstSearch(DefinitionKey(name="depth-first search", field=FieldName.MATHEMATICS))
# TODO(K4liber): it does not have to recursively visit neighbors, it can be implemented iteratively with a stack.
