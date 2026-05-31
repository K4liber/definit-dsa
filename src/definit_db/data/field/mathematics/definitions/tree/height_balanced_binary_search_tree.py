from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.balanced_binary_tree import BALANCED_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.binary_search_tree import BINARY_SEARCH_TREE
from definit_db.data.field.mathematics.definitions.tree.subtree import SUBTREE


class _HeightBalancedBinarySearchTree(Definition):
    def _get_content(self) -> str:
        return f"""
A height-balanced binary search tree is a {BINARY_SEARCH_TREE.key.get_reference(phrase="binary search tree")} 
that satisfies the {BALANCED_BINARY_TREE.key.get_reference(phrase="balanced binary tree")} property: for every 
{NODE.key.get_reference(phrase="node")}, the heights of the left and right 
{SUBTREE.key.get_reference(phrase="subtrees")} differ by at most one.
"""


HEIGHT_BALANCED_BINARY_SEARCH_TREE = _HeightBalancedBinarySearchTree(
    key=DefinitionKey(
        name="height-balanced_binary_search_tree",
        field=FieldName.MATHEMATICS,
    )
)