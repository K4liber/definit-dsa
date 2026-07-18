from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _Bug(Definition):
    def _get_content(self) -> str:
        return f"""
An error or defect in a system, {PROGRAM.key.get_reference("program")}, or
{ALGORITHM.key.get_reference("algorithm")} that causes it to behave incorrectly or produce unexpected results.

---

A program meant to compute the average of exam scores contains the {INSTRUCTION.key.get_reference(phrase="instruction")}
"divide by the count minus one" instead of "divide by the count". This bug makes every reported average too large,
so the program silently produces incorrect results rather than failing visibly.
"""


BUG = _Bug(
    key=DefinitionKey(
        name="bug",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
