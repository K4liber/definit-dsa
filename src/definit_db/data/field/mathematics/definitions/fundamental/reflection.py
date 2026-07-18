from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.transformation import TRANSFORMATION


class _Reflection(Definition):
    def _get_content(self) -> str:
        return f"""
A {TRANSFORMATION.key.get_reference(phrase="transformation")} that produces a 
mirror image of an {OBJECT.key.get_reference(phrase="object")} across a line, point, or plane (the axis of 
reflection), so that each point and its image are the same distance from the axis but on opposite sides.

---

Reflecting the point (2, 3) across the y-axis produces the point (-2, 3): the x-coordinate is negated while 
the y-coordinate stays the same, placing the image the same distance from the axis but on the opposite side.
"""


REFLECTION = _Reflection(
    key=DefinitionKey(
        name="reflection",
        field=FieldName.MATHEMATICS,
    )
)
