from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.numeral_system import NUMERAL_SYSTEM
from definit_db.data.field.mathematics.definitions.fundamental.radix import RADIX


class _HexadecimalCode(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a representation of a value written in the hexadecimal 
{NUMERAL_SYSTEM.key.get_reference("numeral system")}.

Hexadecimal is a positional numeral system with {RADIX.key.get_reference("radix")} 16, 
commonly using digits 0-9 and letters A-F.
"""


HEXADECIMAL_CODE = _HexadecimalCode(
    key=DefinitionKey(
        name="hexadecimal code",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
