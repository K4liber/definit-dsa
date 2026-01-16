from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.vector import VECTOR


class _Matrix(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a rectangular arrangement of {NUMBER.key.get_reference("numbers")} 
in rows and columns.

A matrix can be viewed as a collection of {VECTOR.key.get_reference("vectors")} (rows or columns).
"""


MATRIX = _Matrix(
    key=DefinitionKey(
        name="matrix",
        field=FieldName.MATHEMATICS,
    )
)
