from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.disk import DISK
from definit_db.data.field.computer_science.definitions.fundamental.file_storage import FILE_STORAGE
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.fundamental.input_output import INPUT_OUTPUT
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _OperatingSystem(Definition):
    def _get_content(self) -> str:
        return f"""
An operating system is system software that manages a {COMPUTER.key.get_reference(phrase="computer")}'s
{HARDWARE.key.get_reference(phrase="hardware")} and {PROGRAM.key.get_reference(phrase="software")} resources. It
allocates {COMPUTER_MEMORY.key.get_reference(phrase="memory")} to running programs, schedules their use of the
hardware, and provides services they rely on, such as {FILE_STORAGE.key.get_reference(phrase="file storage")}
and {INPUT_OUTPUT.key.get_reference(phrase="input/output")}.

---

When several programs run at once on a laptop, the operating system decides which one may use the processor next,
how much memory each receives, and how they take turns reading from the {DISK.key.get_reference(phrase="disk")}. A program never touches the hardware
directly; instead it asks the operating system, which mediates access so the programs do not interfere with each
other.
"""


OPERATING_SYSTEM = _OperatingSystem(
    key=DefinitionKey(
        name="operating system",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
