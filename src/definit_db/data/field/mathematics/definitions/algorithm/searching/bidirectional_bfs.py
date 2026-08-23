from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
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
search stops when the two frontiers meet, allowing the {ALGORITHM.key.get_reference()} to reconstruct a 
{PATH.key.get_reference(phrase="path")} between the start and target while often exploring fewer nodes than a 
single breadth-first search.

---

Finding the {PATH.key.get_reference(phrase="path")} from S to T:
{NODE.key.get_reference("Nodes")}: S, A, B, C, T — edges: S–A, A–B, B–C, C–T


Forward  {BREADTH_FIRST_SEARCH.key.get_reference(phrase="BFS")} from S: step 1 → {{A}},  step 2 → {{B}}

Backward {BREADTH_FIRST_SEARCH.key.get_reference(phrase="BFS")} from T: step 1 → {{C}},  step 2 → {{B}}


Both frontiers reach B → {PATH.key.get_reference(phrase="path")}: S → A → B → C → T
"""


BIDIRECTIONAL_BFS = _BidirectionalBFS(
    key=DefinitionKey(
        name="bidirectional BFS",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("bidirectional breadth-first search",),
)
