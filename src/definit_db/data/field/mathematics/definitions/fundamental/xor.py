from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.logical_operator import LOGICAL_OPERATOR


class _Xor(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="XOR")} is a {LOGICAL_OPERATOR.key.get_reference(phrase="logical operator")} that is true
exactly when one of its inputs is true and the other is false.

Equivalently, for two {BOOLEAN_EXPRESSION.key.get_reference(phrase="boolean expressions")} A and B, A XOR B is true
when A and B have different truth values.
"""


XOR = _Xor(
    key=DefinitionKey(
        name="XOR",
        field=FieldName.MATHEMATICS,
    )
)
