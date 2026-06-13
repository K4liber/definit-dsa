from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.descendant import DESCENDANT
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Subtree(Definition):
    def _get_content(self) -> str:
        return f"""
A {TREE.key.get_reference(phrase="tree")} formed from a {NODE.key.get_reference(phrase="node")} and all its 
{DESCENDANT.key.get_reference(phrase="descendants")} in a tree.

---

In a {TREE.key.get_reference(phrase="tree")} where "A" is the parent of "B" and "C", and "B" is the parent of "D" 
and "E", the subtree rooted at {NODE.key.get_reference(phrase="node")} "B" consists of "B" together with its 
{DESCENDANT.key.get_reference(phrase="descendants")} "D" and "E".
"""


SUBTREE = _Subtree(
    key=DefinitionKey(
        name="subtree",
        field=FieldName.MATHEMATICS,
    )
)
