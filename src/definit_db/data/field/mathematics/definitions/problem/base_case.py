from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.reduction import REDUCTION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _BaseCase(Definition):
    def _get_content(self) -> str:
        return f"""
The simplest instance of the {PROBLEM.key.get_reference()}, which can be 
{SOLUTION.key.get_reference("solved")} directly without further {REDUCTION.key.get_reference()}.

---

In the {PROBLEM.key.get_reference()} of finding the oldest person among a group of people, the base case is
a reduction to comparing the ages of two people.
"""


BASE_CASE = _BaseCase(
    key=DefinitionKey(
        name="base_case",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("base condition", "base step"),
)
