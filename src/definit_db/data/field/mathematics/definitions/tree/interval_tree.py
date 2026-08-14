from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.interval import INTERVAL
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.balanced_binary_tree import BALANCED_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.binary_search_tree import BINARY_SEARCH_TREE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _IntervalTree(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {BINARY_SEARCH_TREE.key.get_reference(phrase="binary search tree")} that stores 
{INTERVAL.key.get_reference(phrase="intervals")} as its keys, ordered by each interval's start point. Each 
{NODE.key.get_reference(phrase="node")} is additionally annotated with the largest end point found anywhere in its 
subtree, which lets a search skip over subtrees that cannot possibly contain an overlap. The 
{TREE.key.get_reference(phrase="tree")} is kept {BALANCED_BINARY_TREE.key.get_reference(phrase="balanced")} to 
guarantee efficient search operations.

---

Storing the {INTERVAL.key.get_reference(phrase="intervals")} [1, 5], [3, 8], [10, 15], and [20, 25] in an interval 
tree, ordered by start point, could produce a tree whose root is [10, 15] (subtree annotation 25), with [3, 8] 
(subtree annotation 8) as its left child and [20, 25] (subtree annotation 25) as its right child; [1, 5] 
(subtree annotation 5) is in turn the left child of [3, 8].

A search for an interval overlapping the point 9 starts at the root [10, 15]: 9 does not fall inside [10, 15], so 
the search must pick a child to continue into. Since the left child's annotation (8) is less than 9, no interval 
anywhere in the left subtree — [3, 8] or [1, 5] — can possibly reach as far as 9, so that whole subtree is skipped 
without being visited. The search continues into the right child [20, 25], which also does not contain 9 and has 
no children left to check, so it correctly concludes that no stored interval overlaps 9.
"""


INTERVAL_TREE = _IntervalTree(
    key=DefinitionKey(
        name="interval_tree",
        field=FieldName.MATHEMATICS,
    )
)
