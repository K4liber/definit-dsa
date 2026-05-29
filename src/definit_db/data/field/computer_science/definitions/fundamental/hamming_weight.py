from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT


class _HammingWeight(Definition):
    def _get_content(self) -> str:
        return f"""
The Hamming weight of a {BINARY_REPRESENTATION.key.get_reference(phrase="binary representation")} is the number 
of {BIT.key.get_reference(phrase="bits")} whose value is 1. It is also called the population count or the number 
of set bits.
"""


HAMMING_WEIGHT = _HammingWeight(
    key=DefinitionKey(
        name="Hamming weight",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
