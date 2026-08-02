from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.file_storage import FILE_STORAGE


class _Volatile(Definition):
    def _get_content(self) -> str:
        return f"""
A property of {DATA.key.get_reference()} or storage meaning its contents are not
retained when power is removed.

---

An unsaved document open in a text editor is volatile: if the machine
loses power, the edits disappear because they were only held in temporary
storage. Once saved to {FILE_STORAGE.key.get_reference()}, the data
persists and remains available after restart.
"""


VOLATILE = _Volatile(
    key=DefinitionKey(
        name="volatile",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
