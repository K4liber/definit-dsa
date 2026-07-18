from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.binary_tree_traversal import BINARY_TREE_TRAVERSAL
from definit_db.data.field.mathematics.definitions.tree.subtree import SUBTREE


class _InOrderTraversal(Definition):
    def _get_content(self) -> str:
        return f"""
A {BINARY_TREE_TRAVERSAL.key.get_reference("binary tree traversal")} of a
{BINARY_TREE.key.get_reference("binary tree")} where, for each {NODE.key.get_reference("node")}, the left 
{SUBTREE.key.get_reference("subtree")} is visited first, then the node itself, and then the right subtree.

---

Take a {BINARY_TREE.key.get_reference("binary tree")} where {NODE.key.get_reference("node")} "A" has left child 
"B" and right child "C". An in-order traversal visits the left {SUBTREE.key.get_reference("subtree")} first ("B"), 
then the node itself ("A"), and finally the right subtree ("C"), reporting the 
{NODE.key.get_reference("nodes")} in the order "B", "A", "C".
"""


IN_ORDER_TRAVERSAL = _InOrderTraversal(
    key=DefinitionKey(
        name="in-order traversal",
        field=FieldName.MATHEMATICS,
    )
)
