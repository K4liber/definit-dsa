from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE


class _BinaryTreeTraversal(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a procedure for visiting each {NODE.key.get_reference("node")} in a
{BINARY_TREE.key.get_reference("binary tree")} in a specified order.

---

Take a {BINARY_TREE.key.get_reference("binary tree")} where {NODE.key.get_reference("node")} "A" has 
children "B" and "C". A binary tree traversal that visits a node before its children would report the 
{NODE.key.get_reference("nodes")} in the order "A", "B", "C", touching each node exactly once.
"""


BINARY_TREE_TRAVERSAL = _BinaryTreeTraversal(
    key=DefinitionKey(
        name="binary tree traversal",
        field=FieldName.MATHEMATICS,
    )
)
