from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.product import PRODUCT


class _Factorial(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} of a non-negative {INTEGER.key.get_reference("integer")} n, written n!, is the
{PRODUCT.key.get_reference("product")} of all positive integers up to n.

By convention, 0! = 1.
"""


FACTORIAL = _Factorial(
    key=DefinitionKey(
        name="factorial",
        field=FieldName.MATHEMATICS,
    )
)
