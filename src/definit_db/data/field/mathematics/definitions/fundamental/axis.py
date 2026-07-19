from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.transformation import TRANSFORMATION


class _Axis(Definition):
    def _get_content(self) -> str:
        return f"""
An axis is a reference line about which a geometric or coordinate space is organized. Positions may be measured
along an axis (as coordinates are along the x-axis and y-axis of a plane), and
{TRANSFORMATION.key.get_reference(phrase="transformations")} may be defined with respect to an axis (as a
reflection mirrors points across it). An axis is itself an
{OBJECT.key.get_reference(phrase="object")} of the space.

---

In the two-dimensional plane, the x-axis and y-axis are two perpendicular reference lines. The point (3, 5) is
located three units along the x-axis and five units along the y-axis. Reflecting that point across the x-axis
gives (3, -5): the axis serves both as a basis for measuring position and as the line of reflection.
"""


AXIS = _Axis(
    key=DefinitionKey(
        name="axis",
        field=FieldName.MATHEMATICS,
    )
)
