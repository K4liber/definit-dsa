from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.axis import AXIS
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Vector(Definition):
    def _get_content(self) -> str:
        return f"""
An ordered {SEQUENCE.key.get_reference("sequence")} of
{NUMBER.key.get_reference("numbers")}, often used to represent a point or a direction in space.

---

The {SEQUENCE.key.get_reference("sequence")} ("2", "3") is a vector of two {NUMBER.key.get_reference("numbers")}: 
it can represent the point two units along one {AXIS.key.get_reference(phrase="axis")} and three units along
another, or the direction pointing that way from the origin. 
way from the origin.
"""


VECTOR = _Vector(
    key=DefinitionKey(
        name="vector",
        field=FieldName.MATHEMATICS,
    )
)
