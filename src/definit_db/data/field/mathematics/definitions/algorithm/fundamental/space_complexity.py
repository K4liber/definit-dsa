from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _SpaceComplexity(Definition):
    def _get_content(self) -> str:
        return f"""
A measure of {COMPLEXITY.key.get_reference()} that quantifies the amount of space an 
{ALGORITHM.key.get_reference()} requires as a {FUNCTION.key.get_reference()} of the input size. 
Space complexity describes how the space requirements grow with increasing input size.

---

An {ALGORITHM.key.get_reference()} that copies every {NUMBER.key.get_reference(phrase="number")} of a sequence 
into a new sequence stores one extra number per input: "3" numbers require "3" stored numbers and "6" numbers 
require "6", so its space complexity grows in direct proportion to the input size.
"""


SPACE_COMPLEXITY = _SpaceComplexity(
    key=DefinitionKey(
        name="space complexity",
        field=FieldName.MATHEMATICS,
    )
)
