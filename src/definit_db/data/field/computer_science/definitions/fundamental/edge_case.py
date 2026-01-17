from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.test_case import TEST_CASE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.analysis.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _EdgeCase(Definition):
    def _get_content(self) -> str:
        return f"""
An {self.key.get_reference()} is a {TEST_CASE.key.get_reference("test case")} designed to cover unusual or
{BOUND.key.get_reference("boundary")} {CRITERION.key.get_reference("conditions")} where a system, 
{ALGORITHM.key.get_reference("algorithm")}, or {FUNCTION.key.get_reference("function")} 
may behave differently.
"""


EDGE_CASE = _EdgeCase(
    key=DefinitionKey(
        name="edge case",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
