from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.table import TABLE


class _Storage(Definition):
    def _get_content(self) -> str:
        return f"""
The process of keeping {DATA.key.get_reference(phrase="data")} or {INFORMATION.key.get_reference(phrase="information")} 
in a medium so that it can be accessed, retrieved, or modified later.

---

Writing the {NUMBER.key.get_reference(phrase="numbers")} 72, 85, and 90 into a 
{TABLE.key.get_reference(phrase="table")} so they can be read back later 
is an act of storage: the values persist in the table until they are deliberately changed or removed.
"""


STORAGE = _Storage(
    key=DefinitionKey(
        name="storage",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
