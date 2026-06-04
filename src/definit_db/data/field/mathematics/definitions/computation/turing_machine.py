from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _TuringMachine(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a mathematical model of {COMPUTATION.key.get_reference()} that defines an
abstract machine. It consists of an infinite tape divided into cells, a head that can read and write symbols on
the tape, a state register that stores the machine's current state, and a finite table of
{INSTRUCTION.key.get_reference("instructions")} that determines the machine's behavior. The Turing machine
processes input by following a {SEQUENCE.key.get_reference()} of state transitions based on the current state
and the symbol being read.

---

Imagine a Turing machine whose tape holds the single symbol "0". Its only
{INSTRUCTION.key.get_reference("instruction")} says: if the head reads "0", write "1" and then stop.
Running the machine performs a {SEQUENCE.key.get_reference()} of one step that reads the symbol, follows the
instruction, and changes the tape from "0" to "1".
"""


TURING_MACHINE = _TuringMachine(DefinitionKey(name="Turing machine", field=FieldName.MATHEMATICS))
