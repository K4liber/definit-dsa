from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Uniqueness(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference("Uniqueness")} means that there is exactly one
{OBJECT.key.get_reference("object")} satisfying a given description, within the intended context.
"""


UNIQUENESS = _Uniqueness(
    key=DefinitionKey(
        name="uniqueness",
        field=FieldName.MATHEMATICS,
    )
)
