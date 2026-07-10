from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS


class _Unicode(Definition):
    def _get_content(self) -> str:
        return f"""
A {CHARACTER_ENCODING.key.get_reference(phrase="character encoding")} standard that aims to provide a 
{UNIQUENESS.key.get_reference(phrase="unique")} {NUMBER.key.get_reference(phrase="number")} for every 
{CHARACTER.key.get_reference()}, regardless of the system.

---

Each character is assigned a code point, written as U+ followed by a hexadecimal number. For example, `A` is 
assigned U+0041, the digit `0` is U+0030, and the symbol `€` is U+20AC. No two characters share the same code point.
"""


UNICODE = _Unicode(
    key=DefinitionKey(
        name="unicode",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
