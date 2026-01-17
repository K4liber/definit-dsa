from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.natural_number import NATURAL_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.prime_number import PRIME_NUMBER


class _SieveOfEratosthenes(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Sieve of Eratosthenes")} is an {ALGORITHM.key.get_reference()} that finds all
{PRIME_NUMBER.key.get_reference(phrase="prime numbers")} up to a given bound n.

It works by iteratively marking multiples of each prime starting from 2; any unmarked number remaining is prime.

The input bound n is typically a {NATURAL_NUMBER.key.get_reference(phrase="natural number")}.
"""


SIEVE_OF_ERATOSTHENES = _SieveOfEratosthenes(
    key=DefinitionKey(
        name="Sieve of Eratosthenes",
        field=FieldName.MATHEMATICS,
    )
)
