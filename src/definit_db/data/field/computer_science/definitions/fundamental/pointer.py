from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.variable import VARIABLE
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _Pointer(Definition):
    def _get_content(self) -> str:
        return f"""
A {VARIABLE.key.get_reference()} whose value is a memory address: it refers to a
location in {COMPUTER_MEMORY.key.get_reference()}. A pointer can be used to indirectly access
{INFORMATION.key.get_reference()} stored at that location.

---

Suppose memory holds a temperature reading at address 100. A pointer whose value is 100 lets a program read or
update that reading without copying it. Many pointers can refer to the same location, so an update made through
one pointer is immediately visible through any other pointer to that location.
"""


POINTER = _Pointer(
    key=DefinitionKey(
        name="pointer",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
