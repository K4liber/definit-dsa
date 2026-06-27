from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _PatienceSorting(Definition):
    def _get_content(self) -> str:
        return f"""
Patience sorting is a {SORTING.key.get_reference(phrase="sorting")} {ALGORITHM.key.get_reference()} that processes
a {SEQUENCE.key.get_reference(phrase="sequence")} by dealing its elements into piles: each element is placed on the
leftmost pile whose top is greater than or equal to the element. If no such pile exists, a new pile is
started. The piles are then merged to produce the sorted sequence.

---

Sorting [4, 2, 3, 1]:

  Place 4 → pile 1: [4]          tops: [4]
  Place 2 → pile 1 top 4 ≥ 2  → pile 1: [4,2]     tops: [2]
  Place 3 → pile 1 top 2 < 3  → new pile 2: [3]    tops: [2, 3]
  Place 1 → pile 1 top 2 ≥ 1  → pile 1: [4,2,1]   tops: [1, 3]

  Merge by repeatedly taking the smallest top: 1, 2, 3, 4  →  [1, 2, 3, 4]  ✓
"""


PATIENCE_SORTING = _PatienceSorting(
    key=DefinitionKey(
        name="Patience sorting",
        field=FieldName.MATHEMATICS,
    )
)
