from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Item(Definition):
    def _get_content(self) -> str:
        return f"""
A single {OBJECT.key.get_reference("object")} considered as one of the members of a
{COLLECTION.key.get_reference("collection")}.

---

In the collection (1, 2, 3), the number "2" is an item:
it is a single {OBJECT.key.get_reference("object")} that belongs to the
{COLLECTION.key.get_reference("collection")}.
"""


ITEM = _Item(
    key=DefinitionKey(
        name="item",
        field=FieldName.MATHEMATICS,
    )
)
