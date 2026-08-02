from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.map import MAP
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _CharacterEncoding(Definition):
    def _get_content(self) -> str:
        return f"""
A method of representing {CHARACTER.key.get_reference(phrase="characters")} as numerical values, allowing
{COMPUTER.key.get_reference(phrase="computers")} to store and manipulate text. Character encoding schemes define the
{MAP.key.get_reference(phrase="mapping")} between characters and their corresponding
{NUMBER.key.get_reference(phrase="numerical")} values.

---

Under one encoding, the {CHARACTER.key.get_reference(phrase="character")} `A` is assigned the number 65, `B` is 
assigned 66, and so on. Storing the text `AB` then means storing the two numbers 65 and 66, which can later be mapped 
back to the original characters.
"""


CHARACTER_ENCODING = _CharacterEncoding(
    key=DefinitionKey(
        name="character_encoding",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
