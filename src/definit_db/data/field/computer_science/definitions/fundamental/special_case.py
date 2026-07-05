from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.edge_case import EDGE_CASE
from definit_db.data.field.computer_science.definitions.fundamental.test_case import TEST_CASE
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _SpecialCase(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a particular {TEST_CASE.key.get_reference("test case")} that satisfies additional
{CRITERION.key.get_reference("conditions")}, making it a more specific situation within a broader category.

Special cases may be related to {EDGE_CASE.key.get_reference("edge cases")}, but they are not necessarily 
{BOUND.key.get_reference(phrase="boundary")} conditions.

---

Within the broad category "integer", the special case "even {INTEGER.key.get_reference(phrase="integer")}" adds
the condition "divisible by 2". A {FUNCTION.key.get_reference()} written for all integers may need separate handling 
for the even special case — for example, an integer is even exactly when its last 
{BIT.key.get_reference(phrase="binary digit")} is 0, so the check can be done with a single 
{BITWISE_OPERATION.key.get_reference(phrase="bitwise")} test instead of division.
"""


SPECIAL_CASE = _SpecialCase(
    key=DefinitionKey(
        name="special case",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
