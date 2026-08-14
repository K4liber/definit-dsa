from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _Table(Definition):
    def _get_content(self) -> str:
        return f"""
A table is a structured {COLLECTION.key.get_reference(phrase="collection")} of {ITEM.key.get_reference(phrase="items")}
arranged so that each entry can be looked up by its position or by an associated 
{INDEX.key.get_reference(phrase="index")}. A one-dimensional table stores entries in a single row or column, 
while a two-dimensional table arranges them into rows and columns. 
Tables are used to organize values for quick reference.

---

A one-dimensional table of city populations might store
(3, 1, 8) for cities A, B, and C, letting each value be retrieved by its {INDEX.key.get_reference(phrase="index")}.
"""


TABLE = _Table(
    key=DefinitionKey(
        name="table",
        field=FieldName.MATHEMATICS,
    )
)
