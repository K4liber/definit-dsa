from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.transformation import TRANSFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.vector import VECTOR


class _Translation(Definition):
    def _get_content(self) -> str:
        return f"""
A {TRANSFORMATION.key.get_reference(phrase="transformation")} that moves every 
point of an {OBJECT.key.get_reference(phrase="object")} by the same {VECTOR.key.get_reference(phrase="vector")}, 
without changing its orientation, size, or shape.

---

Translating the point (2, 3) by the vector (5, 0) produces the point (7, 3): every point shifts the same 
amount in the same direction, so the object keeps its shape and orientation.
"""


TRANSLATION = _Translation(
    key=DefinitionKey(
        name="translation",
        field=FieldName.MATHEMATICS,
    )
)
