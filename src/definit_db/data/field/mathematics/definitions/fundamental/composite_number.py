from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.prime_number import PRIME_NUMBER


class _CompositeNumber(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a positive {INTEGER.key.get_reference("integer")} greater than 1 that is not a
{PRIME_NUMBER.key.get_reference("prime number")} — equivalently, it has at least one positive divisor other than
1 and itself.

---

4, 6, 8, 9, and 10 are composite numbers — for example, 9 = 3 × 3, so 3 is a divisor of 9 other than 1 and 9.

2, 3, 5, and 7 are not composite numbers — they are {PRIME_NUMBER.key.get_reference("prime numbers")}.
1 is not composite either, since it has no positive divisor other than itself.
"""


COMPOSITE_NUMBER = _CompositeNumber(
    key=DefinitionKey(
        name="composite number",
        field=FieldName.MATHEMATICS,
    )
)
