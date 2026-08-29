from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _Transformation(Definition):
    def _get_content(self) -> str:
        return f"""
An {OPERATION.key.get_reference(phrase="operation")} applied to an 
{OBJECT.key.get_reference(phrase="object")} that changes its position, orientation, size, or shape, producing 
a new configuration of the same object.

---

Applying a transformation to the point (2, 3) can move it to the point (7, 3): the point's position changes, 
but it is still a point — the same object in a new configuration.
"""


TRANSFORMATION = _Transformation(
    key=DefinitionKey(
        name="transformation",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["transform"],
)
