from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.radix import RADIX
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _RadixSort(Definition):
    def _get_content(self) -> str:
        return f"""
{RADIX.key.get_reference("Radix")} Sort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} that sorts
a {SEQUENCE.key.get_reference("sequence")} of {INTEGER.key.get_reference("integers")}
(or other {OBJECT.key.get_reference(phrase="objects")} that can be represented as integers) by processing
individual digits one position at a time, from least significant digit (LSD) to most or most to least (MSD).

Instead of comparing elements directly, it distributes them into buckets according to the current digit
and then collects them in order. When k (the number of digits) is treated as a constant independent of
n (the number of {ITEM.key.get_reference(phrase="elements")}), radix sort runs in O(n·k) = O(n) time — otherwise O(n·k) 
is no better than comparison-based sorts.

---

Sorting [53, 21, 74, 42, 35] by LSD {RADIX.key.get_reference("radix")} sort:


Pass 1 — sort by ones digit:  [21, 42, 53, 74, 35]

Pass 2 — sort by tens digit:  [21, 35, 42, 53, 74]  ✓
"""


RADIX_SORT = _RadixSort(
    key=DefinitionKey(
        name="radix sort",
        field=FieldName.MATHEMATICS,
    ),
)
