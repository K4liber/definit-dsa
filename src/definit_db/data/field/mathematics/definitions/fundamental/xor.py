from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.logical_operator import LOGICAL_OPERATOR


class _Xor(Definition):
    def _get_content(self) -> str:
        return f"""
A {LOGICAL_OPERATOR.key.get_reference(phrase="logical operator")} that is true
exactly when one of its inputs is true and the other is false.

Equivalently, for two {BOOLEAN_EXPRESSION.key.get_reference(phrase="boolean expressions")} A and B, A XOR B is true
when A and B have different truth values.

---

Given the {BOOLEAN_EXPRESSION.key.get_reference("boolean expressions")} "the light is on" (true) and "the switch 
is up" (false), XOR combines them as "the light is on XOR the switch is up", which 
evaluates to true because exactly one of the two expressions is true.
"""


XOR = _Xor(
    key=DefinitionKey(
        name="XOR",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["exclusive OR", "exclusive disjunction"],
)
