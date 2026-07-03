from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _FeasibleSolution(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {SOLUTION.key.get_reference()} to a {PROBLEM.key.get_reference()} 
that satisfies all the {CONSTRAINT.key.get_reference("constraints")}. A feasible solution may not be optimal, 
but it meets all the requirements and restrictions of the problem.

---

For a packing {PROBLEM.key.get_reference()} limited to a weight {CONSTRAINT.key.get_reference()} of "10kg", any 
selection of items whose combined weight does not exceed "10kg" is a {self.key.get_reference("feasible solution")}, 
even if a different selection would pack more value into the same limit.
"""


FEASIBLE_SOLUTION = _FeasibleSolution(DefinitionKey(name="feasible solution", field=FieldName.MATHEMATICS))
