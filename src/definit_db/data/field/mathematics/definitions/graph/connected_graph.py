from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _ConnectedGraph(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference(phrase="connected graph")} is a {GRAPH.key.get_reference()} in which every pair of 
{NODE.key.get_reference(phrase="nodes")} is connected by a {PATH.key.get_reference(phrase="path")}.

---

Consider a {GRAPH.key.get_reference()} of cities "A", "B", and "C" with the 
{EDGE.key.get_reference(phrase="edges")} "A-B" and "B-C". Every pair of 
{NODE.key.get_reference(phrase="nodes")} can be reached from any other: "A" reaches "C" through the 
{PATH.key.get_reference(phrase="path")} A-B-C. Because no city is isolated, this is a connected graph.
"""


CONNECTED_GRAPH = _ConnectedGraph(
    key=DefinitionKey(
        name="connected graph",
        field=FieldName.MATHEMATICS,
    )
)
