from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE


class _CompleteBinaryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {BINARY_TREE.key.get_reference(phrase="binary tree")} in which every level, except possibly the last, is 
completely filled, and all {NODE.key.get_reference(phrase="nodes")} are as far left as possible. In a complete 
binary tree, all nodes at the last level are filled from left to right. It can have between 1 and 2^h nodes at 
the last level h.

---

Take a {BINARY_TREE.key.get_reference(phrase="binary tree")} where {NODE.key.get_reference(phrase="node")} 
"A" has children "B" and "C", "B" has children "D" and "E", and "C" has a single child "F". The first two 
levels are completely filled, and the last level is filled left to right ("D", "E", "F") with no gap before 
"F". Because every {NODE.key.get_reference(phrase="node")} sits as far left as possible, this is a complete 
binary tree.
"""


COMPLETE_BINARY_TREE = _CompleteBinaryTree(
    key=DefinitionKey(
        name="complete_binary_tree",
        field=FieldName.MATHEMATICS,
    )
)
