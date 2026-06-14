from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.height_balanced_binary_search_tree import (
    HEIGHT_BALANCED_BINARY_SEARCH_TREE,
)
from definit_db.data.field.mathematics.definitions.tree.subtree import SUBTREE


class _AVLTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {HEIGHT_BALANCED_BINARY_SEARCH_TREE.key.get_reference(phrase="height-balanced binary search tree")} that keeps 
itself balanced automatically: after every insertion or deletion it restores the invariant that, for any 
{NODE.key.get_reference(phrase="node")}, the heights of the left and right 
{SUBTREE.key.get_reference(phrase="subtrees")} differ by at most one. It was the first such self-balancing 
structure to be invented, named after its inventors Georgy Adelson-Velsky and Evgenii Landis.

---

Insert the keys "1", "2", and "3" in order into an AVL tree. After inserting "3", the 
{NODE.key.get_reference(phrase="node")} "1" would have a left {SUBTREE.key.get_reference(phrase="subtree")} of 
height 0 and a right subtree of height 2 — a difference of two, violating the balance rule. The tree rebalances 
by rotating so that "2" becomes the root with "1" and "3" as its children, restoring the height difference to at 
most one.
"""


AVL_TREE = _AVLTree(
    key=DefinitionKey(
        name="avl_tree",
        field=FieldName.MATHEMATICS,
    )
)
