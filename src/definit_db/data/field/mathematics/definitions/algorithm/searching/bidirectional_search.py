from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.adjacent import ADJACENT
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _BidirectionalSearch(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
An {ALGORITHM.key.get_reference()} for finding a {PATH.key.get_reference()} 
between two {NODE.key.get_reference("nodes")} in a {GRAPH.key.get_reference()}. It simultaneously runs a search 
forward from the start node and backward from the goal node, stopping when the two frontiers meet. 
By searching from both ends, the algorithm can significantly reduce the search space compared to 
searching in only one direction.

---

Finding a {PATH.key.get_reference()} from A to F in the {GRAPH.key.get_reference()}:
{NODE.key.get_reference("Nodes")}: A, B, C, D, E, F — edges: A–B, B–C, C–D, D–E, E–F

  Forward  from A: step 1 → {{B}},  step 2 → {{C}}
  Backward from F: step 1 → {{E}},  step 2 → {{D}}

  C and D are {ADJACENT.key.get_reference(phrase="adjacent")} → searches meet → 
  {PATH.key.get_reference("path")}: A → B → C → D → E → F
"""


BIDIRECTIONAL_SEARCH = _BidirectionalSearch(DefinitionKey(name="bidirectional search", field=FieldName.MATHEMATICS))
