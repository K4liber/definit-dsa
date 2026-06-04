from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Function(Definition):
    def _get_content(self) -> str:
        return f"""
A function is a kind of {RELATION.key.get_reference(phrase="relation")} from a
{SET.key.get_reference(phrase="set")} X to a {SET.key.get_reference(phrase="set")} Y that assigns to each
{ITEM.key.get_reference(phrase="element")} (or {OBJECT.key.get_reference(phrase="object")}) of X exactly one
{ITEM.key.get_reference(phrase="element")} of Y.

---

Take X = (1, 2, 3), Y = (2, 3, 4) and the rule f(x) = x + 1.
This is a function because each {ITEM.key.get_reference(phrase="element")} of X is assigned exactly one
{ITEM.key.get_reference(phrase="element")} of Y: 1 maps to 2, 2 maps to 3, and 3 maps to 4.
"""


FUNCTION = _Function(
    key=DefinitionKey(
        name="function",
        field=FieldName.MATHEMATICS,
    )
)
