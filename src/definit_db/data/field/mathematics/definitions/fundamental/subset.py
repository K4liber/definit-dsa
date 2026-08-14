from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Subset(Definition):
    def _get_content(self) -> str:
        return f"""
A {SET.key.get_reference(phrase="set")} all of whose {ITEM.key.get_reference(phrase="elements")} are contained in
another set. If every element of set A is also an element of set B, then A is a subset of B.

---

The {SET.key.get_reference(phrase="set")} (1, 3) is a subset of (1, 2, 3, 4), since every 
{ITEM.key.get_reference(phrase="element")} of (1, 3) also belongs to (1, 2, 3, 4). The set (1, 5) is not a subset of 
(1, 2, 3, 4), since 5 is not contained in it.
"""


SUBSET = _Subset(
    key=DefinitionKey(
        name="subset",
        field=FieldName.MATHEMATICS,
    )
)
