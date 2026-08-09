from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.deallocation import DEALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.heap_memory import HEAP_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.stack_memory import STACK_MEMORY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION


class _MemoryManagement(Definition):
    def _get_content(self) -> str:
        return f"""
The {OPERATION.key.get_reference()} of controlling how a {PROGRAM.key.get_reference()} 
uses {COMPUTER_MEMORY.key.get_reference()}.

It includes when and how {MEMORY_ALLOCATION.key.get_reference("memory is allocated")} and 
{DEALLOCATION.key.get_reference(phrase="freed")}, and aims to use memory 
{EFFICIENCY.key.get_reference(phrase="efficiently")} and safely.

---

For example, a program typically relies on two regions with different rules: the 
{STACK_MEMORY.key.get_reference()} is managed automatically 
(memory is claimed when a {FUNCTION.key.get_reference(phrase="function")} is called and released 
when it returns), while the {HEAP_MEMORY.key.get_reference()} is managed explicitly by the program, which must request 
blocks and later release them. Good memory management keeps each region balanced so the program neither runs out of 
memory nor holds on to memory it no longer needs.
"""


MEMORY_MANAGEMENT = _MemoryManagement(
    key=DefinitionKey(
        name="memory management",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
