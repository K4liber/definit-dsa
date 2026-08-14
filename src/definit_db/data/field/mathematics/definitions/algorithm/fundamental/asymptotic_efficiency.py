from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _AsymptoticEfficiency(Definition):
    def _get_content(self) -> str:
        return f"""
A notion of {EFFICIENCY.key.get_reference("efficiency")} that focuses on the 
{ASYMPTOTIC_BEHAVIOR.key.get_reference("asymptotic behavior")} of resource usage as 
{INPUT_DATA.key.get_reference("input")} size grows.

It is commonly expressed using {BIG_O_NOTATION.key.get_reference("Big O notation")}.

---

Compare two {ALGORITHM.key.get_reference("algorithms")}: one with O(n) resource usage and one with O(log n):

When n = 10: O(n) is about 10 units, while O(log n) is about 4 units.

When n = 1 000: O(n) is about 1 000 units, while O(log n) is about 10 units.

When n = 1 000 000: O(n) is about 1 000 000 units, while O(log n) is about 20 units.

For small n the difference is negligible. As n grows, it becomes decisive — the O(log n)
algorithm uses a tiny fraction of the resources of the O(n) one. Asymptotic efficiency
captures exactly this: how resource usage scales as n grows without {BOUND.key.get_reference(phrase="bound")}.
"""


ASYMPTOTIC_EFFICIENCY = _AsymptoticEfficiency(
    key=DefinitionKey(
        name="asymptotic efficiency",
        field=FieldName.MATHEMATICS,
    )
)
