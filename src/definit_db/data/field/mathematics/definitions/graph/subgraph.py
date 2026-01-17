from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _Subgraph(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {GRAPH.key.get_reference()} formed from a subset of the 
{NODE.key.get_reference("nodes")} and {EDGE.key.get_reference("edges")} of another graph.
"""


SUBGRAPH = _Subgraph(
    key=DefinitionKey(
        name="subgraph",
        field=FieldName.MATHEMATICS,
    )
)
