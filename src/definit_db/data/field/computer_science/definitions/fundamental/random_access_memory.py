from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.array import ARRAY
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.fundamental.processor import PROCESSOR
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _RandomAccessMemory(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A type of {COMPUTER_MEMORY.key.get_reference()} that allows {DATA.key.get_reference()} 
to be read or written in almost the same amount of time regardless of the physical location of the data within the 
memory. This enables fast access to any memory location, making it suitable for storing data that needs to be 
quickly accessed and modified during {PROGRAM.key.get_reference()} execution.

---

When a {PROCESSOR.key.get_reference()} reads element 5 of a million-element {ARRAY.key.get_reference()}, it reaches 
that location just as fast as element 0 — there is no need to scan through the preceding elements first. 
This constant-time access is what lets programs index into arrays and other 
{DATA_STRUCTURE.key.get_reference(phrase="data structures")} without slowdown.
"""


RANDOM_ACCESS_MEMORY = _RandomAccessMemory(DefinitionKey(name="random access memory", field=FieldName.COMPUTER_SCIENCE))
