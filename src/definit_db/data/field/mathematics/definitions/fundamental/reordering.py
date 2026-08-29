from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Reordering(Definition):
    def _get_content(self) -> str:
        return f"""
A change in the order of {ITEM.key.get_reference(phrase="items")} in a
{SEQUENCE.key.get_reference("sequence")}, without changing which items are present.

---

The {SEQUENCE.key.get_reference("sequence")} [1, 2, 3] can be reordered to [3, 1, 2] or [2, 3, 1].
All three contain the same items — only the arrangement differs.
"""


REORDERING = _Reordering(
    key=DefinitionKey(
        name="reordering",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["permutation", "rearrangement"],
)
