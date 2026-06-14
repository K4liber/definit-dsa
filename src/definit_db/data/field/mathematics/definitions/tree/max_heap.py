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

---

Arrange values in a {BINARY_HEAP.key.get_reference("binary heap")}: the {ROOT.key.get_reference("root")} "9" has 
children "7" and "6", and "7" has children "3" and "5". Every parent's key is greater than or equal to its 
children's ("9" ≥ "7" and "6"; "7" ≥ "3" and "5"), so the largest element "9" sits at the root and can be read in 
a single step.
"""


MAX_HEAP = _MaxHeap(
    key=DefinitionKey(
        name="max-heap",
        field=FieldName.MATHEMATICS,
    )
)
