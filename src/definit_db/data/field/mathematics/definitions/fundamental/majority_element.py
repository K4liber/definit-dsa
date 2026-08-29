from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _MajorityElement(Definition):
    def _get_content(self) -> str:
        return f"""
An {ITEM.key.get_reference(phrase="element")} in a {SEQUENCE.key.get_reference(phrase="sequence")} that appears 
more than half the total {NUMBER.key.get_reference(phrase="number")} of times. Formally, given a sequence of n elements, a majority element is one that 
occurs more than n/2 times. A sequence may have at most one majority element.

---

For the sequence (2, 2, 1, 1, 1, 2, 1), which has 7 elements, the item 1 occurs 4 times. Since 4 is more than
7/2 = 3.5, 1 is the majority element of the sequence. The item 2 occurs only 3 times, which is not more than
3.5, so it is not a majority element.
"""


MAJORITY_ELEMENT = _MajorityElement(
    key=DefinitionKey(
        name="majority element",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["majority item"],
)
