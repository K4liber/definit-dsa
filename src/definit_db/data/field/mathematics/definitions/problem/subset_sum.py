from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _SubsetSum(Definition):
    def _get_content(self) -> str:
        return f"""
A decision {PROBLEM.key.get_reference()} that asks: given a 
{SET.key.get_reference()} of {INTEGER.key.get_reference("integers")} and a target 
{NUMBER.key.get_reference()} T, does there exist a subset that sums exactly to T?

---

{SET.key.get_reference()} S = {{3, 1, 4, 1, 5}},  target T = 9

Check whether any subset of S sums to 9:

  {{3, 1, 5}} → 3 + 1 + 5 = 9  ✓

Answer: yes. The subset {{3, 1, 5}} (and also {{4, 5}}) is a witness.

Counter-example: S = {{2, 4, 6}},  T = 5 → no subset sums to 5, answer: no.
"""


SUBSET_SUM = _SubsetSum(
    key=DefinitionKey(
        name="subset sum",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["subset-sum problem"],
)
