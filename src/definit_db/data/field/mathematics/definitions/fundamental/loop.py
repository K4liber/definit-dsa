from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Loop(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a control structure that repeats a {SEQUENCE.key.get_reference()} of 
{INSTRUCTION.key.get_reference("instructions")} multiple times until a specified condition is met or for a 
predetermined number of iterations. Loops enable efficient execution of repetitive tasks and are fundamental to 
iterating over data structures.
"""


LOOP = _Loop(DefinitionKey(name="loop", field=FieldName.MATHEMATICS))
