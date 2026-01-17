from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.combination import COMBINATION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _BinomialCoefficient(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a number that counts how many ways to choose k {ITEM.key.get_reference("items")} 
from n {ITEM.key.get_reference("items")}, ignoring order.

It is closely related to {COMBINATION.key.get_reference("combinations")} and is commonly written as "n choose k".
"""


BINOMIAL_COEFFICIENT = _BinomialCoefficient(
    key=DefinitionKey(
        name="binomial coefficient",
        field=FieldName.MATHEMATICS,
    )
)
