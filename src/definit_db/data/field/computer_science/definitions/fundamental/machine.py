from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _Machine(Definition):
    def _get_content(self) -> str:
        return f"""
In computing, a {self.key.get_reference()} is a physical or virtual {COMPUTER.key.get_reference(phrase="computer")}
that can run {PROGRAM.key.get_reference(phrase="programs")} and perform computation.
"""


MACHINE = _Machine(
    key=DefinitionKey(
        name="machine",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
