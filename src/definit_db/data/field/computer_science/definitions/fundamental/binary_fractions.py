from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _BinaryFractions(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A way to represent fractional {NUMBER.key.get_reference("numbers")} 
using {BINARY_REPRESENTATION.key.get_reference("binary representation")}. In binary fractions, 
{BIT.key.get_reference("bits")} to the right of a binary point represent negative powers of 2 
(1/2, 1/4, 1/8, etc.), similar to how digits after a decimal point in base-10 represent 
negative powers of 10.

---

The binary fraction 0.101 represents 1/2 + 0/4 + 1/8 = 5/8.
"""


BINARY_FRACTIONS = _BinaryFractions(DefinitionKey(name="binary fractions", field=FieldName.COMPUTER_SCIENCE))
