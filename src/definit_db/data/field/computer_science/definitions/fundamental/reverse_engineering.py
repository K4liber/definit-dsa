from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _ReverseEngineering(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the process of analyzing a {PROGRAM.key.get_reference("program")} or system to 
discover its components, structure, and {OPERATION.key.get_reference("operation")}, often by examining its 
{DATA.key.get_reference("data")} and behavior, without access to its source code. 
Reverse engineering is used to understand how something works.
"""


REVERSE_ENGINEERING = _ReverseEngineering(
    key=DefinitionKey(
        name="reverse engineering",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
