from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.computation.deterministic import DETERMINISTIC
from definit_db.data.field.mathematics.definitions.computation.turing_machine import TURING_MACHINE
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _NondeterministicTuringMachine(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {TURING_MACHINE.key.get_reference("Turing machine")} where each
{INSTRUCTION.key.get_reference()} can have multiple possible next states and actions. Given the current
state and the symbol being read, the machine can "choose" among several possible transitions, effectively
exploring multiple {COMPUTATION.key.get_reference("computational")} {PATH.key.get_reference("paths")} simultaneously 
and accepting if any path leads to acceptance. It recognizes exactly the same languages as a 
{DETERMINISTIC.key.get_reference("deterministic")} Turing machine, but this branching
can reach an accepting path in far fewer steps, which makes it a convenient model for reasoning about how hard a 
{PROBLEM.key.get_reference("problem")} is to solve.

---

A {TURING_MACHINE.key.get_reference("Turing machine")} that, upon reading "0", may either write "1" and move
right or instead halt — two different transitions allowed for the same (state, symbol) pair — is
nondeterministic. Conceptually it follows both {INSTRUCTION.key.get_reference("instructions")} at once and
accepts the input if any of the explored paths accepts.
"""


NONDETERMINISTIC_TURING_MACHINE = _NondeterministicTuringMachine(
    DefinitionKey(name="nondeterministic Turing machine", field=FieldName.MATHEMATICS)
)
