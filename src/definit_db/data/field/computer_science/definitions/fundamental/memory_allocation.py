from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.variable import VARIABLE
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _MemoryAllocation(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The {OPERATION.key.get_reference()} of assigning a block of 
{COMPUTER_MEMORY.key.get_reference()} to store {DATA.key.get_reference()} for use by a {PROGRAM.key.get_reference()}. 
It determines where and how much memory is reserved for storing {INFORMATION.key.get_reference()} during program 
execution.

---

For example, when a {PROGRAM.key.get_reference("program")} needs to store a {NUMBER.key.get_reference()} for later 
use, a region of {COMPUTER_MEMORY.key.get_reference("memory")} is reserved, sized to hold that value, and associated 
with a {VARIABLE.key.get_reference()}. Once the stored data is no longer needed, the reserved region can be released so 
the memory is available for later use.
"""


MEMORY_ALLOCATION = _MemoryAllocation(DefinitionKey(name="memory allocation", field=FieldName.COMPUTER_SCIENCE))
