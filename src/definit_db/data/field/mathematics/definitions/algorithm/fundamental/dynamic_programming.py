from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.optimal_substructure import OPTIMAL_SUBSTRUCTURE
from definit_db.data.field.mathematics.definitions.problem.overlapping_subproblems import OVERLAPPING_SUBPROBLEMS
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _DynamicProgramming(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {ALGORITHM.key.get_reference()} that solves a {PROBLEM.key.get_reference()} by breaking it down into 
simpler {SUBPROBLEM.key.get_reference("subproblems")} and storing their {SOLUTION.key.get_reference("solutions")} 
to avoid redundant computations. Dynamic programming is particularly {EFFICIENCY.key.get_reference("efficient")} 
for problems that exhibit {OVERLAPPING_SUBPROBLEMS.key.get_reference()} and {OPTIMAL_SUBSTRUCTURE.key.get_reference()}, 
enabling the construction of an {OPTIMAL_SOLUTION.key.get_reference("optimal solution")} by reusing previously 
computed results.

---

To compute the {NUMBER.key.get_reference(phrase="number")} at position "5" in the sequence "1", "1", "2", "3", "5" 
where each number is the sum of the previous two, dynamic programming stores the 
{SOLUTION.key.get_reference()} of each {SUBPROBLEM.key.get_reference()}, each earlier position, once and reuses 
it, so position "3" is computed a single time instead of repeatedly.
"""


DYNAMIC_PROGRAMMING = _DynamicProgramming(
    key=DefinitionKey(
        name="dynamic_programming",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("DP",),
)
