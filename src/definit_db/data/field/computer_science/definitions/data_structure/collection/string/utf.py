from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.unicode import UNICODE
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Utf(Definition):
    def _get_content(self) -> str:
        return f"""
UTF (Unicode Transformation Format) is a {CHARACTER_ENCODING.key.get_reference(phrase="character encoding")} 
standard that represents {UNICODE.key.get_reference(phrase="Unicode")} 
{CHARACTER.key.get_reference(phrase="characters")} using variable-length 
{SEQUENCE.key.get_reference(phrase="sequences")} of bytes.

---

The character `A` (code point U+0041) is represented by a single byte, while `€` (code point U+20AC) requires three 
bytes. Characters with higher code points may need up to four bytes, so the {NUMBER.key.get_reference(phrase="number")} 
of bytes per character varies.
"""


UTF = _Utf(
    key=DefinitionKey(
        name="utf",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
