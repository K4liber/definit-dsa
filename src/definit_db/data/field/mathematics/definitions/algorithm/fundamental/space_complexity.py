from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION


class _SpaceComplexity(Definition):
    def _get_content(self) -> str:
        return f"""
A measure of {COMPLEXITY.key.get_reference()} that quantifies the amount of memory or storage space an 
{ALGORITHM.key.get_reference()} requires as a {FUNCTION.key.get_reference()} of the input size. 
Space complexity describes how the memory requirements grow with increasing input size.
"""


SPACE_COMPLEXITY = _SpaceComplexity(
    key=DefinitionKey(
        name="space complexity",
        field=FieldName.MATHEMATICS,
    )
)
