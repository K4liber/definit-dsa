from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _UnaryOperation(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Unary operation")} is an {OPERATION.key.get_reference(phrase="operation")} that takes
exactly one input (one operand).

---

Negating the {NUMBER.key.get_reference("number")} "7" to get "-7" is a {self.key.get_reference("unary operation")}: 
it takes exactly one input, "7", and produces one output, "-7".
"""


UNARY_OPERATION = _UnaryOperation(
    key=DefinitionKey(
        name="Unary operation",
        field=FieldName.MATHEMATICS,
    )
)
