from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.adjacent import ADJACENT
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _BubbleSort(Definition):
    def _get_content(self) -> str:
        return f"""
Bubble Sort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that repeatedly steps through a 
{SEQUENCE.key.get_reference("sequence")}, compares {ADJACENT.key.get_reference(phrase="adjacent")} 
{ITEM.key.get_reference(phrase="elements")} and swaps them if they are in the wrong order. This process is repeated 
until the entire {SEQUENCE.key.get_reference("sequence")} is sorted. Bubble sort is simple but generally inefficient 
for large {INPUT_DATA.key.get_reference(phrase="inputs")}, as it repeatedly passes over the sequence.

---

Sorting [3, 1, 2]:

Pass 1: 

compare 3,1 → swap → [1, 3, 2]

compare 3,2 → swap → [1, 2, 3]

Pass 2:

compare 1,2 → ok

compare 2,3 → ok  →  [1, 2, 3]  ✓

nothing swapped in this pass, so the {SEQUENCE.key.get_reference("sequence")} is sorted.
"""


BUBBLE_SORT = _BubbleSort(
    key=DefinitionKey(
        name="bubble_sort",
        field=FieldName.MATHEMATICS,
    )
)
