from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _BinarySearch(Definition):
    def _get_content(self) -> str:
        return f"""
Binary Search is an {ALGORITHM.key.get_reference()} that finds the position of a target value 
within a {SEQUENCE.key.get_reference("sequence")} by repeatedly dividing the search interval in half. 
Binary search requires the {SEQUENCE.key.get_reference("sequence")} to be {SORTING.key.get_reference(phrase="sorted")}. 
At each step it compares the target with the middle element of the interval and then continues 
the search on the left or right half, effectively using a {DIVIDE_AND_CONQUER.key.get_reference()} approach.

---

Searching for 9 in the {SEQUENCE.key.get_reference("sequence")} [1, 3, 5, 7, 9, 11, 13]:

  Step 1: interval [1..13], mid = 7.  9 > 7 → search right half [9, 11, 13]
  Step 2: interval [9..13], mid = 11. 9 < 11 → search left half [9]
  Step 3: interval [9..9],  mid = 9.  9 = 9 → found ✓
"""


BINARY_SEARCH = _BinarySearch(
    key=DefinitionKey(
        name="binary_search",
        field=FieldName.MATHEMATICS,
    )
)
