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
{ITEM.key.get_reference(phrase="item")} at position i equals the item at position n-1-i. For 
example, a sequence (1, 2, 3, 2, 1) or the string "racecar" are palindromes.
"""


PALINDROME = _Palindrome(
    key=DefinitionKey(
        name="palindrome",
        field=FieldName.MATHEMATICS,
    )
)
