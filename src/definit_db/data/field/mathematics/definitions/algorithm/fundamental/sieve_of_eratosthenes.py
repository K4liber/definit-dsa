from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.composite_number import COMPOSITE_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.iteration import ITERATION
from definit_db.data.field.mathematics.definitions.fundamental.natural_number import NATURAL_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.prime_number import PRIME_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.square import SQUARE
from definit_db.data.field.mathematics.definitions.fundamental.square_root import SQUARE_ROOT


class _SieveOfEratosthenes(Definition):
    def _get_content(self) -> str:
        return f"""
An {ALGORITHM.key.get_reference()} that finds all
{PRIME_NUMBER.key.get_reference(phrase="prime numbers")} up to a given {BOUND.key.get_reference()} n.

It works by {ITERATION.key.get_reference(phrase="iteratively")} marking multiples of each prime starting from 2; 
any unmarked number remaining is prime. Marking can stop as soon as the next unmarked number's 
{SQUARE.key.get_reference()} exceeds n, since any {COMPOSITE_NUMBER.key.get_reference(phrase="composite number")} 
up to n must be divisible by a {PRIME_NUMBER.key.get_reference(phrase="prime number")} no greater than its 
own {SQUARE_ROOT.key.get_reference()}.

The {INPUT_DATA.key.get_reference(phrase="input")} bound n is typically a 
{NATURAL_NUMBER.key.get_reference(phrase="natural number")}.

---

To find all primes up to n = 30: start with the numbers 2 through 30, then cross out every multiple of 2
(4, 6, 8, ...), every remaining multiple of 3 (9, 15, 21, ...), and every remaining multiple of 5 (25). Since
7 × 7 = 49 exceeds 30, no further marking is needed. The numbers that are never crossed out —
2, 3, 5, 7, 11, 13, 17, 19, 23, and 29 — are exactly the prime numbers up to 30.
"""


SIEVE_OF_ERATOSTHENES = _SieveOfEratosthenes(
    key=DefinitionKey(
        name="Sieve of Eratosthenes",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["sieve", "prime sieve"],
)
