from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.bitwise_operation import BITWISE_OPERATION


class _Bitmask(Definition):
    def _get_content(self) -> str:
        return f"""
A bitmask is a {BINARY_REPRESENTATION.key.get_reference(phrase="binary representation")} pattern whose 
{BIT.key.get_reference(phrase="bits")} are used with {BITWISE_OPERATION.key.get_reference(phrase="bitwise operations")} 
to select, set, clear, toggle, or test corresponding bits in another value.
"""


BITMASK = _Bitmask(
    key=DefinitionKey(
        name="bitmask",
        field=FieldName.COMPUTER_SCIENCE,
    )
)