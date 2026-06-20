from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR


class _AsymptoticRuntime(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is the theoretical running time of an algorithm as the input size grows,
ignoring constant factors and lower-order terms.

It is typically expressed as a {BIG_O_NOTATION.key.get_reference("Big O")} 
{TIME_COMPLEXITY.key.get_reference("time complexity")} that describes the 
{ASYMPTOTIC_BEHAVIOR.key.get_reference("asymptotic")} growth of the runtime.

---

An algorithm performs exactly 5n² + 3n + 100 operations for an input of size n.

Its asymptotic runtime is O(n²): the constant factor 5, the lower-order term 3n, and the
constant 100 are all dropped because for large n the n² term dominates:

  n =    10:  5(100) + 3(10) + 100  =    630   (n² term is 79% of total)
  n =   100:  5(10 000) + 300 + 100 = 50 400   (n² term is 99% of total)
  n = 1 000:  5(1 000 000) + ...    ≈  5 000 000 (n² term is >99.9% of total)

For large n, only the growth rate of the leading term matters — hence O(n²).
"""


ASYMPTOTIC_RUNTIME = _AsymptoticRuntime(
    key=DefinitionKey(
        name="asymptotic runtime",
        field=FieldName.MATHEMATICS,
    )
)
