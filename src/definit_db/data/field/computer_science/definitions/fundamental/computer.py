from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Computer(Definition):
    def _get_content(self) -> str:
        return f"""
A device that can execute {INSTRUCTION.key.get_reference(phrase="instructions")}
to process {INFORMATION.key.get_reference()} and perform tasks automatically. A computer can store, retrieve, and
manipulate {DATA.key.get_reference(phrase="data")} according to instructions.

---

A pocket calculator is a simple computer: it takes {NUMBER.key.get_reference(phrase="numbers")} such as 7 and 5 as
{INPUT_DATA.key.get_reference()}, follows the built-in instruction "multiply", and outputs the data 35.
"""


COMPUTER = _Computer(DefinitionKey(name="computer", field=FieldName.COMPUTER_SCIENCE))
