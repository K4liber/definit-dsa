from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION


class _LogicalOperator(Definition):
    def _get_content(self) -> str:
        return f"""
An operator that takes one or more
{BOOLEAN_EXPRESSION.key.get_reference(phrase="boolean expressions")} as input and produces a boolean output.

---

Combining the {BOOLEAN_EXPRESSION.key.get_reference("boolean expressions")} "true" and "false" with the word 
"and" produces the single boolean output "false". The word "and" here acts as a 
logical operator, taking two boolean inputs and producing one boolean result.
"""


LOGICAL_OPERATOR = _LogicalOperator(
    key=DefinitionKey(
        name="Logical operator",
        field=FieldName.MATHEMATICS,
    )
)
