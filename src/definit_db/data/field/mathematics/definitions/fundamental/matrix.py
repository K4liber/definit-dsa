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

---

The arrangement with first row ("1", "2") and second row ("3", "4") is a matrix of four 
{NUMBER.key.get_reference("numbers")} laid out in two rows and two columns. Its rows can be read as the 
{VECTOR.key.get_reference("vectors")} ("1", "2") and ("3", "4").
"""


MATRIX = _Matrix(
    key=DefinitionKey(
        name="matrix",
        field=FieldName.MATHEMATICS,
    )
)
