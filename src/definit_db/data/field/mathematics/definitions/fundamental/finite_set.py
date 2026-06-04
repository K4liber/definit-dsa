from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _FiniteSet(Definition):
    def _get_content(self) -> str:
        return f"""
Finite set is a {SET.key.get_reference(phrase="set")} that has a finite number of
{ITEM.key.get_reference("elements")}.
Informally, a finite set is a set which one could in principle count and finish counting.

---

(2, 4, 6, 8, 10) is a finite set with five {ITEM.key.get_reference("elements")}.
Counting them ends after the last {ITEM.key.get_reference("element")}, so the set is finite.
"""


FINITE_SET = _FiniteSet(
    key=DefinitionKey(
        name="finite_set",
        field=FieldName.MATHEMATICS,
    )
)
