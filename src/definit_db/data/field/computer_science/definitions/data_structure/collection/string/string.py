from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _String(Definition):
    def _get_content(self) -> str:
        return f"""
A {SEQUENCE.key.get_reference(phrase="sequence")} of {CHARACTER.key.get_reference(phrase="characters")}, typically 
used to represent text. Strings can be of variable length and can contain letters, 
{NUMBER.key.get_reference(phrase="numbers")}, symbols, and whitespace.

---

The text `Hello` is a string made up of the characters `H`, `e`, `l`, `l`, `o` in that order. To store it, a 
{CHARACTER_ENCODING.key.get_reference(phrase="character encoding")} assigns each character a numerical value; for 
example, `H` may map to 72 and `e` to 101, so the string is recorded as the corresponding sequence of numbers and 
can later be decoded back into the original text.
"""


STRING = _String(
    key=DefinitionKey(
        name="string",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=["character string"],
)
