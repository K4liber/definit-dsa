from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.fundamental.fibonacci import FIBONACCI
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.overlapping_subproblems import OVERLAPPING_SUBPROBLEMS
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _Memoization(Definition):
    def _get_content(self) -> str:
        return f"""
An {OPTIMIZATION.key.get_reference()} technique that stores the results of expensive {FUNCTION.key.get_reference()} 
calls and returns the stored result when the same inputs occur again. memoization is particularly 
effective for {RECURSION.key.get_reference("recursive")} {FUNCTION.key.get_reference("functions")} with 
{OVERLAPPING_SUBPROBLEMS.key.get_reference()}, where the same {SUBPROBLEM.key.get_reference("subproblems")} are 
computed multiple times. By storing previously computed {SOLUTION.key.get_reference("solutions")}, memoization 
significantly reduces redundant computations and improves performance.

---

Computing the {FIBONACCI.key.get_reference()} term "F30" through naive {RECURSION.key.get_reference("recursion")} 
recomputes "F28" many times, since every call to "Fn" independently calls "Fn-1" and "Fn-2". 
Memoization stores each "Fn" the first time it is computed, so later calls with the 
same "n" return the stored value instead of repeating the recursive calls.
"""


MEMOIZATION = _Memoization(
    key=DefinitionKey(
        name="memoization",
        field=FieldName.MATHEMATICS,
    )
)
