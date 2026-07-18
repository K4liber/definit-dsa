from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _Product(Definition):
    def _get_content(self) -> str:
        return f"""
The result of applying the multiplication
{OPERATION.key.get_reference("operation")} to two or more {NUMBER.key.get_reference("numbers")}.

---

3 × 4 = 12, so 12 is the product of 3 and 4.
2 × 5 × 3 = 30, so 30 is the product of 2, 5, and 3.
"""


PRODUCT = _Product(
    key=DefinitionKey(
        name="product",
        field=FieldName.MATHEMATICS,
    )
)
