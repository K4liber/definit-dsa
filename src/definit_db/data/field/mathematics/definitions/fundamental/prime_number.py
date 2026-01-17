from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER


class _PrimeNumber(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a positive {INTEGER.key.get_reference("integer")} greater than 1 that has
exactly two positive divisors: 1 and itself.
"""


PRIME_NUMBER = _PrimeNumber(
    key=DefinitionKey(
        name="prime number",
        field=FieldName.MATHEMATICS,
    )
)
