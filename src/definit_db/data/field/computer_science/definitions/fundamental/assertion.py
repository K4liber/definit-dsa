from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.code import CODE
from definit_db.data.field.computer_science.definitions.fundamental.division_by_zero import DIVISION_BY_ZERO
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.test import TEST
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _Assertion(Definition):
    def _get_content(self) -> str:
        return f"""
A statement in {CODE.key.get_reference()} that checks whether a 
{CRITERION.key.get_reference("condition")} holds.

Assertions are commonly used in {TEST.key.get_reference("tests")} to detect unexpected states.

---

In code that {COMPUTATION.key.get_reference(phrase="computes")} an average, an assertion might state "the count is 
greater than zero" before the division
happens. If the count is in fact zero, the assertion fails immediately and stops the {PROGRAM.key.get_reference()} 
at that line - making the false assumption visible instead of letting a silent 
{DIVISION_BY_ZERO.key.get_reference(phrase="division-by-zero error")} occur later.
"""


ASSERTION = _Assertion(
    key=DefinitionKey(
        name="assert",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
