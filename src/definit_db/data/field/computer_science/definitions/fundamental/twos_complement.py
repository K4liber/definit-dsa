from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _TwosComplement(Definition):
    def _get_content(self) -> str:
        return f"""
A {BINARY_REPRESENTATION.key.get_reference("binary representation")} method used to 
represent signed {INTEGER.key.get_reference("integers")} in computing. Positive {NUMBER.key.get_reference("numbers")} 
are written in standard binary form, while a negative number is represented by inverting all 
{BIT.key.get_reference("bits")} of its positive counterpart and adding 1. This lets the same hardware circuitry perform 
arithmetic on both positive and negative values, which is why it is the most common way to represent signed integers.

---

In a 4-bit system, +5 is written as `0101`. To represent -5, invert every bit of `0101` to get `1010`, then add 1 to 
obtain `1011`. Reading `1011` as two's complement gives back -5, while the leftmost bit being 1 signals that the value 
is negative. The same addition circuit works for both signs: adding `0101` (+5) and `1011` (-5) yields `0000` with a 
discarded carry, confirming the result is 0.
"""


TWOS_COMPLEMENT = _TwosComplement(
    key=DefinitionKey(
        name="two's complement",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=["2's complement"],
)
