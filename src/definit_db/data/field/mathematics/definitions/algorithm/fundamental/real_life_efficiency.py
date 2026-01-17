from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_world_performance import (
    REAL_WORLD_PERFORMANCE,
)
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _RealLifeEfficiency(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is {EFFICIENCY.key.get_reference("efficiency")} as observed in practice.

It is closely related to {REAL_WORLD_PERFORMANCE.key.get_reference("real-world performance")}, 
and depends on factors such as the implementation, constant factors, and typical 
{INPUT_DATA.key.get_reference("inputs")}.
"""


REAL_LIFE_EFFICIENCY = _RealLifeEfficiency(
    key=DefinitionKey(
        name="real-life efficiency",
        field=FieldName.MATHEMATICS,
    )
)
