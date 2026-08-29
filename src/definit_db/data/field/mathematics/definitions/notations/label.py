from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Label(Definition):
    def _get_content(self) -> str:
        return f"""
A label is a name, {NUMBER.key.get_reference(phrase="number")}, or symbol attached to an
{OBJECT.key.get_reference(phrase="object")} to give it meaning or identify it.

---

The {OBJECT.key.get_reference(phrase="object")} "3" can be given the label "x".
Here "x" is a symbol attached to the object so we can refer to it by name instead of by its value.
"""


LABEL = _Label(
    key=DefinitionKey(
        name="label",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["tag"],
)
