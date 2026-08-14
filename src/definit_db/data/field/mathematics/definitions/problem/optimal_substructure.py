from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _OptimalSubstructure(Definition):
    def _get_content(self) -> str:
        return f"""
A {PROBLEM.key.get_reference(phrase="problem")} is said to have optimal substructure if an 
{OPTIMAL_SOLUTION.key.get_reference(phrase="optimal solution")} can be constructed from optimal solutions of its 
{SUBPROBLEM.key.get_reference(phrase="subproblems")}.

---

The {PROBLEM.key.get_reference(phrase="problem")} of finding the largest of the 
{NUMBER.key.get_reference(phrase="numbers")} "2", "9", and "4" has optimal substructure: its 
{OPTIMAL_SOLUTION.key.get_reference(phrase="optimal solution")} "9" is the larger of "2" and the optimal solution 
of the {SUBPROBLEM.key.get_reference(phrase="subproblem")} "find the largest of "9" and "4"".
"""


OPTIMAL_SUBSTRUCTURE = _OptimalSubstructure(
    key=DefinitionKey(
        name="optimal_substructure",
        field=FieldName.MATHEMATICS,
    )
)
