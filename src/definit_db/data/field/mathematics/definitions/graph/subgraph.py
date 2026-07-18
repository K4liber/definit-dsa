from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _Subgraph(Definition):
    def _get_content(self) -> str:
        return f"""
A {GRAPH.key.get_reference()} formed from a subset of the 
{NODE.key.get_reference("nodes")} and {EDGE.key.get_reference("edges")} of another graph.

---

Start with a {GRAPH.key.get_reference()} of cities "A", "B", "C", and "D" with the 
{EDGE.key.get_reference("edges")} "A-B", "B-C", and "C-D". Keeping only the 
{NODE.key.get_reference("nodes")} "A", "B", "C" together with the edges "A-B" and "B-C" gives a subgraph 
of the original graph.
"""


SUBGRAPH = _Subgraph(
    key=DefinitionKey(
        name="subgraph",
        field=FieldName.MATHEMATICS,
    )
)
