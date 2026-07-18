from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER


class _PrimeNumber(Definition):
    def _get_content(self) -> str:
        return f"""
A positive {INTEGER.key.get_reference("integer")} greater than 1 that has
exactly two positive divisors: 1 and itself.

---

2, 3, 5, 7, and 11 are prime numbers — each is only divisible by 1 and itself.

4 is not a prime number because it has three divisors: 1, 2, and 4.
1 is not a prime number because it has only one divisor, not two.
"""


PRIME_NUMBER = _PrimeNumber(
    key=DefinitionKey(
        name="prime number",
        field=FieldName.MATHEMATICS,
    )
)
