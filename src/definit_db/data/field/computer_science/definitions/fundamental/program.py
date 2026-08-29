from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Program(Definition):
    def _get_content(self) -> str:
        return f"""
A {SEQUENCE.key.get_reference()} of {INSTRUCTION.key.get_reference("instructions")} that 
a {COMPUTER.key.get_reference()} can execute to perform a specific task. A program defines the 
{OPERATION.key.get_reference("operations")} that should be carried out and the order in which they should be executed.

---

A program that computes the average of exam scores implements an {ALGORITHM.key.get_reference()} as a concrete sequence 
of instructions: read each score, add them, then divide by the count. The same algorithm can be expressed by many
different programs.
"""


PROGRAM = _Program(
    DefinitionKey(name="program", field=FieldName.COMPUTER_SCIENCE),
    aliases=["computer program"],
)
