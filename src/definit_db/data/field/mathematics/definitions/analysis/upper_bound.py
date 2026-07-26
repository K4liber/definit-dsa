from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.expression import EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _UpperBound(Definition):
    def _get_content(self) -> str:
        return f"""
A {BOUND.key.get_reference()} that establishes the maximum value or growth rate that a
{FUNCTION.key.get_reference()} or {EXPRESSION.key.get_reference()} can achieve. An upper bound provides a ceiling on
values: they may approach this ceiling but cannot exceed it.

---

For the {FUNCTION.key.get_reference()} f(x) = sin(x), the {NUMBER.key.get_reference()} 1 is an upper bound:
the function's values never rise above it. Any larger value, such as 2, is also an upper bound, but 1 is the
smallest (tightest) one.
"""


UPPER_BOUND = _UpperBound(
    key=DefinitionKey(
        name="upper_bound",
        field=FieldName.MATHEMATICS,
    )
)
