from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.brute_force import BRUTE_FORCE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_world_performance import (
    REAL_WORLD_PERFORMANCE,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.problem.overlapping_subproblems import OVERLAPPING_SUBPROBLEMS


class _Bud(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
An {OPTIMIZATION.key.get_reference()} framework for improving 
{ALGORITHM.key.get_reference("algorithms")} by identifying and addressing three types of inefficiencies: Bottlenecks 
(the slowest parts that limit overall {REAL_WORLD_PERFORMANCE.key.get_reference("performance")}), Unnecessary work 
({OPERATION.key.get_reference("operations")} that can be eliminated without affecting the result), and Duplicated 
work (redundant {COMPUTATION.key.get_reference("computations")} that can be avoided by reusing previously computed 
results). By systematically examining these three areas, BUD helps identify opportunities for 
{REAL_WORLD_PERFORMANCE.key.get_reference("performance")} improvement.

---

A {BRUTE_FORCE.key.get_reference("brute-force")} routine that searches for a duplicate value in a list by comparing 
every element with every other element can be improved by applying BUD: the nested 
comparison loop is the bottleneck, re-checking pairs that were already ruled out is unnecessary work, and rescanning 
the list from the start for each element revisits the same 
{OVERLAPPING_SUBPROBLEMS.key.get_reference("overlapping subproblem")}, which is duplicated work. Replacing the nested 
loop with a single pass that remembers previously seen elements removes all three inefficiencies and lowers the 
{TIME_COMPLEXITY.key.get_reference()} of the routine.
"""


BUD = _Bud(DefinitionKey(name="BUD", field=FieldName.MATHEMATICS))
