from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Vector(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is an ordered {SEQUENCE.key.get_reference("sequence")} of
{NUMBER.key.get_reference("numbers")}, often used to represent a point or a direction in space.
"""


VECTOR = _Vector(
    key=DefinitionKey(
        name="vector",
        field=FieldName.MATHEMATICS,
    )
)
