from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_vs_space_tradeoff import (
    TIME_VS_SPACE_TRADE_OFF,
)


class _Precomputation(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a technique where some results are computed in advance and stored, so they can be
reused later to reduce computation time.

Precomputation often improves {TIME_COMPLEXITY.key.get_reference("time complexity")} at the cost of higher
{SPACE_COMPLEXITY.key.get_reference("space complexity")}, illustrating a 
{TIME_VS_SPACE_TRADE_OFF.key.get_reference()}.
"""


PRECOMPUTATION = _Precomputation(
    key=DefinitionKey(
        name="precomputation",
        field=FieldName.MATHEMATICS,
    )
)
