from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY


class _Efficiency(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is how well a method uses resources to achieve a result.

In {ALGORITHM.key.get_reference("algorithm")} analysis, efficiency is typically described using 
{TIME_COMPLEXITY.key.get_reference("time complexity")} and 
{SPACE_COMPLEXITY.key.get_reference("space complexity")}.
"""


EFFICIENCY = _Efficiency(
    key=DefinitionKey(
        name="efficiency",
        field=FieldName.MATHEMATICS,
    )
)
