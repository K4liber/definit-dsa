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
"""


ASYMPTOTIC_RUNTIME = _AsymptoticRuntime(
    key=DefinitionKey(
        name="asymptotic runtime",
        field=FieldName.MATHEMATICS,
    )
)
