from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Item(Definition):
    def _get_content(self) -> str:
        return f"""
An {self.key.get_reference()} is a single {OBJECT.key.get_reference("object")} considered as an element of a
{SET.key.get_reference("set")}.
"""


ITEM = _Item(
    key=DefinitionKey(
        name="item",
        field=FieldName.MATHEMATICS,
    )
)
