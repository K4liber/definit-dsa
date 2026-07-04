from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _Transformation(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is an {OPERATION.key.get_reference(phrase="operation")} applied to an 
{OBJECT.key.get_reference(phrase="object")} that changes its position, orientation, size, or shape, producing 
a new configuration of the same object.

---

Translating the point (2, 3) by (5, 0) produces the point (7, 3): the transformation changes the point's 
position while leaving its nature as a point unchanged.
"""


TRANSFORMATION = _Transformation(
    key=DefinitionKey(
        name="transformation",
        field=FieldName.MATHEMATICS,
    )
)
