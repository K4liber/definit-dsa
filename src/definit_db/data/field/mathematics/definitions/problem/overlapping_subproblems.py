from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _OverlappingSubProblems(Definition):
    def _get_content(self) -> str:
        return f"""
A {PROBLEM.key.get_reference()} is said to have overlapping 
{SUBPROBLEM.key.get_reference(phrase="subproblems")} if the problem can be broken down into smaller, 
simpler subproblems that are reused several times.

---

In a sequence of {NUMBER.key.get_reference(phrase="numbers")} where each equals the sum of the previous two — 
"1", "1", "2", "3", "5" — finding the value at position "5" by naive {RECURSION.key.get_reference(phrase="recursion")} 
expands as:

F(5) = F(4) + F(3)

a) solving F(4):

F(4) = F(3) + F(2) → F(3) and F(2) solved here

F(3) = F(2) + F(1) → F(2) and F(1) solved here

b) and on the other branch of F(5), solving F(3):

F(3) = F(2) + F(1) → F(3), F(2), and F(1) solved AGAIN

So the {SUBPROBLEM.key.get_reference(phrase="subproblems")} "find F(3)", "find F(2)", and "find F(1)" are each 
solved more than once — they overlap across separate branches of the recursion.
"""


OVERLAPPING_SUBPROBLEMS = _OverlappingSubProblems(
    key=DefinitionKey(
        name="overlapping_subproblems",
        field=FieldName.MATHEMATICS,
    )
)
