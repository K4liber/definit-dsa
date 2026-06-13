from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.directed_acyclic_graph import DIRECTED_ACYCLIC_GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _Tree(Definition):
    def _get_content(self) -> str:
        return f"""
A tree is a {DIRECTED_ACYCLIC_GRAPH.key.get_reference(phrase="directed acyclic graph")} with the restriction that 
a child can only have one parent. Each {NODE.key.get_reference(phrase="node")} can have zero or more child nodes.

---

Arrange family members as {NODE.key.get_reference(phrase="nodes")}: "A" is the parent of "B" and "C", 
and "B" is the parent of "D". Every member has exactly one parent (except "A", which has none), and no 
arrows ever loop back, so this {DIRECTED_ACYCLIC_GRAPH.key.get_reference(phrase="directed acyclic graph")} 
is a tree.
"""


TREE = _Tree(
    key=DefinitionKey(
        name="tree",
        field=FieldName.MATHEMATICS,
    )
)
