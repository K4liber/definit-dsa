from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION


class _LogicalOperator(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Logical operator")} is an operator that takes one or more
{BOOLEAN_EXPRESSION.key.get_reference(phrase="boolean expressions")} as input and produces a boolean output.
"""


LOGICAL_OPERATOR = _LogicalOperator(
    key=DefinitionKey(
        name="Logical operator",
        field=FieldName.MATHEMATICS,
    )
)
