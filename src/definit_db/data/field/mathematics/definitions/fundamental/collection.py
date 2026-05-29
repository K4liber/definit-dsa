from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Collection(Definition):
    def _get_content(self) -> str:
        return f"""
A collection is a group of {OBJECT.key.get_reference(phrase="objects")} considered together.
"""


COLLECTION = _Collection(
    key=DefinitionKey(
        name="collection",
        field=FieldName.MATHEMATICS,
    )
)
