from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.file_storage import FILE_STORAGE
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.pixel import PIXEL
from definit_db.data.field.computer_science.definitions.fundamental.volatile import VOLATILE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _ComputerMemory(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {HARDWARE.key.get_reference()} component that stores {DATA.key.get_reference()} 
for immediate use by a {COMPUTER.key.get_reference()}. It provides temporary
{FILE_STORAGE.key.get_reference("storage")} for {INSTRUCTION.key.get_reference("instructions")} and
data that are actively being {COMPUTATION.key.get_reference("processed")} or accessed,
enabling the {COMPUTER.key.get_reference("computer")} to perform
{OPERATION.key.get_reference("operations")} {EFFICIENCY.key.get_reference("efficiently")}.

---

When you open a photo, the {INFORMATION.key.get_reference()} describing its
{PIXEL.key.get_reference("pixels")} is loaded from
{FILE_STORAGE.key.get_reference()} into memory so
that each edit appears instantly while you work. If power is lost before saving, the in-memory contents disappear —
illustrating that this storage is {VOLATILE.key.get_reference()}, unlike the
{FILE_STORAGE.key.get_reference()} it was loaded from.
"""


COMPUTER_MEMORY = _ComputerMemory(DefinitionKey(name="computer memory", field=FieldName.COMPUTER_SCIENCE))
