from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.code import CODE
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.disk import DISK
from definit_db.data.field.computer_science.definitions.fundamental.operating_system import OPERATING_SYSTEM
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _Process(Definition):
    def _get_content(self) -> str:
        return f"""
An instance of a {PROGRAM.key.get_reference(phrase="program")}
that is being executed by the {OPERATING_SYSTEM.key.get_reference(phrase="operating system")}. When launched, a
process receives its own region of {COMPUTER_MEMORY.key.get_reference(phrase="memory")} for its 
{CODE.key.get_reference(phrase="code")} and {DATA.key.get_reference(phrase="data")}.

---

A {PROGRAM.key.get_reference(phrase="program")} is static {CODE.key.get_reference(phrase="code")} stored on a 
{DISK.key.get_reference(phrase="disk")}, while a
process is that program in motion. Running the same program twice creates two
processes, each with its own {COMPUTER_MEMORY.key.get_reference(phrase="memory")} and state, even though both came
from the same program.
"""


PROCESS = _Process(
    key=DefinitionKey(
        name="process",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
