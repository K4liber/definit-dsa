from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.logical_operator import LOGICAL_OPERATOR


class _OrOperator(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="OR")} is a {LOGICAL_OPERATOR.key.get_reference(phrase="logical operator")} that is true
if at least one of its inputs is true.

Equivalently, for two {BOOLEAN_EXPRESSION.key.get_reference(phrase="boolean expressions")} A and B, A OR B is false
only when both A and B are false.

---

Given the {BOOLEAN_EXPRESSION.key.get_reference("boolean expressions")} "it is raining" (true) and "it is windy" 
(false), {self.key.get_reference("OR")} combines them as "it is raining OR it is windy", which evaluates to true 
because at least one of the two expressions is true.
"""


OR_OPERATOR = _OrOperator(
    key=DefinitionKey(
        name="OR",
        field=FieldName.MATHEMATICS,
    )
)
