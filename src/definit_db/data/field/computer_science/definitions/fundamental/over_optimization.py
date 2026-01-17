from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_world_performance import (
    REAL_WORLD_PERFORMANCE,
)


class _OverOptimization(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the act of applying {OPTIMIZATION.key.get_reference()} 
beyond what is justified by the requirements.

Over-optimization can make a {PROGRAM.key.get_reference()} harder to understand and maintain, 
and may not yield meaningful {REAL_WORLD_PERFORMANCE.key.get_reference("performance")} benefits.
"""


OVER_OPTIMIZATION = _OverOptimization(
    key=DefinitionKey(
        name="over-optimization",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
