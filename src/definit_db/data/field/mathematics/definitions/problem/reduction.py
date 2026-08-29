from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _Reduction(Definition):
    def _get_content(self) -> str:
        return f"""
Reduction is a process of transforming a 
{PROBLEM.key.get_reference()} into a simpler or smaller instance of the same or a 
{RELATION.key.get_reference("related")} problem, often to make it easier to find a 
{SOLUTION.key.get_reference(phrase="solution")}.

---

In the problem of finding the oldest person among a group of people, 
the reduction is to comparing the ages of two people.
"""


REDUCTION = _Reduction(
    key=DefinitionKey(
        name="reduction",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["problem reduction"],
)
