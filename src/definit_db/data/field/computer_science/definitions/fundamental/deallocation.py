from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _Deallocation(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the {OPERATION.key.get_reference()} of releasing a block of 
{COMPUTER_MEMORY.key.get_reference()} that was previously reserved through 
{MEMORY_ALLOCATION.key.get_reference()}, returning it to the pool of memory available for future use by a 
{PROGRAM.key.get_reference()}.

---

For example, after a program allocates a block to hold a temporary {DATA.key.get_reference("buffer")} and finishes using 
it, it deallocates the block so the same memory can be reused for a later allocation. Forgetting to deallocate blocks 
that are no longer needed gradually exhausts the available memory.
"""


DEALLOCATION = _Deallocation(DefinitionKey(name="deallocation", field=FieldName.COMPUTER_SCIENCE))
