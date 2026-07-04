from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.and_operator import AND_OPERATOR
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Bitmask(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {BINARY_REPRESENTATION.key.get_reference(phrase="binary representation")} pattern 
whose {BIT.key.get_reference(phrase="bits")} are used with 
{BITWISE_OPERATION.key.get_reference(phrase="bitwise operations")} to select, set, clear, toggle, or test corresponding 
bits in another {NUMBER.key.get_reference(phrase="value")}.

---

The bitmask 0010 can be combined with a bitwise {AND_OPERATOR.key.get_reference(phrase="AND operation")} on 0110 to 
test whether bit 1 is set: 0010 AND 0110 = 0010, which is nonzero, so bit 1 of 0110 is set.
"""


BITMASK = _Bitmask(
    key=DefinitionKey(
        name="bitmask",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
