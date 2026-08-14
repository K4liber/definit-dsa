from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER


class _Divisor(Definition):
    def _get_content(self) -> str:
        return f"""
A divisor of a non-zero {INTEGER.key.get_reference(phrase="integer")} n is an integer d such that n = d × k for
some integer k. Equivalently, d divides n (written d | n), or n is divisible by d: dividing n by d leaves no
remainder.

Common equivalent wordings: "d is a divisor of n", "d divides n", "n is divisible by d", and "d is a factor of n".

---

The divisors of 12 are 1, 2, 3, 4, 6, and 12, since 12 = 1×12 = 2×6 = 3×4. Each divides 12 with no remainder.
By contrast, 5 is not a divisor of 12: 12 ÷ 5 leaves remainder 2, so 5 does not divide 12.

A divisor of 7 is 1 (since 7 = 1 × 7), and 7 itself is also a divisor (since 7 = 7 × 1).
"""


DIVISOR = _Divisor(
    key=DefinitionKey(
        name="divisor",
        field=FieldName.MATHEMATICS,
    )
)
