from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.logical_operator import LOGICAL_OPERATOR
from definit_db.data.field.mathematics.definitions.fundamental.unary_operation import UNARY_OPERATION


class _NotOperator(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="NOT")} is a {UNARY_OPERATION.key.get_reference(phrase="unary operation")} and
{LOGICAL_OPERATOR.key.get_reference(phrase="logical operator")} that inverts the truth value of its input.

For a {BOOLEAN_EXPRESSION.key.get_reference(phrase="boolean expression")} A:
- NOT A is true when A is false.
- NOT A is false when A is true.
"""


NOT_OPERATOR = _NotOperator(
    key=DefinitionKey(
        name="NOT",
        field=FieldName.MATHEMATICS,
    )
)
