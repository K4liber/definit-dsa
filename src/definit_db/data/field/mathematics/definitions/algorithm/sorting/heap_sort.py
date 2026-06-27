from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.tree.heap_tree import HEAP_TREE


class _HeapSort(Definition):
    def _get_content(self) -> str:
        return f"""
Heap Sort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that builds a 
{HEAP_TREE.key.get_reference(phrase="heap tree")} from the elements of a {SEQUENCE.key.get_reference("sequence")}, 
and then repeatedly extracts the root (the maximum or minimum) and restores the heap until the entire 
{SEQUENCE.key.get_reference("sequence")} is sorted.

---

Sorting [4, 1, 3, 2] using a max-{HEAP_TREE.key.get_reference(phrase="heap")}:

  Build heap:  [4, 2, 3, 1]
  Extract 4 →  [3, 2, 1]  | sorted: [4]
  Extract 3 →  [2, 1]     | sorted: [3, 4]
  Extract 2 →  [1]        | sorted: [2, 3, 4]
  Extract 1 →  []         | sorted: [1, 2, 3, 4]  ✓
"""


HEAP_SORT = _HeapSort(
    key=DefinitionKey(
        name="heap_sort",
        field=FieldName.MATHEMATICS,
    )
)
