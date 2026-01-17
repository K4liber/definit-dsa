from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName


class _BooleanExpression(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference(phrase="boolean expression")} is an expression that evaluates to either true or false.
"""


BOOLEAN_EXPRESSION = _BooleanExpression(
    key=DefinitionKey(
        name="boolean expression",
        field=FieldName.MATHEMATICS,
    )
)
