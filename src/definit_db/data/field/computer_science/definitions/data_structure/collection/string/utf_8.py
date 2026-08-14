from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.ascii import ASCII
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.unicode import UNICODE
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.utf import UTF
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.byte import BYTE


class _Utf8(Definition):
    def _get_content(self) -> str:
        return f"""
A {UTF.key.get_reference(phrase="UTF")} {CHARACTER_ENCODING.key.get_reference(phrase="character encoding")} 
scheme that uses 8-{BIT.key.get_reference(phrase="bit")} code units, meaning each unit is one 
{BYTE.key.get_reference(phrase="byte")}. A 
{UNICODE.key.get_reference(phrase="Unicode")} {CHARACTER.key.get_reference(phrase="character")} is encoded as 1 to 4 
such units. It is backward compatible with {ASCII.key.get_reference(phrase="ASCII")} and can represent any character 
in the Unicode standard.

---

The character `A` (code point U+0041) is encoded as a single 8-bit unit, matching its ASCII representation. The 
character `€` (code point U+20AC) is encoded as three units, while rarer characters may need up to four units.
"""


UTF_8 = _Utf8(
    key=DefinitionKey(
        name="utf_8",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
