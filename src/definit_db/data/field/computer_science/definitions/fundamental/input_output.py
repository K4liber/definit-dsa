from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.software_system import SOFTWARE_SYSTEM


class _InputOutput(Definition):
    def _get_content(self) -> str:
        return f"""
Input output (I/O) is the transfer of {DATA.key.get_reference(phrase="data")} between 
a {COMPUTER.key.get_reference()} and
the outside world. Input is {DATA.key.get_reference(phrase="data")} received into the 
{SOFTWARE_SYSTEM.key.get_reference(phrase="system")}, while output is {DATA.key.get_reference(phrase="data")} sent out; 
both flow through {HARDWARE.key.get_reference(phrase="hardware")} devices.

---

A keyboard provides input: each key press sends data into the {COMPUTER.key.get_reference()}. 
A display provides output: the {COMPUTER.key.get_reference()}
sends data out to be shown on the screen. Together these devices let a person interact with 
a running {PROGRAM.key.get_reference()}.
"""


INPUT_OUTPUT = _InputOutput(
    key=DefinitionKey(
        name="input output",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=["I/O", "input/output"],
)
