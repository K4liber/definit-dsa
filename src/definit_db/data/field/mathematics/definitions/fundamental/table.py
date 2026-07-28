from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.square_root import SQUARE_ROOT


class _Table(Definition):
    def _get_content(self) -> str:
        return f"""
A table is a structured {COLLECTION.key.get_reference(phrase="collection")} of {ITEM.key.get_reference(phrase="items")}
arranged so that each entry can be looked up by its position or by an associated 
{INDEX.key.get_reference(phrase="index")}. A one-dimensional table stores entries in a single row or column, 
while a two-dimensional table arranges them into rows and columns. 
Tables are used to organize values for quick reference.

---

A multiplication table arranges products into rows and columns: the entry at row 3, column 4 holds the value 12,
so one can look up 3 × 4 by finding that position instead of {COMPUTATION.key.get_reference("recomputing")} it. 
A one-dimensional table of {SQUARE_ROOT.key.get_reference("square roots")} might store 
(√1, √2, √3, √4) = (1, 1.41, 1.73, 2), letting each value be retrieved by its {INDEX.key.get_reference(phrase="index")} 
without recalculating it.
"""


TABLE = _Table(
    key=DefinitionKey(
        name="table",
        field=FieldName.MATHEMATICS,
    )
)
