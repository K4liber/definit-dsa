from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.n_ary_tree import N_ARY_TREE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _BinaryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {TREE.key.get_reference(phrase="tree")} in which each {NODE.key.get_reference(phrase="node")} has at most 
two children, referred to as the left child and the right child.

A binary tree is a special case of an {N_ARY_TREE.key.get_reference(phrase="n-ary tree")} where n = 2.

---

Arrange {NODE.key.get_reference(phrase="nodes")} as a {TREE.key.get_reference(phrase="tree")}: "A" has 
left child "B" and right child "C", and "B" has a left child "D" but no right child. Since no node holds 
more than two children, this is a binary tree.
"""


BINARY_TREE = _BinaryTree(
    key=DefinitionKey(
        name="binary_tree",
        field=FieldName.MATHEMATICS,
    )
)
