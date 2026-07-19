from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.list import LIST
from definit_db.data.field.computer_science.definitions.fundamental.test_case import TEST_CASE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _EdgeCase(Definition):
    def _get_content(self) -> str:
        return f"""
A {TEST_CASE.key.get_reference("test case")} designed to cover unusual or
{BOUND.key.get_reference("boundary")} {CRITERION.key.get_reference("conditions")} where a system, 
{ALGORITHM.key.get_reference("algorithm")}, or {FUNCTION.key.get_reference("function")} 
may behave differently.

---

For a function that finds the smallest item in a {LIST.key.get_reference()}, the edge cases include the empty
list (no item to choose), a single-element list (only one candidate), and a list where every item is equal (no
{UNIQUENESS.key.get_reference(phrase="unique")} smallest). Each sits at a boundary the function must handle
without crashing or returning a wrong result.
"""


EDGE_CASE = _EdgeCase(
    key=DefinitionKey(
        name="edge case",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
