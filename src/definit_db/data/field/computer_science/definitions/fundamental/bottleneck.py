from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_world_performance import (
    REAL_WORLD_PERFORMANCE,
)
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT


class _Bottleneck(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a part of a system that limits overall
{REAL_WORLD_PERFORMANCE.key.get_reference("performance")} because it is the slowest or most
{CONSTRAINT.key.get_reference("constrained")} step.

In {ALGORITHM.key.get_reference("algorithm")} analysis, a bottleneck is often the
{OPERATION.key.get_reference("operation")} that dominates the
{COMPLEXITY.key.get_reference("complexity")}.

---

An algorithm first sorts a list of n elements in {BIG_O_NOTATION.key.get_reference(phrase="O(n log n)")} time, then 
scans it once in {BIG_O_NOTATION.key.get_reference(phrase="O(n)")} time. The sorting step is the bottleneck, since its 
complexity grows faster than the scanning step as n increases, so it dominates the algorithm's overall running time.
"""


BOTTLENECK = _Bottleneck(
    key=DefinitionKey(
        name="bottleneck",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
