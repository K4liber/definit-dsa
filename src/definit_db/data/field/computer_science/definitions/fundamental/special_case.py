from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.edge_case import EDGE_CASE
from definit_db.data.field.computer_science.definitions.fundamental.test_case import TEST_CASE
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _SpecialCase(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a particular {TEST_CASE.key.get_reference("test case")} that satisfies additional
{CRITERION.key.get_reference("conditions")}, making it a more specific situation within a broader category.

Special cases may be related to {EDGE_CASE.key.get_reference("edge cases")}, but they are not necessarily 
boundary conditions.
"""


SPECIAL_CASE = _SpecialCase(
    key=DefinitionKey(
        name="special case",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
