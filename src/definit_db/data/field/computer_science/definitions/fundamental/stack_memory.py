from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.deallocation import DEALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.variable import VARIABLE
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.last_in_first_out import LAST_IN_FIRST_OUT


class _StackMemory(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A region of {COMPUTER_MEMORY.key.get_reference()} used for static 
{MEMORY_ALLOCATION.key.get_reference()} during {PROGRAM.key.get_reference()} execution. It stores 
{DATA.key.get_reference()} in a {LAST_IN_FIRST_OUT.key.get_reference()} order, automatically allocating and 
{DEALLOCATION.key.get_reference(phrase="deallocating")} memory as {FUNCTION.key.get_reference("functions")} are called 
and return. The stack manages local {VARIABLE.key.get_reference("variables")} and function call 
{DATA.key.get_reference(phrase="data")}.

---

For example, when a function A calls function B, which in turn calls function C, the stack grows as each function is 
entered — C on top of B on top of A — and shrinks in the reverse order as each function returns: C first, then B, then 
A. The local data of each function is removed as soon as that function returns, which is what makes the ordering 
last-in-first-out.
"""


STACK_MEMORY = _StackMemory(DefinitionKey(name="stack memory", field=FieldName.COMPUTER_SCIENCE))
