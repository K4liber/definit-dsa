from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _Subproblem(Definition):
    def _get_content(self) -> str:
        return f"""
A smaller, more manageable {PROBLEM.key.get_reference(phrase="problem")} derived from a larger problem, often 
used in the context of problem-solving and algorithm design.

---

The {PROBLEM.key.get_reference(phrase="problem")} "add the {NUMBER.key.get_reference(phrase="numbers")} "2", "3", 
and "4"" can be broken into the subproblem "add "2" and "3"", whose result "5" is then combined with "4" to solve 
the original problem.
"""


SUBPROBLEM = _Subproblem(
    key=DefinitionKey(
        name="subproblem",
        field=FieldName.MATHEMATICS,
    )
)
