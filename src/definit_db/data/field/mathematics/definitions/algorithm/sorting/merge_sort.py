from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION


class _MergeSort(Definition):
    def _get_content(self) -> str:
        return f"""
MergeSort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that uses a 
{DIVIDE_AND_CONQUER.key.get_reference()} approach: it divides the input 
{SEQUENCE.key.get_reference("sequence")} into two halves, {RECURSION.key.get_reference("recursively")} sorts each 
half, and then merges the two sorted halves into a single sorted {SEQUENCE.key.get_reference("sequence")}. 

---

Sort [5, 2, 8, 1]:

Divide:
  [5, 2, 8, 1]  →  [5, 2]  and  [8, 1]
  [5, 2]        →  [5]     and  [2]      ← base cases
  [8, 1]        →  [8]     and  [1]      ← base cases

Merge (bottom-up):
  [5] + [2]:  2 < 5 → take 2; take 5                       →  [2, 5]
  [8] + [1]:  1 < 8 → take 1; take 8                       →  [1, 8]
  [2, 5] + [1, 8]:
    2 vs 1 → take 1  →  [1]
    2 vs 8 → take 2  →  [1, 2]
    5 vs 8 → take 5  →  [1, 2, 5]
    take 8           →  [1, 2, 5, 8]

Result: [1, 2, 5, 8]
"""


MERGE_SORT = _MergeSort(
    key=DefinitionKey(
        name="merge_sort",
        field=FieldName.MATHEMATICS,
    )
)
