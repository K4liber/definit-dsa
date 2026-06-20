from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.analysis.upper_bound import UPPER_BOUND
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION


class _BigONotation(Definition):
    def _get_content(self) -> str:
        return f"""
A mathematical notation used to describe the {ASYMPTOTIC_BEHAVIOR.key.get_reference()} of a 
{FUNCTION.key.get_reference()}, particularly the {UPPER_BOUND.key.get_reference()} of 
{TIME_COMPLEXITY.key.get_reference()} or {SPACE_COMPLEXITY.key.get_reference()} as the input size grows. 
Big O notation characterizes the worst-case growth rate, allowing comparison of algorithm efficiency 
independent of implementation details.

---

Example Big O classes:

  O(1)      — constant:    accessing an element by index in an array
  O(n)      — linear:      scanning every element once (e.g. linear search)

Big O drops constant factors and lower-order terms. An algorithm that performs 3n + 7 operations
is O(n), not O(3n + 7), because for large n the leading term dominates:

  n = 1 000 000:  3n + 7 = 3 000 007  ≈  3n

The notation captures growth rate, not exact operation count.
"""


BIG_O_NOTATION = _BigONotation(
    key=DefinitionKey(
        name="big_o_notation",
        field=FieldName.MATHEMATICS,
    )
)
