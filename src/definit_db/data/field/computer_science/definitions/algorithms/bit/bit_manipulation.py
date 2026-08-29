from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION


class _BitManipulation(Definition):
    def _get_content(self) -> str:
        return f"""
A technique that uses {BITWISE_OPERATION.key.get_reference(phrase="bitwise operations")} 
to perform direct {OPERATION.key.get_reference(phrase="operations")} on individual 
{BIT.key.get_reference(phrase="bits")} or groups of {BIT.key.get_reference(phrase="bits")} in a 
{BINARY_REPRESENTATION.key.get_reference(phrase="binary representation")}. It is commonly used in 
{ALGORITHM.key.get_reference(phrase="algorithms")} for tasks like setting, clearing, toggling, or checking specific 
{BIT.key.get_reference(phrase="bits")}, as well as performing {EFFICIENCY.key.get_reference(phrase="efficient")} 
{COMPUTATION.key.get_reference(phrase="computations")}.

---

To check whether the third bit of `1010` is set, a mask `0100` is applied with a bitwise AND: `1010 AND 0100` yields 
`0000`, so the {BIT.key.get_reference("bit")} is 0. To set that same {BIT.key.get_reference("bit")}, 
a mask `0100` is applied with a bitwise OR: `1010 OR 0100` yields 
`1110`, turning the bit on without changing the others.
"""


BIT_MANIPULATION = _BitManipulation(
    DefinitionKey(name="bit manipulation", field=FieldName.COMPUTER_SCIENCE),
    aliases=("bit twiddling",),
)
