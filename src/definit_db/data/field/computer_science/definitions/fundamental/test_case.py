from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.set import SET
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.list import LIST
from definit_db.data.field.computer_science.definitions.fundamental.test import TEST
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _TestCase(Definition):
    def _get_content(self) -> str:
        return f"""
A single instance of a {TEST.key.get_reference("test")}, defined by a specific
{SET.key.get_reference("set")} of {INPUT_DATA.key.get_reference("inputs")}, evaluation 
{CRITERION.key.get_reference("criteria")} and expected results.

---

One test case for a {FUNCTION.key.get_reference()} that performs {SORTING.key.get_reference()} is: input
[3, 1, 2], expected output [1, 2, 3]. Another test case for the same function is: input [5, 5, 5] (a 
{LIST.key.get_reference("list")} where every {NUMBER.key.get_reference()} is the same), expected output [5, 5, 5]. 
Each test case checks the function against one specific situation; together, many test cases build confidence that the 
function works in general.
"""


TEST_CASE = _TestCase(
    key=DefinitionKey(
        name="test case",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
