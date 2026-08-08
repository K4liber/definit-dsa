from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_world_performance import (
    REAL_WORLD_PERFORMANCE,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.loop import LOOP


class _OverOptimization(Definition):
    def _get_content(self) -> str:
        return f"""
The act of applying {OPTIMIZATION.key.get_reference()} 
beyond what is justified by the requirements.

Over-optimization can make a {PROGRAM.key.get_reference()} harder to understand and maintain, 
and may not yield meaningful {REAL_WORLD_PERFORMANCE.key.get_reference("performance")} benefits.

---

A program that processes 100 records per day is over-optimized if a developer rewrites its simple 
{LOOP.key.get_reference(phrase="loop")} into
obfuscated {BITWISE_OPERATION.key.get_reference(phrase="bitwise")} tricks purely to improve the 
{TIME_COMPLEXITY.key.get_reference()} from 
{BIG_O_NOTATION.key.get_reference("O(n)")} to {BIG_O_NOTATION.key.get_reference("O(n/2)")}. The
theoretical gain is negligible at this scale, but the tricks make the code far harder to read, debug, and extend.
"""


OVER_OPTIMIZATION = _OverOptimization(
    key=DefinitionKey(
        name="over-optimization",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
