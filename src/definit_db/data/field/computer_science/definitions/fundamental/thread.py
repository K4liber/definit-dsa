from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.concurrency import CONCURRENCY
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.process import PROCESS
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _Thread(Definition):
    def _get_content(self) -> str:
        return f"""
A unit of execution within a {PROCESS.key.get_reference(phrase="process")}.

Threads within the same process typically share {COMPUTER_MEMORY.key.get_reference(phrase="memory")} and resources,
but can run different {OPERATION.key.get_reference(phrase="operations")}.

---

A {PROCESS.key.get_reference(phrase="process")} that handles a long 
{COMPUTATION.key.get_reference(phrase="computation")} while still accepting user 
{INPUT_DATA.key.get_reference(phrase="input")} can split the work across two threads: 
one performs the {COMPUTATION.key.get_reference(phrase="computation")}, the other
listens for {INPUT_DATA.key.get_reference(phrase="input")}. Because they belong to the same process they share 
{COMPUTER_MEMORY.key.get_reference(phrase="memory")}, and because they run as separate threads the 
{PROGRAM.key.get_reference(phrase="program")} achieves {CONCURRENCY.key.get_reference(phrase="concurrency")} 
without starting a second process.
"""


THREAD = _Thread(
    key=DefinitionKey(
        name="thread",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
