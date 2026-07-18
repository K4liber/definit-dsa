from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR


class _AsymptoticEfficiency(Definition):
    def _get_content(self) -> str:
        return f"""
A notion of {EFFICIENCY.key.get_reference("efficiency")} that focuses on the 
{ASYMPTOTIC_BEHAVIOR.key.get_reference("asymptotic behavior")} of resource usage as input size grows.

It is commonly expressed using {BIG_O_NOTATION.key.get_reference("Big O notation")}.

---

Compare two algorithms: one with O(n) resource usage and one with O(log n):

  n =          10:  O(n) ≈        10 units,  O(log n) ≈  4 units
  n =       1 000:  O(n) ≈     1 000 units,  O(log n) ≈ 10 units
  n = 1 000 000:  O(n) ≈ 1 000 000 units,  O(log n) ≈ 20 units

For small n the difference is negligible. As n grows, it becomes decisive — the O(log n)
algorithm uses a tiny fraction of the resources of the O(n) one. Asymptotic efficiency
captures exactly this: how resource usage scales as n grows without bound.
"""


ASYMPTOTIC_EFFICIENCY = _AsymptoticEfficiency(
    key=DefinitionKey(
        name="asymptotic efficiency",
        field=FieldName.MATHEMATICS,
    )
)
