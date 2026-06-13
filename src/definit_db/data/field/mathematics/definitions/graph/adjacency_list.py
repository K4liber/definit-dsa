from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _AdjacencyList(Definition):
    def _get_content(self) -> str:
        return f"""
An adjacency list is a way of representing a {GRAPH.key.get_reference(phrase="graph")} as a collection of lists. 
Each list corresponds to a {NODE.key.get_reference(phrase="node")} in the graph and contains a list of its 
adjacent nodes.

---

Take a {GRAPH.key.get_reference(phrase="graph")} of three cities "A", "B", and "C" with the 
{EDGE.key.get_reference(phrase="edges")} "A-B" and "B-C". Its adjacency list stores, for each 
{NODE.key.get_reference(phrase="node")}, the nodes it directly connects to:

A: [B]
B: [A, C]
C: [B]
"""


ADJACENCY_LIST = _AdjacencyList(
    key=DefinitionKey(
        name="adjacency_list",
        field=FieldName.MATHEMATICS,
    )
)
