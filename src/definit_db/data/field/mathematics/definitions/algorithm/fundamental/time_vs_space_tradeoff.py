from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.asymptotic_runtime import ASYMPTOTIC_RUNTIME
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY


class _TimeVsSpaceTradeOff(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is a common design trade-off where improving 
{TIME_COMPLEXITY.key.get_reference("time complexity")} usually requires using more 
{SPACE_COMPLEXITY.key.get_reference("space complexity")}, and reducing memory usage may increase
{ASYMPTOTIC_RUNTIME.key.get_reference("runtime")}.
"""


TIME_VS_SPACE_TRADE_OFF = _TimeVsSpaceTradeOff(
    key=DefinitionKey(
        name="time vs space trade-off",
        field=FieldName.MATHEMATICS,
    )
)
