from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _Constraint(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {CRITERION.key.get_reference("condition")} or restriction that must be satisfied 
by any valid {SOLUTION.key.get_reference()} to a {PROBLEM.key.get_reference()}. Constraints define {BOUND.key.get_reference("bounds")} 
and limitations within which a solution must operate, determining which solutions are acceptable and which are not.
"""


CONSTRAINT = _Constraint(DefinitionKey(name="constraint", field=FieldName.MATHEMATICS))
