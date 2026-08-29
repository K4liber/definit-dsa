from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _SelectionSort(Definition):
    def _get_content(self) -> str:
        return f"""
SelectionSort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that sorts an 
{SEQUENCE.key.get_reference("sequence")} by repeatedly finding the minimum (or maximum) 
{ITEM.key.get_reference(phrase="element")} from the unsorted part and moving it to the beginning (or end). 
This process is repeated until the entire sequence is sorted.

---

Sort [4, 1, 3, 2] in ascending order. At each step, find the minimum of the unsorted part and
swap it into the next sorted position:


[4, 1, 3, 2]; unsorted: [4,1,3,2]; min=1 → swap with pos 0 → [1, 4, 3, 2]

[1, 4, 3, 2]; unsorted: [4,3,2]; min=2 → swap with pos 1 → [1, 2, 3, 4]

[1, 2, 3, 4]; unsorted: [3,4]; min=3 → already at pos 2 → [1, 2, 3, 4]

[1, 2, 3, 4]; unsorted: [4]; single element → done


Result: [1, 2, 3, 4]
"""


SELECTION_SORT = _SelectionSort(
    key=DefinitionKey(
        name="selection sort",
        field=FieldName.MATHEMATICS,
    ),
)
