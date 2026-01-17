from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.test import TEST
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _TestCase(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a single instance of a {TEST.key.get_reference("test")}, defined by a specific
set of {INPUT_DATA.key.get_reference("inputs")}, evaluation {CRITERION.key.get_reference("criteria")}, 
and expected results.
"""


TEST_CASE = _TestCase(
    key=DefinitionKey(
        name="test case",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
