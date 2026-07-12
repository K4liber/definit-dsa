from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE


class _InputOutput(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} (I/O) is the transfer of {DATA.key.get_reference(phrase="data")} between a computer and
the outside world. Input is data received into the system, while output is data sent out; both flow through
{HARDWARE.key.get_reference(phrase="hardware")} devices.

---

A keyboard provides input: each key press sends data into the computer. A display provides output: the computer
sends data out to be shown on the screen. Together these devices let a person interact with a running program.
"""


INPUT_OUTPUT = _InputOutput(
    key=DefinitionKey(
        name="input output",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
