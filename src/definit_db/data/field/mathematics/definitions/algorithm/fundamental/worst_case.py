from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _WorstCase(Definition):
    def _get_content(self) -> str:
        return f"""
The maximum {TIME_COMPLEXITY.key.get_reference("time complexity")} an
{ALGORITHM.key.get_reference()} can take over all {INPUT_DATA.key.get_reference("inputs")} of a given size.

It describes the least favorable inputs or {CRITERION.key.get_reference("conditions")} under which the algorithm
performs as slowly as possible.

---

For an {ALGORITHM.key.get_reference()} that searches a {SEQUENCE.key.get_reference()} of "100" 
{INPUT_DATA.key.get_reference("items")} one by one for a target value, the worst case occurs when the target is the 
last item checked or absent from the sequence, giving a {TIME_COMPLEXITY.key.get_reference()} of "100" comparisons.
"""


WORST_CASE = _WorstCase(
    key=DefinitionKey(
        name="worst case",
        field=FieldName.MATHEMATICS,
    )
)
