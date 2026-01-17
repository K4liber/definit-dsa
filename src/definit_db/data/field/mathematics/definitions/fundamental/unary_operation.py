from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _UnaryOperation(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Unary operation")} is an {OPERATION.key.get_reference(phrase="operation")} that takes
exactly one input (one operand).
"""


UNARY_OPERATION = _UnaryOperation(
    key=DefinitionKey(
        name="Unary operation",
        field=FieldName.MATHEMATICS,
    )
)
