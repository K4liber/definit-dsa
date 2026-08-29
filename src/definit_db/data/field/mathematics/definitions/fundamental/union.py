from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Union(Definition):
    def _get_content(self) -> str:
        return f"""
The union of two {SET.key.get_reference("sets")} A and B is the set of
{ITEM.key.get_reference("elements")} that are in A or in B (or in both).

---

A = (1, 2, 3) and B = (2, 3, 4).
The union of A and B is the {SET.key.get_reference("set")} (1, 2, 3, 4),
because it gathers every {ITEM.key.get_reference("element")} that appears in either set, without repetition.
"""


UNION = _Union(
    key=DefinitionKey(
        name="union",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["set union"],
)
