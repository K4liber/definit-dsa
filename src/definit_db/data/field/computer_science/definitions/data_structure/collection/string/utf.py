from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.unicode import UNICODE
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER


class _Utf(Definition):
    def _get_content(self) -> str:
        return f"""
UTF (Unicode Transformation Format) is a {CHARACTER_ENCODING.key.get_reference(phrase="character encoding")} 
standard that represents {UNICODE.key.get_reference(phrase="Unicode")} {CHARACTER.key.get_reference(phrase="characters")} using variable-length sequences 
of bytes.
"""


UTF = _Utf(
    key=DefinitionKey(
        name="utf",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
