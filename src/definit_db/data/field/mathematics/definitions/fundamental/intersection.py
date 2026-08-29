from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Intersection(Definition):
    def _get_content(self) -> str:
        return f"""
The intersection of two {SET.key.get_reference("sets")} A and B is the set of
{ITEM.key.get_reference("elements")} that are in both A and B.

---

A = (1, 2, 3) and B = (2, 3, 4).
The intersection of A and B is the {SET.key.get_reference("set")} (2, 3),
because 2 and 3 are the only {ITEM.key.get_reference("elements")} that appear in both sets.
"""


INTERSECTION = _Intersection(
    key=DefinitionKey(
        name="intersection",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["set intersection"],
)
