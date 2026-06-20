from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION


class _QuickSort(Definition):
    def _get_content(self) -> str:
        return f"""
QuickSort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that uses a 
{DIVIDE_AND_CONQUER.key.get_reference()} approach to sort elements. It selects a 'pivot' element, partitions the 
other elements into two sub-{SEQUENCE.key.get_reference("sequences")} according to whether they are less than or 
greater than the pivot, and then {RECURSION.key.get_reference("recursively")} sorts the sub-sequences.

---

Sort [3, 1, 4, 2] by always choosing the last element as the pivot:

[3, 1, 4, 2]  pivot = 2
  left  (< 2): [1]
  right (> 2): [3, 4]

Recursively sort [1]:
  single element → already sorted: [1]

Recursively sort [3, 4]:  pivot = 4
  left  (< 4): [3]
  right (> 4): []
  single elements → already sorted
  combine: [3] + [4] = [3, 4]

Combine all:  [1] + [2] + [3, 4]  =  [1, 2, 3, 4]
"""


QUICK_SORT = _QuickSort(
    key=DefinitionKey(
        name="quick_sort",
        field=FieldName.MATHEMATICS,
    )
)
