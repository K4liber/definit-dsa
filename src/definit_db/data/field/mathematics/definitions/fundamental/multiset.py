from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.distinctness import DISTINCTNESS
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Multiset(Definition):
    def _get_content(self) -> str:
        return f"""
A multiset is a {COLLECTION.key.get_reference(phrase="collection")}, similar to a
{SET.key.get_reference(phrase="set")}, that allows the same {ITEM.key.get_reference(phrase="element")} to occur
more than once. Unlike a set, which only contains {DISTINCTNESS.key.get_reference(phrase="distinct")} elements,
a multiset also records how many times each
{ITEM.key.get_reference(phrase="element")} appears.

---

The multiset (1, 1, 2, 3, 3, 3) contains 1 twice, 2 once, and 3 three times.
As a {SET.key.get_reference(phrase="set")} it would collapse to (1, 2, 3), but as a multiset the repeated
{ITEM.key.get_reference(phrase="elements")} are kept.
"""


MULTISET = _Multiset(
    key=DefinitionKey(
        name="multiset",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["bag"],
)
