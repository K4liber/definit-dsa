from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.tree.complete_binary_tree import COMPLETE_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.heap_tree import HEAP_TREE


class _BinaryHeap(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {HEAP_TREE.key.get_reference("heap")} that is structured as a
{COMPLETE_BINARY_TREE.key.get_reference("complete binary tree")}.

---

Arrange values in a {COMPLETE_BINARY_TREE.key.get_reference("complete binary tree")}: the root "9" has children 
"7" and "6", and "7" has children "3" and "5". Every level is filled from left to right, so the shape is a 
complete binary tree, and each parent is at least as large as its children ("9" ≥ "7" and "6"; "7" ≥ "3" and "5"), 
satisfying the {HEAP_TREE.key.get_reference("heap")} property. Together these make it a binary heap.
"""


BINARY_HEAP = _BinaryHeap(
    key=DefinitionKey(
        name="binary heap",
        field=FieldName.MATHEMATICS,
    )
)
