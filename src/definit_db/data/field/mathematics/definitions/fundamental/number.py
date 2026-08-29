from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Number(Definition):
    def _get_content(self) -> str:
        return f"""
A number is a mathematical {OBJECT.key.get_reference()} used to count or measure.

---

The {OBJECT.key.get_reference()} "3" is a number: it can, for example, count three apples.
"""


NUMBER = _Number(
    key=DefinitionKey(
        name="number",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["numeric value"],
)
