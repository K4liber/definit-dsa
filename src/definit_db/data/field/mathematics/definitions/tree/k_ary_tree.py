from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.n_ary_tree import N_ARY_TREE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _KAryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is an {N_ARY_TREE.key.get_reference("n-ary tree")} in which each 
{NODE.key.get_reference(phrase="node")} has at most k children.

The maximum number of nodes at level h of a k-ary tree is k^h, and the maximum number of nodes in a 
k-ary tree of height h is (k^(h+1) - 1) / (k - 1).
"""


K_ARY_TREE = _KAryTree(
    key=DefinitionKey(
        name="k_ary_tree",
        field=FieldName.MATHEMATICS,
    )
)
