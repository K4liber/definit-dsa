from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _OptimalSolution(Definition):
    def _get_content(self) -> str:
        return f"""
A {SOLUTION.key.get_reference(phrase="solution")} that is the best among all possible solutions, often in terms 
of a specific {CRITERION.key.get_reference(phrase="criterion")}.

---

Consider the {PROBLEM.key.get_reference(phrase="problem")} "choose an even 
{NUMBER.key.get_reference(phrase="number")} from "2", "4", "5", and "7"". Both "2" and "4" are valid 
{SOLUTION.key.get_reference(phrase="solutions")}, since each satisfies the problem. Under the 
{CRITERION.key.get_reference(phrase="criterion")} of picking the largest such number, "4" is the optimal solution.
"""


OPTIMAL_SOLUTION = _OptimalSolution(
    key=DefinitionKey(
        name="optimal_solution",
        field=FieldName.MATHEMATICS,
    )
)
