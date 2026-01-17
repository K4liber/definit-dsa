from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH


class _AcyclicGraph(Definition):
    def _get_content(self) -> str:
        return f"""
An {self.key.get_reference()} is a {GRAPH.key.get_reference(phrase="graph")} that contains no 
{CYCLE.key.get_reference(phrase="cycles")}.
"""


ACYCLIC_GRAPH = _AcyclicGraph(
    key=DefinitionKey(
        name="acyclic graph",
        field=FieldName.MATHEMATICS,
    )
)
