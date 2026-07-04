from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.finite_sequence import FINITE_SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _Palindrome(Definition):
    def _get_content(self) -> str:
        return f"""
A {FINITE_SEQUENCE.key.get_reference(phrase="finite sequence")} that reads the same forwards and 
backwards. Formally, a sequence of length n is a palindrome when, for every 
{INDEX.key.get_reference(phrase="index")} i in [0, n-1], the 
{ITEM.key.get_reference(phrase="item")} at position i equals the item at position n-1-i.

---

The sequence (1, 2, 3, 2, 1) has length 5. Comparing items from both ends: position 0 (value 1) matches
position 4 (value 1), and position 1 (value 2) matches position 3 (value 2), so the sequence is a palindrome.

The sequence (1, 2, 3, 4) is not a palindrome, since position 0 (value 1) does not match position 3 (value 4).
"""


PALINDROME = _Palindrome(
    key=DefinitionKey(
        name="palindrome",
        field=FieldName.MATHEMATICS,
    )
)
