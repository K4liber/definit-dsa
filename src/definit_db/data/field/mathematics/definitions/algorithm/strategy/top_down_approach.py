from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.fibonacci import FIBONACCI
from definit_db.data.field.mathematics.definitions.problem.overlapping_subproblems import OVERLAPPING_SUBPROBLEMS
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _TopDownApproach(Definition):
    def _get_content(self) -> str:
        return f"""
A {ALGORITHM.key.get_reference()} design approach that breaks a {PROBLEM.key.get_reference()} into smaller
{SUBPROBLEM.key.get_reference("subproblems")} and solves them using {RECURSION.key.get_reference()}. The top-down
approach typically stores results of subproblems when the problem exhibits 
{OVERLAPPING_SUBPROBLEMS.key.get_reference()}, avoiding redundant work and building solutions 
from those stored results.

---

To compute the 5th term of the {FIBONACCI.key.get_reference()} sequence via {RECURSION.key.get_reference()}, a 
top-down approach expresses "F5" as "F4 + F3", and "F4" as "F3 + F2", each call breaking the 
{PROBLEM.key.get_reference()} into smaller {SUBPROBLEM.key.get_reference("subproblems")}. Because "F3" is needed by 
both "F4" and "F5", its result is stored the first time it is computed and reused the second time, exploiting the 
{OVERLAPPING_SUBPROBLEMS.key.get_reference()}.
"""


TOP_DOWN_APPROACH = _TopDownApproach(
    key=DefinitionKey(
        name="top_down_approach",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["top-down"],
)
