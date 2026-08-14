from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.fundamental.storage import STORAGE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS


class _Key(Definition):
    def _get_content(self) -> str:
        return f"""
A value used to identify, sort, or look up {DATA.key.get_reference(phrase="data")} within a 
{DATA_STRUCTURE.key.get_reference(phrase="data structure")}. A key serves as a distinguishing 
{ITEM.key.get_reference(phrase="item")} that determines 
where data is {STORAGE.key.get_reference(phrase="stored")} or how it is ordered, enabling 
{EFFICIENCY.key.get_reference(phrase="efficient")} search, insertion, and deletion.

---

In a phone book, each person's name acts as a key: the entries are sorted alphabetically by name, so 
looking up "Smith" quickly narrows the search to the relevant section. In a {DATA.key.get_reference(phrase="data")} 
record storing student grades, the student ID number serves as the key that 
{UNIQUENESS.key.get_reference(phrase="uniquely")} identifies each record.
"""


KEY = _Key(
    key=DefinitionKey(
        name="key",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
