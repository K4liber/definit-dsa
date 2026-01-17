from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.real_number import REAL_NUMBER


class _Float(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Float")} is a floating-point data type used to represent an approximation of a
{REAL_NUMBER.key.get_reference(phrase="real number")} with finite precision.
"""


FLOAT = _Float(
    key=DefinitionKey(
        name="Float",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
