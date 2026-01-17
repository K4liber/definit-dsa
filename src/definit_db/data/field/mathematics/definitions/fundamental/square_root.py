from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _SquareRoot(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} of a non-negative {NUMBER.key.get_reference("number")} x is a non-negative
number y such that y² = x.
"""


SQUARE_ROOT = _SquareRoot(
    key=DefinitionKey(
        name="square root",
        field=FieldName.MATHEMATICS,
    )
)
