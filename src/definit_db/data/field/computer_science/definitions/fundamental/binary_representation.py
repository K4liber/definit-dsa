from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _BinaryRepresentation(Definition):
    def _get_content(self) -> str:
        return f"""
A way of expressing {INFORMATION.key.get_reference()} using only two symbols, 
typically 0 and 1. In this system, each digit is called a {BIT.key.get_reference()}, and 
{SEQUENCE.key.get_reference("sequences")} of bits are used to represent {NUMBER.key.get_reference("numbers")} 
and other types of information.

---

The number 13 has the binary representation 1101: reading the bits from left to right as powers of two gives
1x2^3 + 1x2^2 + 0x2^1 + 1x2^0 = 8 + 4 + 0 + 1 = 13.
"""


BINARY_REPRESENTATION = _BinaryRepresentation(
    DefinitionKey(name="binary representation", field=FieldName.COMPUTER_SCIENCE),
    aliases=("base-2 representation",),
)
