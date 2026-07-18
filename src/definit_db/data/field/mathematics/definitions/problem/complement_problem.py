from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _ComplementProblem(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The complement problem of a decision {PROBLEM.key.get_reference()} is obtained by swapping its "yes" and 
"no" answers: for any given {INPUT_DATA.key.get_reference("input")}, the complement answers "no" exactly when the 
original answers "yes", and "yes" exactly when the original answers "no". It inverts the acceptance 
{CRITERION.key.get_reference("criteria")} while keeping the same input structure.

---

The decision {PROBLEM.key.get_reference()} "Is this {NUMBER.key.get_reference("number")} even?" has the complement 
problem "Is this number odd?". For the {INPUT_DATA.key.get_reference("input")} "4" the original answers "yes" while 
the complement answers "no"; for the input "3" the two answers are reversed.
"""


COMPLEMENT_PROBLEM = _ComplementProblem(DefinitionKey(name="complement problem", field=FieldName.MATHEMATICS))
