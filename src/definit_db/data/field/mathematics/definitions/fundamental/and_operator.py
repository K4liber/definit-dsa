from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.logical_operator import LOGICAL_OPERATOR


class _AndOperator(Definition):
    def _get_content(self) -> str:
        return f"""
A {LOGICAL_OPERATOR.key.get_reference(phrase="logical operator")} that is true
only when all of its inputs are true.

For two {BOOLEAN_EXPRESSION.key.get_reference(phrase="boolean expressions")} A and B, A AND B is true exactly when
both A and B are true.

---

Given the {BOOLEAN_EXPRESSION.key.get_reference("boolean expressions")} "it is raining" (true) and "it is windy" 
(true), AND combines them as "it is raining AND it is windy", which evaluates to true 
because both expressions are true.
"""


AND_OPERATOR = _AndOperator(
    key=DefinitionKey(
        name="AND",
        field=FieldName.MATHEMATICS,
    )
)
