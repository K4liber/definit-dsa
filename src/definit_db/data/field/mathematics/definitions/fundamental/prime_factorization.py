from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.prime_number import PRIME_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.product import PRODUCT
from definit_db.data.field.mathematics.definitions.fundamental.reordering import REORDERING


class _PrimeFactorization(Definition):
    def _get_content(self) -> str:
        return f"""
The prime factorization of a positive {INTEGER.key.get_reference("integer")} greater than 1 is a
representation of the number as a {PRODUCT.key.get_reference("product")} of
{PRIME_NUMBER.key.get_reference("prime numbers")}.

Every positive {INTEGER.key.get_reference("integer")} greater than 1 has exactly one such representation,
up to {REORDERING.key.get_reference("reordering")}.

---

12 = 2 × 2 × 3  — the prime factorization of 12 uses the {PRIME_NUMBER.key.get_reference("prime numbers")} 2 and 3.
60 = 2 × 2 × 3 × 5

Both are {PRODUCT.key.get_reference("products")} of {PRIME_NUMBER.key.get_reference("prime numbers")}, and
no other such representation exists (up to reordering).
"""


PRIME_FACTORIZATION = _PrimeFactorization(
    key=DefinitionKey(
        name="prime factorization",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["prime decomposition"],
)
