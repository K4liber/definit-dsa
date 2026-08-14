from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.code import CODE
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.software_system import SOFTWARE_SYSTEM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _ReverseEngineering(Definition):
    def _get_content(self) -> str:
        return f"""
The process of analyzing a {PROGRAM.key.get_reference("program")} or 
{SOFTWARE_SYSTEM.key.get_reference(phrase="system")} to 
discover its components, structure, and {OPERATION.key.get_reference("operation")}, often by examining its 
{DATA.key.get_reference("data")} and behavior, without access to its source {CODE.key.get_reference()}. 
Reverse engineering is used to understand how something works.

---

Given a program whose source code is unavailable, an engineer studies what it does for many different 
{INPUT_DATA.key.get_reference(phrase="inputs")}:
"input 5 gives 25, input 6 gives 36, input 7 gives 49." From these observations the engineer infers that the
underlying {ALGORITHM.key.get_reference()} squares the input — reconstructing the logic from behavior alone,
without ever reading the original code.
"""


REVERSE_ENGINEERING = _ReverseEngineering(
    key=DefinitionKey(
        name="reverse engineering",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
