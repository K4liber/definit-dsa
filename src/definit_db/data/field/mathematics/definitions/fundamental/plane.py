from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Plane(Definition):
    def _get_content(self) -> str:
        return f"""
A plane is a flat, two-dimensional surface that extends indefinitely. It is the geometric {OBJECT.key.get_reference()} 
on which points, lines, and figures are studied: any two distinct points in a plane determine a straight line 
that lies entirely within it.

---

A sheet of paper is a finite region of a plane; idealized, the plane extends without end in every direction. 
A straight line drawn between any two points on the sheet stays on the same flat surface, illustrating that the 
line lies within the plane.
"""


PLANE = _Plane(
    key=DefinitionKey(
        name="plane",
        field=FieldName.MATHEMATICS,
    )
)
