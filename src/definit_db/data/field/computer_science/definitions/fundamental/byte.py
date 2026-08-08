from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _Byte(Definition):
    def _get_content(self) -> str:
        return f"""
A unit of digital {INFORMATION.key.get_reference(phrase="information")} consisting of eight 
{BIT.key.get_reference(phrase="bits")}. A byte is the smallest addressable unit of 
{COMPUTER_MEMORY.key.get_reference(phrase="memory")} in most {COMPUTER.key.get_reference(phrase="computer")} 
architectures and is commonly used to represent a single {CHARACTER.key.get_reference(phrase="character")} of text.

---

A single byte can store 256 distinct values (2^8), ranging from 00000000 to 11111111 in 
{BINARY_REPRESENTATION.key.get_reference(phrase="binary")}. For example, the byte 01000001 represents the decimal 
value 65, which corresponds to the character `A` in ASCII.
"""


BYTE = _Byte(
    key=DefinitionKey(
        name="byte",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
