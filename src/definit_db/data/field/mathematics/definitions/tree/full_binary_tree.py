from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.leaf import LEAF


class _FullBinaryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {BINARY_TREE.key.get_reference("binary tree")} 
in which every {NODE.key.get_reference("node")} has either 0 or 2 children.

Equivalently, every internal (non-{LEAF.key.get_reference("leaf")}) node has exactly two children.
"""


FULL_BINARY_TREE = _FullBinaryTree(
    key=DefinitionKey(
        name="full binary tree",
        field=FieldName.MATHEMATICS,
    )
)
