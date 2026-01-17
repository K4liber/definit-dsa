from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _BestCase(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is the minimum {TIME_COMPLEXITY.key.get_reference("time complexity")} an
{ALGORITHM.key.get_reference()} can take for some {INPUT_DATA.key.get_reference("input")} of a given size.

It describes the most favorable inputs or {CRITERION.key.get_reference("conditions")} under which the algorithm
performs as fast as possible.
"""


BEST_CASE = _BestCase(
    key=DefinitionKey(
        name="best case",
        field=FieldName.MATHEMATICS,
    )
)
