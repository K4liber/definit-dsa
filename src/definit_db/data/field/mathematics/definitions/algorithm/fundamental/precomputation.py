from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_vs_space_tradeoff import (
    TIME_VS_SPACE_TRADE_OFF,
)
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Precomputation(Definition):
    def _get_content(self) -> str:
        return f"""
A technique where some results are computed in advance and stored, so they can be
reused later to reduce computation time.

Precomputation often improves {TIME_COMPLEXITY.key.get_reference("time complexity")} at the cost of higher
{SPACE_COMPLEXITY.key.get_reference("space complexity")}, illustrating a 
{TIME_VS_SPACE_TRADE_OFF.key.get_reference()}.

---

Given the {SEQUENCE.key.get_reference()} [3, 1, 4, 1, 5], suppose we need to answer many queries
of the form "what is the sum of elements from index i to index j?"

Without precomputation: add up each element between i and j on every query → O(n) per query.

With precomputation — store prefix sums P where P[k] = sum of the first k elements:

  P = [0, 3, 4, 8, 9, 14]

Any range sum is then a single {OPERATION.key.get_reference()}: sum(i, j) = P[j+1] - P[i] → O(1) per query.

For example, sum of elements at indices 1 to 3 = P[4] - P[1] = 9 - 3 = 6  ✓  (1 + 4 + 1 = 6)

The precomputed array costs O(n) extra {SPACE_COMPLEXITY.key.get_reference("space")} but reduces each query's
{TIME_COMPLEXITY.key.get_reference("time complexity")} from O(n) to O(1).
"""


PRECOMPUTATION = _Precomputation(
    key=DefinitionKey(
        name="precomputation",
        field=FieldName.MATHEMATICS,
    )
)
