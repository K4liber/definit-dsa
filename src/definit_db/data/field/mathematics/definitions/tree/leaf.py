from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Leaf(Definition):
    def _get_content(self) -> str:
        return f"""
A {NODE.key.get_reference(phrase="node")} in a {TREE.key.get_reference(phrase="tree")} that does not have 
any children (descendants).

---

Picture a small {TREE.key.get_reference(phrase="tree")} where {NODE.key.get_reference(phrase="node")} "A" 
branches to "B" and "C". Since "B" and "C" have no children of their own, each of them is a leaf, while "A" 
is not.
"""


LEAF = _Leaf(
    key=DefinitionKey(
        name="leaf",
        field=FieldName.MATHEMATICS,
    )
)
