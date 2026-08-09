from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.call_stack import CALL_STACK
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.stack_memory import STACK_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.variable import VARIABLE
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.base_case import BASE_CASE
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION


class _StackOverflow(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
stack overflow occurs when a {PROGRAM.key.get_reference()} attempts to use more 
{STACK_MEMORY.key.get_reference()} than is available. This typically happens when the {CALL_STACK.key.get_reference()} 
grows too large, often due to excessive {FUNCTION.key.get_reference()} {RECURSION.key.get_reference()} or allocating 
too many local {VARIABLE.key.get_reference("variables")}. When stack overflow occurs, the program usually 
terminates with an error.

---

For example, a {RECURSION.key.get_reference(phrase="recursive")} 
{FUNCTION.key.get_reference(phrase="function")} that calls itself on every step without ever reaching 
a {BASE_CASE.key.get_reference()} keeps adding entries to the call stack: one for the first call, another for the 
recursive call, another for the next, and so on. Because each entry consumes stack memory, the stack eventually fills 
up and the next call cannot be placed, which is when the stack overflow occurs.
"""


STACK_OVERFLOW = _StackOverflow(DefinitionKey(name="stack overflow", field=FieldName.COMPUTER_SCIENCE))
