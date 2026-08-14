from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.balanced_binary_tree import BALANCED_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.subtree import SUBTREE


class _UnbalancedBinaryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {BINARY_TREE.key.get_reference(phrase="binary tree")} that does not satisfy the 
{BALANCED_BINARY_TREE.key.get_reference(phrase="balanced binary tree")} property. In an unbalanced binary tree, 
the depth of the two {SUBTREE.key.get_reference(phrase="subtrees")} of at least one 
{NODE.key.get_reference(phrase="node")} differs by more than one.

---

Take a {BINARY_TREE.key.get_reference(phrase="binary tree")} where {NODE.key.get_reference(phrase="node")} "A" 
has left child "B" and right child "C". On the left side the {NODE.key.get_reference(phrase="nodes")} form a 
chain: "B" has left child "D", and "D" has left child "E". At "A" the left 
{SUBTREE.key.get_reference(phrase="subtree")} (B, D, E) has height 2 while the right subtree (C) has height 0 — 
a difference of two — so the {BALANCED_BINARY_TREE.key.get_reference(phrase="balance")} property fails and the 
tree is unbalanced.
"""


UNBALANCED_BINARY_TREE = _UnbalancedBinaryTree(
    key=DefinitionKey(
        name="unbalanced_binary_tree",
        field=FieldName.MATHEMATICS,
    )
)
