from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_heap import BINARY_HEAP
from definit_db.data.field.mathematics.definitions.tree.root import ROOT


class _MinHeap(Definition):
    def _get_content(self) -> str:
        return f"""
A {BINARY_HEAP.key.get_reference("binary heap")} in which the key at each
{NODE.key.get_reference("node")} is less than or equal to the keys of its children.

Equivalently, the minimum {ITEM.key.get_reference(phrase="element")} is stored at the {ROOT.key.get_reference("root")}.

---

Arrange values in a {BINARY_HEAP.key.get_reference("binary heap")}: the {ROOT.key.get_reference("root")} "1" has 
children "3" and "2", and "3" has children "5" and "4". Every parent's key 
is less than or equal to its children's 
("1" ≤ "3" and "2"; "3" ≤ "5" and "4"), so the smallest {ITEM.key.get_reference(phrase="element")} 
"1" sits at the root and can be read in a single step.
"""


MIN_HEAP = _MinHeap(
    key=DefinitionKey(
        name="min-heap",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["minimum heap"],
)
