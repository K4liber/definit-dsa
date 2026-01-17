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
An {self.key.get_reference()} is a {BINARY_TREE_TRAVERSAL.key.get_reference("binary tree traversal")} of a
{BINARY_TREE.key.get_reference("binary tree")} where, for each {NODE.key.get_reference("node")}, the left 
{SUBTREE.key.get_reference("subtree")} is visited first, then the node itself, and then the right subtree.
"""


IN_ORDER_TRAVERSAL = _InOrderTraversal(
    key=DefinitionKey(
        name="in-order traversal",
        field=FieldName.MATHEMATICS,
    )
)
