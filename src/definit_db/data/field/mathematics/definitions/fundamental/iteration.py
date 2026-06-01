from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Iteration(Definition):
    def _get_content(self) -> str:
        return f"""
A single execution of a {SEQUENCE.key.get_reference()} of 
{INSTRUCTION.key.get_reference("instructions")}, performed once each time a repetitive process repeats.

---

Counting from 1 to 3 takes three iterations: one
{INSTRUCTION.key.get_reference("instruction")} carried out for each number.
"""


ITERATION = _Iteration(
    key=DefinitionKey(
        name="iteration",
        field=FieldName.MATHEMATICS,
    )
)
