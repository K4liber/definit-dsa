from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Processor(Definition):
    def _get_content(self) -> str:
        return f"""
A {HARDWARE.key.get_reference()} component of a {COMPUTER.key.get_reference()} 
that executes {INSTRUCTION.key.get_reference("instructions")} and performs {OPERATION.key.get_reference("operations")} 
on {DATA.key.get_reference(phrase="data")}. It is the central component responsible for carrying out the 
{COMPUTATION.key.get_reference(phrase="computational")} 
tasks defined by {PROGRAM.key.get_reference("programs")}, often referred to as the central processing unit (CPU).

---

When a program instructs the processor to add two {NUMBER.key.get_reference(phrase="numbers")}, 
the processor fetches the instruction, reads the two
{INPUT_DATA.key.get_reference(phrase="input")} values from {COMPUTER_MEMORY.key.get_reference(phrase="memory")}, 
executes the addition, and writes the result 
back — repeating this cycle millions of times per second to run an entire program containing thousands of instructions.
"""


PROCESSOR = _Processor(DefinitionKey(name="processor", field=FieldName.COMPUTER_SCIENCE))
