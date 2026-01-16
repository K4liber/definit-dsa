from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.test import TEST
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _Assertion(Definition):
    def _get_content(self) -> str:
        return f"""
An {self.key.get_reference()} is a statement in code that checks whether a 
{CRITERION.key.get_reference("condition")} holds.

Assertions are commonly used in {TEST.key.get_reference("tests")} to detect unexpected states.
"""


ASSERTION = _Assertion(
    key=DefinitionKey(
        name="assert",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
