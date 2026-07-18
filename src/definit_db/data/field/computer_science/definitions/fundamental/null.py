from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.linked_list import LINKED_LIST
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.object import OBJECT
from definit_db.data.field.computer_science.definitions.fundamental.pointer import POINTER
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _Null(Definition):
    def _get_content(self) -> str:
        return f"""
A special value that represents "no value" or 
"no {OBJECT.key.get_reference(phrase="object")}".

It is often used to indicate that a {POINTER.key.get_reference(phrase="pointer")} does not refer to
a valid {COMPUTER_MEMORY.key.get_reference(phrase="memory")} location (i.e., it points to nothing).

---

In a {LINKED_LIST.key.get_reference(phrase="linked list")}, each {NODE.key.get_reference(phrase="node")} holds a
{POINTER.key.get_reference(phrase="pointer")} to the next node. The last node has no successor, so its pointer is
set to null to mark the end of the list. Code that walks the list checks for null to know when to stop.
"""


NULL = _Null(
    key=DefinitionKey(
        name="null",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
