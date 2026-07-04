from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.transformation import TRANSFORMATION


class _Rotation(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {TRANSFORMATION.key.get_reference(phrase="transformation")} that turns an 
{OBJECT.key.get_reference(phrase="object")} around a fixed point (the center of rotation) by a given angle, 
keeping the distance from each point to the center unchanged.

---

Rotating the point (1, 0) by 90 degrees counterclockwise around the origin produces the point (0, 1): the 
point's distance from the origin (1) stays the same, but its position turns around the center by the given 
angle.
"""


ROTATION = _Rotation(
    key=DefinitionKey(
        name="rotation",
        field=FieldName.MATHEMATICS,
    )
)
