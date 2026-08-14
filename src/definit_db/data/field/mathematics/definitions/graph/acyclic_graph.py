from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _AcyclicGraph(Definition):
    def _get_content(self) -> str:
        return f"""
A {GRAPH.key.get_reference(phrase="graph")} that contains no 
{CYCLE.key.get_reference(phrase="cycles")}.

---

Consider cities "A", "B", and "C" connected as A-B and B-C, with no link back from "C" to "A". 
Starting at any {NODE.key.get_reference(phrase="node")} you can never return to it, so this 
{GRAPH.key.get_reference(phrase="graph")} has no {CYCLE.key.get_reference(phrase="cycle")} and is acyclic.
"""


ACYCLIC_GRAPH = _AcyclicGraph(
    key=DefinitionKey(
        name="acyclic graph",
        field=FieldName.MATHEMATICS,
    )
)
