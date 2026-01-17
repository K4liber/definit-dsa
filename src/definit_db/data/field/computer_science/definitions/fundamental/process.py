from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.operating_system import OPERATING_SYSTEM
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _Process(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is an instance of a {PROGRAM.key.get_reference(phrase="program")}
that is being executed by the {OPERATING_SYSTEM.key.get_reference(phrase="operating system")}.
"""


PROCESS = _Process(
    key=DefinitionKey(
        name="process",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
