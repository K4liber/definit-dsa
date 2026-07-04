from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.worst_case import WORST_CASE
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.tree.balanced_binary_tree import BALANCED_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.binary_search_tree import BINARY_SEARCH_TREE
from definit_db.data.field.mathematics.definitions.tree.root import ROOT


class _RedBlackTree(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {BALANCED_BINARY_TREE.key.get_reference(phrase="self-balancing")} 
{BINARY_SEARCH_TREE.key.get_reference(phrase="binary search tree")}. The red-black tree is named after the colors 
used to represent the {NODE.key.get_reference(phrase="nodes")}. It maintains the following properties, which are
not themselves what make {OPERATION.key.get_reference(phrase="operations")} fast, but instead guarantee that the
tree's height stays low:

1. Each node is either red or black.
2. The {ROOT.key.get_reference(phrase="root")} node is always black.
3. Every empty child position (where a node has no left or right child) is treated as black.
4. If a node is red, both of its children are black.
5. Every {PATH.key.get_reference(phrase="path")} from a node down to an empty child position passes through the
   same number of black nodes.

Properties 4 and 5 together bound the height of the tree: since two red nodes can never appear in a row, no
path can contain more red nodes than black ones, so the longest possible path is at most twice as long as the
shortest. This keeps the tree's height proportional to the logarithm of the number of nodes, no matter what
order values are inserted or removed in — unlike a plain binary search tree, whose height can degrade to the
number of nodes in the {WORST_CASE.key.get_reference(phrase="worst case")}. It is this logarithmic height,
combined with the ordering that any binary search tree already provides, that makes search, insertion, and
deletion {EFFICIENCY.key.get_reference(phrase="efficient")}: each of these operations walks at most one path
from the root to an empty child position, so their cost is proportional to the height rather than to the
number of nodes in the tree.

---

Inserting the values 10, 20, and 30 into an initially empty red-black tree could produce this arrangement: root
node 20 (black), with left child 10 (red) and right child 30 (red). The root is black, and both red nodes have
only empty child positions, which count as black, so no red node has a red child. Every path from the root to an
empty child position passes through exactly one black node — the root itself — so the black-node count is the
same on every path, and the tree satisfies all five properties.
"""


RED_BLACK_TREE = _RedBlackTree(
    key=DefinitionKey(
        name="red_black_tree",
        field=FieldName.MATHEMATICS,
    )
)
