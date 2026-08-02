from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA


class _Volatile(Definition):
    def _get_content(self) -> str:
        return f"""
A property of {DATA.key.get_reference()} meaning its contents are not retained when power is removed.

---

Unsaved changes in a document editor are volatile: if the machine loses power before you save,
the edits disappear. Once saved, the data persists.
"""


VOLATILE = _Volatile(
    key=DefinitionKey(
        name="volatile",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
