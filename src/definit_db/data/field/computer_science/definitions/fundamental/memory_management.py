from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _MemoryManagement(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the {OPERATION.key.get_reference()} of controlling how a {PROGRAM.key.get_reference()} 
uses {COMPUTER_MEMORY.key.get_reference()}.

It includes when and how {MEMORY_ALLOCATION.key.get_reference("memory is allocated")} and freed, 
and aims to use memory efficiently and safely.
"""


MEMORY_MANAGEMENT = _MemoryManagement(
    key=DefinitionKey(
        name="memory management",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
