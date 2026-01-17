from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.float import FLOAT
from definit_db.data.field.mathematics.definitions.fundamental.real_number import REAL_NUMBER


class _Double(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Double")} is a floating-point data type used to represent an approximation of a
{REAL_NUMBER.key.get_reference(phrase="real number")} with finite precision.

In many systems, a double provides about twice the precision of a {FLOAT.key.get_reference(phrase="float")}.
"""


DOUBLE = _Double(
    key=DefinitionKey(
        name="Double",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
