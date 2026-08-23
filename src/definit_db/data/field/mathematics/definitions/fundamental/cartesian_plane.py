from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.axis import AXIS
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.plane import PLANE


class _CartesianPlane(Definition):
    def _get_content(self) -> str:
        return f"""
A {PLANE.key.get_reference()} organized by two perpendicular {AXIS.key.get_reference(phrase="axes")} — 
conventionally a horizontal x-axis and a vertical y-axis intersecting at a common origin. Each point in the plane 
is identified by an ordered pair of {NUMBER.key.get_reference(phrase="numbers")} called coordinates, which give 
its signed distance from each axis.

---

In the Cartesian plane, the point (3, 5) is located three units along the x-axis and five units along the y-axis. 
The point (-2, 4) is two units to the left of the y-axis and four units above the x-axis. The two axes partition 
the plane into four regions, one in each combination of positive/negative x and y.
"""


CARTESIAN_PLANE = _CartesianPlane(
    key=DefinitionKey(
        name="Cartesian plane",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("xy-plane", "coordinate plane"),
)
