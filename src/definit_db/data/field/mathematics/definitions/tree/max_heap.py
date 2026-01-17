from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_heap import BINARY_HEAP
from definit_db.data.field.mathematics.definitions.tree.root import ROOT


class _MaxHeap(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {BINARY_HEAP.key.get_reference("binary heap")} in which the key at each
{NODE.key.get_reference("node")} is greater than or equal to the keys of its children.

Equivalently, the maximum element is stored at the {ROOT.key.get_reference("root")}.
"""


MAX_HEAP = _MaxHeap(
    key=DefinitionKey(
        name="max-heap",
        field=FieldName.MATHEMATICS,
    )
)
