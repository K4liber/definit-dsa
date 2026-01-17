from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR


class _AsymptoticEfficiency(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a notion of {EFFICIENCY.key.get_reference("efficiency")} that focuses on the 
{ASYMPTOTIC_BEHAVIOR.key.get_reference("asymptotic behavior")} of resource usage as input size grows.

It is commonly expressed using {BIG_O_NOTATION.key.get_reference("Big O notation")}.
"""


ASYMPTOTIC_EFFICIENCY = _AsymptoticEfficiency(
    key=DefinitionKey(
        name="asymptotic efficiency",
        field=FieldName.MATHEMATICS,
    )
)
