from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _Hardware(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} refers to the physical, tangible components of a {COMPUTER.key.get_reference()} —
the parts that can be touched. Hardware is contrasted with
{PROGRAM.key.get_reference(phrase="programs")} (software), which are the intangible
{INSTRUCTION.key.get_reference(phrase="instructions")} the hardware executes to process 
{DATA.key.get_reference(phrase="data")}.

---

A keyboard is hardware: a physical device with keys that lets a user type {INFORMATION.key.get_reference()}
into the computer.
"""


HARDWARE = _Hardware(DefinitionKey(name="hardware", field=FieldName.COMPUTER_SCIENCE))
