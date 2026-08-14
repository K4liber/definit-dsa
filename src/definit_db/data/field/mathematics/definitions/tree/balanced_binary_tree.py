from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.subtree import SUBTREE


class _BalancedBinaryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {BINARY_TREE.key.get_reference(phrase="binary tree")} in which the depth of the two 
{SUBTREE.key.get_reference(phrase="subtrees")} of every {NODE.key.get_reference(phrase="node")} never differs 
by more than one. This means that for any given node in the tree, the height of its left and right subtrees can 
differ by at most one.

---

Build a {BINARY_TREE.key.get_reference(phrase="binary tree")} where {NODE.key.get_reference(phrase="node")} 
"A" has children "B" and "C", and "B" has a single child "D". At "A" the left 
{SUBTREE.key.get_reference(phrase="subtree")} (B, D) has height 1 and the right subtree (C) has height 0; 
the difference is 1, so the tree is a balanced binary tree.
"""


BALANCED_BINARY_TREE = _BalancedBinaryTree(
    key=DefinitionKey(
        name="balanced_binary_tree",
        field=FieldName.MATHEMATICS,
    )
)
