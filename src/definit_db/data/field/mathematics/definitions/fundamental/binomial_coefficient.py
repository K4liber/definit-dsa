from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.combination import COMBINATION
from definit_db.data.field.mathematics.definitions.fundamental.factorial import FACTORIAL
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _BinomialCoefficient(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a number that counts how many ways to choose k {ITEM.key.get_reference("items")} 
from n {ITEM.key.get_reference("items")}, ignoring order.

It is closely related to {COMBINATION.key.get_reference("combinations")} and is commonly written as "n choose k".

Given the {FACTORIAL.key.get_reference("factorials")} of n, k, and n-k, it is computed as:

  n choose k = n! / (k! × (n-k)!)

---

Choosing 2 {ITEM.key.get_reference("items")} from 5 has "10" possible {COMBINATION.key.get_reference("combinations")}. 
This count, written "5 choose 2", is the {self.key.get_reference("binomial coefficient")} for "n = 5" and "k = 2", 
computed as 5! / (2! × 3!) = 120 / (2 × 6) = "10".
"""


BINOMIAL_COEFFICIENT = _BinomialCoefficient(
    key=DefinitionKey(
        name="binomial coefficient",
        field=FieldName.MATHEMATICS,
    )
)
