from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.fundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.object import OBJECT
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.pointer import POINTER


class _DeepCopy(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an {OPERATION.key.get_reference(phrase="operation")} that creates a new 
{OBJECT.key.get_reference(phrase="object")} with the same value as an existing object, including independent copies 
of the nested {DATA_STRUCTURE.key.get_reference(phrase="data structures")} it refers to. The copy uses separate 
{MEMORY_ALLOCATION.key.get_reference(phrase="memory allocations")}, so changing nested data through one object does 
not change the other object through shared {POINTER.key.get_reference(phrase="pointers")}.

---

Suppose object A holds a list that itself references two other objects, B and C. A deep copy of A produces a new object 
A' that references brand-new copies B' and C' rather than the originals. Modifying a value inside B through A leaves B' 
untouched, because A' reaches B' through its own pointers and shares no memory with A. A shallow copy of A, in contrast, 
would reuse the same B and C, so edits made through either copy would be visible through the other.
"""


DEEP_COPY = _DeepCopy(
    key=DefinitionKey(
        name="deep copy",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
