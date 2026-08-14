from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _ControlStructure(Definition):
    def _get_content(self) -> str:
        return f"""
A construct that determines the order in which a {SEQUENCE.key.get_reference()} of 
{INSTRUCTION.key.get_reference("instructions")} is executed, rather than running them once from start to finish.

---

A rule that says "repeat the next {INSTRUCTION.key.get_reference("instruction")} while the door is open"
is a control structure: it decides when and how often the instruction runs.
"""


CONTROL_STRUCTURE = _ControlStructure(
    key=DefinitionKey(
        name="control structure",
        field=FieldName.MATHEMATICS,
    )
)
