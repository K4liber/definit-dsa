from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.algorithms.bit.bit_manipulation import BIT_MANIPULATION
from definit_db.data.field.computer_science.definitions.algorithms.in_place_algorithm import IN_PLACE_ALGORITHM
from definit_db.data.field.computer_science.definitions.fundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.variable import VARIABLE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.xor import XOR


class _XorSwapAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
The XOR swap algorithm is an {ALGORITHM.key.get_reference(phrase="algorithm")} that swaps the values of two 
{VARIABLE.key.get_reference(phrase="variables")} by applying three {XOR.key.get_reference(phrase="XOR")} 
{BITWISE_OPERATION.key.get_reference(phrase="bitwise operations")}. It is a 
{BIT_MANIPULATION.key.get_reference(phrase="bit manipulation")} technique and an 
{IN_PLACE_ALGORITHM.key.get_reference(phrase="in-place algorithm")} because it exchanges the values without using 
an additional temporary variable.
"""


XOR_SWAP_ALGORITHM = _XorSwapAlgorithm(
    key=DefinitionKey(
        name="XOR swap algorithm",
        field=FieldName.COMPUTER_SCIENCE,
    )
)