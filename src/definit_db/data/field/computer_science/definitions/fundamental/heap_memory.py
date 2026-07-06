from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.deallocation import DEALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.pointer import POINTER
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _HeapMemory(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a region of {COMPUTER_MEMORY.key.get_reference()} used for dynamic 
{MEMORY_ALLOCATION.key.get_reference()} during {PROGRAM.key.get_reference()} execution. It allows 
{DATA.key.get_reference()} to be allocated and {DEALLOCATION.key.get_reference(phrase="deallocated")} at runtime as 
needed. The heap is flexible: memory blocks can be allocated in any order and freed in any order.

---

For example, when a program creates data whose size or lifetime is not known in advance, that data is placed on the
heap. The program receives a {POINTER.key.get_reference()} to the allocated block and can access it for as long as
needed, freeing the block only when the data is no longer required.
"""


HEAP_MEMORY = _HeapMemory(DefinitionKey(name="heap memory", field=FieldName.COMPUTER_SCIENCE))
