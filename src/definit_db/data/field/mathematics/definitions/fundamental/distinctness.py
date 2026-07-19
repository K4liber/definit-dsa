from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS


class _Distinctness(Definition):
    def _get_content(self) -> str:
        return f"""
Distinctness is the property that no two {OBJECT.key.get_reference("objects")} in a given
{COLLECTION.key.get_reference(phrase="collection")} are equal to one another: each object occurs at most once.
Whereas {UNIQUENESS.key.get_reference(phrase="uniqueness")} concerns a single object satisfying a condition,
distinctness is a pairwise relation between the members of a group.

---

In the collection {{"a", "b", "c"}}, all three {ITEM.key.get_reference(phrase="elements")} are distinct: no two
are equal. In the collection {{"a", "a", "b"}}, the two copies of "a" are not distinct from each other, so the
collection does not have distinct elements. The strings "abc" and "ABC" are distinct (they differ), while "abc"
and "abc" are not (they are equal).
"""


DISTINCTNESS = _Distinctness(
    key=DefinitionKey(
        name="distinctness",
        field=FieldName.MATHEMATICS,
    )
)
