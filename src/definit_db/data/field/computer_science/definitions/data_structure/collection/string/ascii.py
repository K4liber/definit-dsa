from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT


class _Ascii(Definition):
    def _get_content(self) -> str:
        return f"""
ASCII is a {CHARACTER_ENCODING.key.get_reference(phrase="character encoding")} standard that uses 7 
{BIT.key.get_reference(phrase="bits")} to represent 128 {CHARACTER.key.get_reference(phrase="characters")}, including letters, digits, punctuation marks, 
and control characters.
"""


ASCII = _Ascii(
    key=DefinitionKey(
        name="ascii",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
