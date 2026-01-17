from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER


class _OperatingSystem(Definition):
    def _get_content(self) -> str:
        return f"""
An {self.key.get_reference()} is system software that manages a {COMPUTER.key.get_reference(phrase="computer")}'s 
hardware and software resources.
"""


OPERATING_SYSTEM = _OperatingSystem(
    key=DefinitionKey(
        name="operating system",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
