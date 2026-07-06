from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.map import MAP
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _CharacterEncoding(Definition):
    def _get_content(self) -> str:
        return f"""
A method of representing {CHARACTER.key.get_reference(phrase="characters")} as numerical values, allowing computers to 
store and manipulate text. Character encoding schemes define the {MAP.key.get_reference(phrase="mapping")} between 
characters and their corresponding {NUMBER.key.get_reference(phrase="numerical")} values.
"""


CHARACTER_ENCODING = _CharacterEncoding(
    key=DefinitionKey(
        name="character_encoding",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
