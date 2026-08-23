from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.right_shift import RIGHT_SHIFT
from definit_db.data.field.computer_science.definitions.fundamental.twos_complement import TWOS_COMPLEMENT
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER


class _ArithmeticRightShift(Definition):
    def _get_content(self) -> str:
        return f"""
A {BITWISE_OPERATION.key.get_reference("bitwise operation")} 
and a variant of {RIGHT_SHIFT.key.get_reference("right shift")} that preserves the sign 
{BIT.key.get_reference()} when shifting signed {INTEGER.key.get_reference("integers")}. 
Instead of filling the leftmost positions with zeros, it replicates the sign bit, 
maintaining the correct sign for negative numbers in {TWOS_COMPLEMENT.key.get_reference()} 
representation. This {OPERATION.key.get_reference()} effectively performs signed integer 
division by powers of 2.

---

The 8-bit value 10110100 (-76 in two's complement) shifted right by two with arithmetic shift 
gives 11101101 (-19): two copies of the sign bit (1) enter from the left, preserving the negative sign, and the 
result is exactly -76 // 4. A logical shift on the same bits would instead produce 00101101 (45), losing the sign.
"""


ARITHMETIC_RIGHT_SHIFT = _ArithmeticRightShift(
    DefinitionKey(name="arithmetic right shift", field=FieldName.COMPUTER_SCIENCE),
    aliases=("signed right shift", "SAR"),
)
