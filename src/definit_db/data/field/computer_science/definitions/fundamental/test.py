from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _Test(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a procedure or experiment used to evaluate whether a system or component
behaves as expected under specified {CRITERION.key.get_reference("conditions")}.

A test typically takes some {DATA.key.get_reference("data")} (the {INPUT_DATA.key.get_reference()}) and produces
observations (outputs) that can be compared to expected results.

---

To test a {FUNCTION.key.get_reference()} that performs {SORTING.key.get_reference()} on 
{NUMBER.key.get_reference(phrase="numbers")}, one might give it the input [3, 1, 2] and check whether it returns 
[1, 2, 3]. The test passes when the actual output matches the expected output, and fails when it does not — revealing 
either a mistake in the function or a mistake in the expected result.
"""


TEST = _Test(
    key=DefinitionKey(
        name="test",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
