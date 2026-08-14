from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE


class _BinarySearchTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {BINARY_TREE.key.get_reference(phrase="binary_tree")} in which the {NODE.key.get_reference(phrase="nodes")} are 
kept in sorted order: for every node, every key in its left subtree is smaller than the node's key, and every key 
in its right subtree is larger. This ordering lets a search for a key proceed by repeatedly moving left or right.

---

Consider a binary search tree whose root {NODE.key.get_reference(phrase="node")} holds the key "8", with left child 
"3" and right child "10". To find "3", start at the root: since "3" < "8", move to the left child and find it. Every 
key in the left subtree ("3") is smaller than "8", and every key in the right subtree ("10") is larger, satisfying 
the ordering property.
"""


BINARY_SEARCH_TREE = _BinarySearchTree(
    key=DefinitionKey(
        name="binary_search_tree",
        field=FieldName.MATHEMATICS,
    )
)
