from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _Product(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is the result of applying the multiplication
{OPERATION.key.get_reference("operation")} to two or more {NUMBER.key.get_reference("numbers")}.
"""


PRODUCT = _Product(
    key=DefinitionKey(
        name="product",
        field=FieldName.MATHEMATICS,
    )
)
