from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Efficiency(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is how well a method uses resources to achieve a result.

In {ALGORITHM.key.get_reference("algorithm")} analysis, efficiency is typically described using 
{TIME_COMPLEXITY.key.get_reference("time complexity")} and 
{SPACE_COMPLEXITY.key.get_reference("space complexity")}.

---

To find a target {NUMBER.key.get_reference(phrase="number")} in a sorted sequence, one 
{ALGORITHM.key.get_reference()} checks every number one by one, while another repeatedly halves the search range; 
the second is more efficient because its {TIME_COMPLEXITY.key.get_reference("time complexity")} grows far more 
slowly as the sequence gets larger.
"""


EFFICIENCY = _Efficiency(
    key=DefinitionKey(
        name="efficiency",
        field=FieldName.MATHEMATICS,
    )
)
