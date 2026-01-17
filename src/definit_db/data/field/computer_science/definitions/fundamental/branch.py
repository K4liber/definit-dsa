from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _Branch(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is one possible {PATH.key.get_reference("path")} of execution in a
{PROGRAM.key.get_reference("program")}, typically chosen by a control decision.
"""


BRANCH = _Branch(
    key=DefinitionKey(
        name="branch",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
