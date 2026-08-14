from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _Path(Definition):
    def _get_content(self) -> str:
        return f"""
A path in a {GRAPH.key.get_reference(phrase="graph")} is a {SEQUENCE.key.get_reference(phrase="sequence")} of 
{EDGE.key.get_reference(phrase="edges")} which joins a sequence of {NODE.key.get_reference(phrase="nodes")} 
which, by most definitions, are all distinct (and since the nodes are distinct, so are the edges).

---

In a {GRAPH.key.get_reference(phrase="graph")} of cities "A", "B", "C", and "D" with the 
{EDGE.key.get_reference(phrase="edges")} "A-B", "B-C", and "C-D", the 
{SEQUENCE.key.get_reference(phrase="sequence")} A-B, B-C, C-D is a path: it walks through the distinct 
{NODE.key.get_reference(phrase="nodes")} A, B, C, D without repeating any of them.
"""


PATH = _Path(
    key=DefinitionKey(
        name="path",
        field=FieldName.MATHEMATICS,
    )
)
