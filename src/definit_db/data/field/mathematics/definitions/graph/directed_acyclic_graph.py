from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.directed_graph import DIRECTED_GRAPH
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _DirectedAcyclicGraph(Definition):
    def _get_content(self) -> str:
        return f"""
A directed acyclic graph is a {DIRECTED_GRAPH.key.get_reference(phrase="directed graph")} with no 
{CYCLE.key.get_reference(phrase="cycles")}.

---

Picture three tasks "A", "B", and "C" as {NODE.key.get_reference(phrase="nodes")}, where the 
{EDGE.key.get_reference(phrase="edges")} "A→B" and "B→C" mean "must finish before". Following the arrows 
you can never return to a task you already completed, so this 
{DIRECTED_GRAPH.key.get_reference(phrase="directed graph")} has no {CYCLE.key.get_reference(phrase="cycle")} 
and is a directed acyclic graph.
"""


DIRECTED_ACYCLIC_GRAPH = _DirectedAcyclicGraph(
    key=DefinitionKey(
        name="directed_acyclic_graph",
        field=FieldName.MATHEMATICS,
    )
)
