from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.distinctness import DISTINCTNESS
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Set(Definition):
    def _get_content(self) -> str:
        return f"""
A set is an unordered {COLLECTION.key.get_reference(phrase="collection")} of
{DISTINCTNESS.key.get_reference(phrase="distinct")} things. These things are called elements or members of the
set and are typically mathematical {OBJECT.key.get_reference(phrase="objects")} of any kind.

---

(1, 2, 3) is a set containing three {OBJECT.key.get_reference(phrase="objects")}.
The order does not matter — (3, 1, 2) is the same set.
However, (1, 1, 2, 3) is not valid because "1" appears twice; sets only contain different things.
"""


SET = _Set(
    key=DefinitionKey(
        name="set",
        field=FieldName.MATHEMATICS,
    )
)
