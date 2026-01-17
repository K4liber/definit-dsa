from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.tree.k_ary_tree import K_ARY_TREE
from definit_db.data.field.mathematics.definitions.tree.n_ary_tree import N_ARY_TREE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _BinaryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {TREE.key.get_reference(phrase="tree")} in which each node has at most two children, referred to as the left 
child and the right child.

A binary tree is a special case of an {N_ARY_TREE.key.get_reference(phrase="n-ary tree")} and a 
{K_ARY_TREE.key.get_reference(phrase="k-ary tree")} where k = 2.
"""


BINARY_TREE = _BinaryTree(
    key=DefinitionKey(
        name="binary_tree",
        field=FieldName.MATHEMATICS,
    )
)
