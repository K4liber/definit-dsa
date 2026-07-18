from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.deallocation import DEALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.heap_memory import HEAP_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.iteration import ITERATION
from definit_db.data.field.mathematics.definitions.fundamental.loop import LOOP


class _HeapOverflow(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
heap overflow occurs when a {PROGRAM.key.get_reference()} attempts to use more 
{HEAP_MEMORY.key.get_reference()} than is available. This typically happens when too much dynamic 
{MEMORY_ALLOCATION.key.get_reference()} occurs without proper {DEALLOCATION.key.get_reference()}, or when attempting to 
allocate a very large amount of {COMPUTER_MEMORY.key.get_reference()} at once. When heap overflow occurs, the program 
may fail to allocate memory and typically terminates with an error.

---

For example, a program that allocates memory inside a {LOOP.key.get_reference()} without ever freeing it gradually fills
the heap. After enough {ITERATION.key.get_reference("iterations")}, the next allocation cannot find a free block large 
enough, so it fails; the program must then either handle the failure or terminate.
"""


HEAP_OVERFLOW = _HeapOverflow(DefinitionKey(name="heap overflow", field=FieldName.COMPUTER_SCIENCE))
