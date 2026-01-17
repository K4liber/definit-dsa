from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM


class _Bug(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is an error or defect in a system, {PROGRAM.key.get_reference("program")}, or
{ALGORITHM.key.get_reference("algorithm")} that causes it to behave incorrectly or produce unexpected results.
"""


BUG = _Bug(
    key=DefinitionKey(
        name="bug",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
