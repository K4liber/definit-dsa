from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.directed_graph import DIRECTED_GRAPH
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _InDegree(Definition):
    def _get_content(self) -> str:
        return f"""
The in-degree of a {NODE.key.get_reference(phrase="node")} in a 
{DIRECTED_GRAPH.key.get_reference(phrase="directed graph")} is the number of 
{EDGE.key.get_reference(phrase="edges")} that point into that node.
"""


IN_DEGREE = _InDegree(
    key=DefinitionKey(
        name="in-degree",
        field=FieldName.MATHEMATICS,
    )
)