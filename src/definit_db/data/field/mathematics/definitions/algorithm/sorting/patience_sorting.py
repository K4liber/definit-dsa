from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _PatienceSorting(Definition):
    def _get_content(self) -> str:
        return f"""
Patience sorting is a {SORTING.key.get_reference(phrase="sorting")} {ALGORITHM.key.get_reference()} that processes
a {SEQUENCE.key.get_reference(phrase="sequence")} by dealing its {ITEM.key.get_reference(phrase="elements")} 
into piles: each element is placed on the leftmost pile whose top is greater than or equal to the element. 
If no such pile exists, a new pile is started. The piles are then merged to produce the sorted sequence.

---

Sort [5, 3, 4, 1, 2]:

Step 1 — Deal: place each element on the leftmost pile whose top ≥ it; if none, start a new pile.
Piles are listed bottom → top (rightmost entry is the top, the only value used for placement).


Place 5 → no piles → pile 1: [5] | tops: [5]

Place 3 → top 5 ≥ 3 → pile 1: [5, 3] | tops: [3]

Place 4 → top 3 < 4 → new pile 2: [4] | tops: [3, 4]

Place 1 → top 3 ≥ 1 → pile 1: [5, 3, 1] | tops: [1, 4]

Place 2 → top 1 < 2, top 4 ≥ 2  → pile 2: [4, 2] | tops: [1, 2]


Final piles:  pile 1: [5, 3, 1]   pile 2: [4, 2]


Step 2 — K-way merge: repeatedly extract the smallest top across all piles into the output.


tops [1, 2] → pop 1 from pile 1 → [1] pile 1: [5, 3] | tops: [3, 2]

tops [3, 2] → pop 2 from pile 2 → [1, 2] | pile 2: [4] | tops: [3, 4]

tops [3, 4] → pop 3 from pile 1 → [1, 2, 3] | pile 1: [5] | tops: [5, 4]

tops [5, 4] → pop 4 from pile 2 → [1, 2, 3, 4] | pile 2: [] | tops: [5, -]

tops [5, -] → pop 5 from pile 1 → [1, 2, 3, 4, 5]


Result: [1, 2, 3, 4, 5]  ✓
"""


PATIENCE_SORTING = _PatienceSorting(
    key=DefinitionKey(
        name="Patience sorting",
        field=FieldName.MATHEMATICS,
    )
)
