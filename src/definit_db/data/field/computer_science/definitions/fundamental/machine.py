from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.fundamental.processor import PROCESSOR
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION


class _Machine(Definition):
    def _get_content(self) -> str:
        return f"""
In computing, a {self.key.get_reference()} is a physical or virtual {COMPUTER.key.get_reference(phrase="computer")}
that can run {PROGRAM.key.get_reference(phrase="programs")} and perform 
{COMPUTATION.key.get_reference(phrase="computation")}.

---

A laptop is a physical machine: its {HARDWARE.key.get_reference(phrase="hardware")} components, including a
{PROCESSOR.key.get_reference(phrase="processor")} that executes instructions, work together to run programs. A
virtual machine is also a machine, but it is implemented in software that emulates physical hardware, so programs
run on it as if it were real hardware.
"""


MACHINE = _Machine(
    key=DefinitionKey(
        name="machine",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
