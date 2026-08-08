from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.disk import DISK
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.storage import STORAGE


class _FileStorage(Definition):
    def _get_content(self) -> str:
        return f"""
The persistent retention of {DATA.key.get_reference(phrase="data")} organized as
named files, typically held on a {DISK.key.get_reference(phrase="disk")}. {STORAGE.key.get_reference(phrase="Storing")} 
data as named files lets {PROGRAM.key.get_reference(phrase="programs")} locate, read, and update it by name rather than 
by physical location on the disk.

---

On a laptop, saving a text document places its data into a named file on the disk. Reopening the document later
reads that file back from the disk, and the content survives shutdown because disk storage is persistent.
"""


FILE_STORAGE = _FileStorage(
    key=DefinitionKey(
        name="file storage",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
