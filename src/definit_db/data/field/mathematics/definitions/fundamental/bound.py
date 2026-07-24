from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.expression import EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Bound(Definition):
    def _get_content(self) -> str:
        return f"""
A limit on the values that a {FUNCTION.key.get_reference()} or {EXPRESSION.key.get_reference()} can take. A bound 
constrains or restricts the range or growth of values, providing a reference point for comparison.

---

The {FUNCTION.key.get_reference()} f(x) = sin(x) only ever produces values between -1 and 1.
The {NUMBER.key.get_reference()} 1 is a bound: no matter which input is chosen, the function never exceeds it.
"""


BOUND = _Bound(
    key=DefinitionKey(
        name="bound",
        field=FieldName.MATHEMATICS,
    )
)
