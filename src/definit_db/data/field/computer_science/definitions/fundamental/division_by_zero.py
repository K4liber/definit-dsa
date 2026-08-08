from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.bug import BUG
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.numeral_system import NUMERAL_SYSTEM


class _DivisionByZero(Definition):
    def _get_content(self) -> str:
        return f"""
A {BUG.key.get_reference(phrase="error")} that occurs when a division {OPERATION.key.get_reference(phrase="operation")} 
is attempted with a divisor of zero. Since division by zero is undefined in standard arithmetic, the result cannot be 
{COMPUTATION.key.get_reference(phrase="computed")}, and the {NUMERAL_SYSTEM.key.get_reference(phrase="number system")} 
has no valid value for it.

---

A {PROGRAM.key.get_reference(phrase="program")} that divides 100 by a variable `count` will trigger 
a division-by-zero error when `count` is 0. Without 
protection, the program crashes at that line; with a guard such as an assertion or a conditional check, the error 
can be caught and handled gracefully instead.
"""


DIVISION_BY_ZERO = _DivisionByZero(
    key=DefinitionKey(
        name="division by zero",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
