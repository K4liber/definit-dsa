from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _ConnectedGraph(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference(phrase="connected graph")} is a {GRAPH.key.get_reference()} in which every pair of 
{NODE.key.get_reference(phrase="nodes")} is connected by a {PATH.key.get_reference(phrase="path")}.
"""


CONNECTED_GRAPH = _ConnectedGraph(
    key=DefinitionKey(
        name="connected graph",
        field=FieldName.MATHEMATICS,
    )
)
