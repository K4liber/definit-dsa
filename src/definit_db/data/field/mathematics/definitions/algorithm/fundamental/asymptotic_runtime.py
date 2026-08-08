from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.asymptotic_efficiency import (
    ASYMPTOTIC_EFFICIENCY,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _AsymptoticRuntime(Definition):
    def _get_content(self) -> str:
        return f"""
A time-focused case of {ASYMPTOTIC_EFFICIENCY.key.get_reference("asymptotic efficiency")} for an 
{ALGORITHM.key.get_reference()} as {INPUT_DATA.key.get_reference("input")} size grows, 
ignoring constant factors and lower-order terms.

It is typically expressed as a {BIG_O_NOTATION.key.get_reference("Big O")} 
{TIME_COMPLEXITY.key.get_reference("time complexity")} that describes the 
{ASYMPTOTIC_BEHAVIOR.key.get_reference("asymptotic")} growth of the runtime.

---

An {ALGORITHM.key.get_reference()} performs exactly 5n² + 3n + 100 {OPERATION.key.get_reference("operations")} 
for an {INPUT_DATA.key.get_reference()} of size n.

Its asymptotic runtime is O(n²): the constant factor 5, the lower-order term 3n, and the
constant 100 are all dropped because for large n the n² term dominates:

When n = 10, total work is 5(100) + 3(10) + 100 = 630, and the n² term contributes about 79%.

When n = 100, total work is 5(10 000) + 300 + 100 = 50 400, and the n² term contributes about 99%.

When n = 1 000, total work is about 5(1 000 000) + ..., which is about 5 000 000, and the n² term contributes 
more than 99.9%.

For large n, only the growth rate of the leading term matters — hence O(n²).
"""


ASYMPTOTIC_RUNTIME = _AsymptoticRuntime(
    key=DefinitionKey(
        name="asymptotic runtime",
        field=FieldName.MATHEMATICS,
    )
)
