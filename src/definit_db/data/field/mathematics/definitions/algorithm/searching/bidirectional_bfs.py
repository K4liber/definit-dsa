from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.searching.bidirectional_search import BIDIRECTIONAL_SEARCH
from definit_db.data.field.mathematics.definitions.algorithm.searching.breadth_first_search import BREADTH_FIRST_SEARCH
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _BidirectionalBFS(Definition):
    def _get_content(self) -> str:
        return f"""
Bidirectional BFS is a {BIDIRECTIONAL_SEARCH.key.get_reference(phrase="bidirectional search")} technique that 
runs {BREADTH_FIRST_SEARCH.key.get_reference(phrase="breadth-first search")} from both a start 
{NODE.key.get_reference(phrase="node")} and a target node in a {GRAPH.key.get_reference(phrase="graph")}. The 
search stops when the two frontiers meet, allowing the algorithm to reconstruct a 
{PATH.key.get_reference(phrase="path")} between the start and target while often exploring fewer nodes than a 
single breadth-first search.
"""


BIDIRECTIONAL_BFS = _BidirectionalBFS(
    key=DefinitionKey(
        name="bidirectional BFS",
        field=FieldName.MATHEMATICS,
    )
)
