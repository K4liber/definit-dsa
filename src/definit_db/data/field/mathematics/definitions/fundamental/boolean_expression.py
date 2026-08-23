from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.expression import EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _BooleanExpression(Definition):
    def _get_content(self) -> str:
        return f"""
An {EXPRESSION.key.get_reference()} that evaluates to either true or false.

---

The boolean expression 3 < 5 compares two {NUMBER.key.get_reference(phrase="numbers")} and evaluates to true.
"""


BOOLEAN_EXPRESSION = _BooleanExpression(
    key=DefinitionKey(
        name="boolean expression",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("logical expression",),
)
