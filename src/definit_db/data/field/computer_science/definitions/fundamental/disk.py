from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE


class _Disk(Definition):
    def _get_content(self) -> str:
        return f"""
A {HARDWARE.key.get_reference(phrase="hardware")} component that stores
{DATA.key.get_reference(phrase="data")} persistently, retaining it even when power is turned off (non-volatile
storage). A disk provides long-term retention of large amounts of data that programs can read or write.

---

A hard disk drive (HDD) or solid-state drive (SSD) in a laptop is a disk: documents, photos, and installed
programs remain stored on it after the computer is shut down and are available again when it next starts.
"""


DISK = _Disk(
    key=DefinitionKey(
        name="disk",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
