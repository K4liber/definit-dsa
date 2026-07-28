from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.fibonacci import FIBONACCI
from definit_db.data.field.mathematics.definitions.fundamental.iteration import ITERATION
from definit_db.data.field.mathematics.definitions.problem.base_case import BASE_CASE
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _BottomUpApproach(Definition):
    def _get_content(self) -> str:
        return f"""
A {ALGORITHM.key.get_reference()} design approach that constructs {SOLUTION.key.get_reference("solutions")} 
to a {PROBLEM.key.get_reference()} by first solving its smaller {SUBPROBLEM.key.get_reference("subproblems")} 
and then combining those solutions to form a solution to the original problem. The bottom-up approach often avoids 
{RECURSION.key.get_reference()} by {ITERATION.key.get_reference("iteratively")} building up answers from the {BASE_CASE.key.get_reference("base cases")}.

---

To compute the 5th term of the {FIBONACCI.key.get_reference()} sequence, a bottom-up approach starts from the 
{BASE_CASE.key.get_reference("base cases")} "F0 = 0" and "F1 = 1", then iteratively computes "F2 = 1", "F3 = 2", 
"F4 = 3", and "F5 = 5", reusing each previously computed {SOLUTION.key.get_reference("solution")} instead of 
{RECURSION.key.get_reference("recursing")} back into smaller {SUBPROBLEM.key.get_reference("subproblems")}.
"""


BOTTOM_UP_APPROACH = _BottomUpApproach(
    key=DefinitionKey(
        name="bottom_up_approach",
        field=FieldName.MATHEMATICS,
    )
)
