from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _Relation(Definition):
    def _get_content(self) -> str:
        return f"""
A relation (also called relationship) describes a connection or association between
{ITEM.key.get_reference(phrase="elements")} of a {COLLECTION.key.get_reference("collection")}.

---

"is less than" is a relation. Applying it to the collection 
(1, 2, 3) it connects 1 to 2, 1 to 3, and 2 to 3.
"""


RELATION = _Relation(
    key=DefinitionKey(
        name="relation",
        field=FieldName.MATHEMATICS,
    )
)
