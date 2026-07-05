from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _ComputerMemory(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {HARDWARE.key.get_reference()} component that stores {DATA.key.get_reference()} 
for immediate use by a {COMPUTER.key.get_reference()}. It provides storage for 
{INSTRUCTION.key.get_reference("instructions")} and data that are actively being processed or accessed, enabling the 
computer to perform {OPERATION.key.get_reference("operations")} efficiently.

---

When you open a photo, the {INFORMATION.key.get_reference()} describing its pixels is loaded from disk into memory so 
that each edit appears instantly while you work. If power is lost before saving, the in-memory contents disappear —
illustrating that this storage is volatile, unlike the disk it was loaded from.
"""


COMPUTER_MEMORY = _ComputerMemory(DefinitionKey(name="computer memory", field=FieldName.COMPUTER_SCIENCE))
