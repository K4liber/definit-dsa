from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.prime_number import PRIME_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.product import PRODUCT
from definit_db.data.field.mathematics.definitions.fundamental.reordering import REORDERING
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS


class _PrimeFactorization(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} of a positive {INTEGER.key.get_reference("integer")} greater than 1 is a
representation of the number as a {PRODUCT.key.get_reference("product")} of
{PRIME_NUMBER.key.get_reference("prime numbers")}.

Up to {REORDERING.key.get_reference("reordering")}, this factorization is
{UNIQUENESS.key.get_reference("unique")}.
"""


PRIME_FACTORIZATION = _PrimeFactorization(
    key=DefinitionKey(
        name="prime factorization",
        field=FieldName.MATHEMATICS,
    )
)
