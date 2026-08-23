from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.stack_memory import STACK_MEMORY
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.last_in_first_out import LAST_IN_FIRST_OUT


class _CallStack(Definition):
    def _get_content(self) -> str:
        return f"""
A region of {STACK_MEMORY.key.get_reference()} that tracks active 
{FUNCTION.key.get_reference("function")} calls during {PROGRAM.key.get_reference()} execution. 
It stores {INFORMATION.key.get_reference()} about each function call, including where to return after 
the function completes. When a function is called, its information is added to the call stack, 
and when it returns, that information is removed in {LAST_IN_FIRST_OUT.key.get_reference()} order.

---

For example, when `main` calls `compute`, which calls `save`, the call stack grows bottom-up as `main`, then `compute`, 
then `save`. When `save` returns, its entry is the first removed; `compute` then becomes the top again and resumes. The 
most recently called function is always the first to return, which is exactly the last-in-first-out rule.
"""


CALL_STACK = _CallStack(
    DefinitionKey(name="call stack", field=FieldName.COMPUTER_SCIENCE),
    aliases=("execution stack", "runtime stack"),
)
