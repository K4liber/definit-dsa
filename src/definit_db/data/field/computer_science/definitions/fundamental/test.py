from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _Test(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a procedure or experiment used to evaluate whether a system or component
behaves as expected under specified {CRITERION.key.get_reference("conditions")}.

A test typically takes some {DATA.key.get_reference("data")} (inputs) and produces observations (outputs)
that can be compared to expected results.
"""


TEST = _Test(
    key=DefinitionKey(
        name="test",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
