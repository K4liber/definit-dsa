from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _Edge(Definition):
    def _get_content(self) -> str:
        return f"""
An edge is a directed or undirected connection between two {NODE.key.get_reference(phrase="nodes")}. 
It defines a {RELATION.key.get_reference(phrase="relationship")} or link between them.

---

Suppose two cities "A" and "B" are each a {NODE.key.get_reference(phrase="node")}. A road that runs 
directly between them is an edge: it links the two {NODE.key.get_reference(phrase="nodes")} and expresses 
the {RELATION.key.get_reference(phrase="relationship")} "is connected by road to".
"""


EDGE = _Edge(
    key=DefinitionKey(
        name="edge",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("link", "arc"),
)
