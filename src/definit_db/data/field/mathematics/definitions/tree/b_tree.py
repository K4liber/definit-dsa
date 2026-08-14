from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.partitioning import PARTITIONING
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.leaf import LEAF
from definit_db.data.field.mathematics.definitions.tree.subtree import SUBTREE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _BTree(Definition):
    def _get_content(self) -> str:
        return f"""
A self-balancing {TREE.key.get_reference(phrase="tree")} data structure 
in which each 
{NODE.key.get_reference(phrase="node")} can hold multiple keys, kept in sorted order, 
and have multiple children. 
The keys of a node {PARTITIONING.key.get_reference(phrase="partition")} 
the values stored in its child 
{SUBTREE.key.get_reference(phrase="subtrees")}, so that every key in a given subtree falls within the range marked 
by the surrounding keys. All {LEAF.key.get_reference(phrase="leaves")} are kept at the same depth.

---

Consider a B-tree whose root {NODE.key.get_reference(phrase="node")} holds the two keys "10" and "20" and has 
three children. Its left child {SUBTREE.key.get_reference(phrase="subtree")} holds keys less than "10" (such as 
"5"), its middle child holds keys between "10" and "20" (such as "15"), and its right child holds keys greater 
than "20" (such as "25"). All three child {LEAF.key.get_reference(phrase="leaves")} sit at the same depth.
"""


B_TREE = _BTree(
    key=DefinitionKey(
        name="b_tree",
        field=FieldName.MATHEMATICS,
    )
)
