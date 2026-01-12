from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _NaturalNumber(Definition):
    def _get_content(self) -> str:
        return f"""
A natural {NUMBER.key.get_reference("number")} is a non-negative {INTEGER.key.get_reference("integer")}.
"""


NATURAL_NUMBER = _NaturalNumber(
    key=DefinitionKey(
        name="natural number",
        field=FieldName.MATHEMATICS,
    )
)
