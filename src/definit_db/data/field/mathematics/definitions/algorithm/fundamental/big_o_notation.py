from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.worst_case import WORST_CASE
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.analysis.upper_bound import UPPER_BOUND
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _BigONotation(Definition):
    def _get_content(self) -> str:
        return f"""
A mathematical notation used to describe the {ASYMPTOTIC_BEHAVIOR.key.get_reference()} of a 
{FUNCTION.key.get_reference()}, particularly the {UPPER_BOUND.key.get_reference()} of 
{TIME_COMPLEXITY.key.get_reference()} or {SPACE_COMPLEXITY.key.get_reference()} as the 
{INPUT_DATA.key.get_reference(phrase="input")} size grows. Big O notation characterizes the 
{WORST_CASE.key.get_reference(phrase="worst-case")} growth rate, allowing comparison of 
{ALGORITHM.key.get_reference(phrase="algorithm")} {EFFICIENCY.key.get_reference()} independent of 
implementation details.

---

Example Big O classes:

O(1) — constant: accessing an {ITEM.key.get_reference(phrase="element")} by {INDEX.key.get_reference(phrase="index")} 
in an array

O(n) — linear: scanning every element once (e.g. linear search)


Big O drops constant factors and lower-order terms. An algorithm that performs 3n + 7 
{OPERATION.key.get_reference(phrase="operations")} is O(n), not O(3n + 7), because for large n the 
leading term dominates:


n = 1 000 000:  3n + 7 = 3 000 007  ≈  3n


The notation captures growth rate, not exact operation count.
"""


BIG_O_NOTATION = _BigONotation(
    key=DefinitionKey(
        name="big_o_notation",
        field=FieldName.MATHEMATICS,
    )
)
