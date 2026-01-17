from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.full_binary_tree import FULL_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.leaf import LEAF


class _PerfectBinaryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {BINARY_TREE.key.get_reference("binary tree")} in which every internal 
(non-{LEAF.key.get_reference("leaf")}) {NODE.key.get_reference("node")} has exactly two children 
and all {LEAF.key.get_reference("leaf")} nodes are at the same depth.

Equivalently, a perfect binary tree is {FULL_BINARY_TREE.key.get_reference("full")} 
and all leaves are at the same depth.
"""


PERFECT_BINARY_TREE = _PerfectBinaryTree(
    key=DefinitionKey(
        name="perfect binary tree",
        field=FieldName.MATHEMATICS,
    )
)
