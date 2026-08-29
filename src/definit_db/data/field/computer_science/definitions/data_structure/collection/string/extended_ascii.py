from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.ascii import ASCII
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT


class _ExtendedAscii(Definition):
    def _get_content(self) -> str:
        return f"""
An extension of the {ASCII.key.get_reference(phrase="ASCII")} 
{CHARACTER_ENCODING.key.get_reference(phrase="character encoding")} standard that uses 8 
{BIT.key.get_reference(phrase="bits")} to represent 256 {CHARACTER.key.get_reference(phrase="characters")}, including 
additional symbols and characters from various languages.

---

The first 128 code points match ASCII exactly, so the value 65 still represents `A`. The remaining 128 code points 
(values 128-255) are used for additional symbols, such as accented letters and box-drawing characters.
"""


EXTENDED_ASCII = _ExtendedAscii(
    key=DefinitionKey(
        name="extended_ascii",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=("high ASCII",),
)
