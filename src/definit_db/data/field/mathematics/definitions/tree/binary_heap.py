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
"""


BINARY_HEAP = _BinaryHeap(
    key=DefinitionKey(
        name="binary heap",
        field=FieldName.MATHEMATICS,
    )
)
