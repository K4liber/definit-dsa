from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER


class _RightShift(Definition):
    def _get_content(self) -> str:
        return f"""
A {BITWISE_OPERATION.key.get_reference("bitwise operation")} 
that shifts all {BIT.key.get_reference("bits")} in a 
{BINARY_REPRESENTATION.key.get_reference("binary representation")} to the right by a 
specified number of positions. Right shift by one position is equivalent to 
{INTEGER.key.get_reference()} division by 2.

---

Shifting the 8-bit value 11001100 (204) right by two positions yields 00110011 (51), which is exactly 204 // 4.
The two rightmost bits are discarded; what fills the vacated positions on the left depends on which variant of
right shift is used.
"""


RIGHT_SHIFT = _RightShift(DefinitionKey(name="right shift", field=FieldName.COMPUTER_SCIENCE))
