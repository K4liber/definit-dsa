from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.asymptotic_runtime import ASYMPTOTIC_RUNTIME
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION


class _TimeVsSpaceTradeOff(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is a common design trade-off where improving 
{TIME_COMPLEXITY.key.get_reference("time complexity")} usually requires using more 
{SPACE_COMPLEXITY.key.get_reference("space complexity")}, and reducing memory usage may increase
{ASYMPTOTIC_RUNTIME.key.get_reference("runtime")}.

---

Suppose we need to answer many queries of the form "is value x in this fixed {COLLECTION.key.get_reference()}?"

Option A — recompute on every query (time-heavy):
  Extra {SPACE_COMPLEXITY.key.get_reference("space")}: O(1)
  Time per query: O(n)  — scan all n values each time

Option B — precompute a lookup table (space-heavy):
  Extra {SPACE_COMPLEXITY.key.get_reference("space")}: O(n)  — store every value up front
  Time per query: O(1)  — direct lookup

Spending O(n) extra {SPACE_COMPLEXITY.key.get_reference("memory")} (option B) reduces each query from O(n) to O(1). 
Which option is better depends on whether memory or speed is the bottleneck for the given problem.
"""


TIME_VS_SPACE_TRADE_OFF = _TimeVsSpaceTradeOff(
    key=DefinitionKey(
        name="time vs space trade-off",
        field=FieldName.MATHEMATICS,
    )
)
