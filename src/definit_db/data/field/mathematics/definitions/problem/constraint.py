from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subset_sum import SUBSET_SUM


class _Constraint(Definition):
    def _get_content(self) -> str:
        return f"""
A {CRITERION.key.get_reference("condition")} or restriction that must be satisfied 
by any valid {SOLUTION.key.get_reference()} to a {PROBLEM.key.get_reference()}. Constraints define 
{BOUND.key.get_reference("bounds")} and limitations within which a solution must operate, 
determining which solutions are acceptable and which are not.

---

In the {SUBSET_SUM.key.get_reference()} {PROBLEM.key.get_reference()} with set "{{3, 1, 4, 1, 5}}" and target "9", the 
constraint is that a valid {SOLUTION.key.get_reference()} must sum to exactly "9": the subset "{{3, 1, 5}}" satisfies 
this constraint, while "{{3, 1, 4}}", which sums to "8", does not.
"""


CONSTRAINT = _Constraint(DefinitionKey(name="constraint", field=FieldName.MATHEMATICS))
