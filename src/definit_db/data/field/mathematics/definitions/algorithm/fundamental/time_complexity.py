from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _TimeComplexity(Definition):
    def _get_content(self) -> str:
        return f"""
A measure of {COMPLEXITY.key.get_reference()} that quantifies the amount of time an 
{ALGORITHM.key.get_reference()} takes to complete as a {FUNCTION.key.get_reference()} of the 
{INPUT_DATA.key.get_reference(phrase="input")} size. Time complexity describes how the number of 
{OPERATION.key.get_reference(phrase="operations")} or execution time grows with increasing input size.

---

An {ALGORITHM.key.get_reference()} that adds up every {NUMBER.key.get_reference(phrase="number")} in a 
{SEQUENCE.key.get_reference()} performs one addition per number, so summing "4" numbers takes "4" operations and "8" 
numbers takes "8"; its time complexity grows in direct proportion to the input size.
"""


TIME_COMPLEXITY = _TimeComplexity(
    key=DefinitionKey(
        name="time_complexity",
        field=FieldName.MATHEMATICS,
    )
)
