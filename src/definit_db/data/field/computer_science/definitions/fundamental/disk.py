from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.volatile import VOLATILE


class _Disk(Definition):
    def _get_content(self) -> str:
        return f"""
A {HARDWARE.key.get_reference(phrase="hardware")} component that stores
{DATA.key.get_reference(phrase="data")} persistently, retaining it even when power is turned off 
(non-{VOLATILE.key.get_reference(phrase="volatile")}
storage). A disk provides long-term retention of large amounts of data that 
{PROGRAM.key.get_reference("programs")} can read or write.

---

A disk in a {COMPUTER.key.get_reference()} retains documents and photos even after the 
{COMPUTER.key.get_reference(phrase="machine")} is shut down: they remain stored on it
and are available again when it next starts.
"""


DISK = _Disk(
    key=DefinitionKey(
        name="disk",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
