from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.control_structure import CONTROL_STRUCTURE
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.iteration import ITERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Loop(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {CONTROL_STRUCTURE.key.get_reference()} that repeats a {SEQUENCE.key.get_reference()} of 
{INSTRUCTION.key.get_reference("instructions")} until a specified condition is met or for a predetermined 
number of {ITERATION.key.get_reference("iterations")}.

---

A loop that repeats the {INSTRUCTION.key.get_reference("instruction")} "add 1 to the total" five times
changes the total from 0 to 5.
"""


LOOP = _Loop(DefinitionKey(name="loop", field=FieldName.MATHEMATICS))
