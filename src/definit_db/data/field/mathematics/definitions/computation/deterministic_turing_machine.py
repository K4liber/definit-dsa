from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.computation.turing_machine import TURING_MACHINE
from definit_db.data.field.mathematics.definitions.fundamental.determinism import DETERMINISM
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS


class _DeterministicTuringMachine(Definition):
    def _get_content(self) -> str:
        return f"""
A {DETERMINISM.key.get_reference("deterministic")} {TURING_MACHINE.key.get_reference("Turing machine")} where each
{INSTRUCTION.key.get_reference()} {UNIQUENESS.key.get_reference("uniquely")} determines the next state and action. 
Given the current state and the symbol being read, there is exactly one possible transition, making the machine's 
behavior completely predictable and reproducible.

---

A {TURING_MACHINE.key.get_reference("Turing machine")} that always writes "1" and moves right when it reads "0",
and always halts when it reads "1", is deterministic: for every (state, symbol) pair there is exactly one
{INSTRUCTION.key.get_reference()} to follow, so it behaves the same way every time it runs on the same input.
"""


DETERMINISTIC_TURING_MACHINE = _DeterministicTuringMachine(
    DefinitionKey(name="deterministic Turing machine", field=FieldName.MATHEMATICS)
)
