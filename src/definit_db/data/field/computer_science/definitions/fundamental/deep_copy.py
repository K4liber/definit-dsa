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
A deep copy is an {OPERATION.key.get_reference(phrase="operation")} that creates a new 
{OBJECT.key.get_reference(phrase="object")} with the same value as an existing object, including independent copies 
of the nested {DATA_STRUCTURE.key.get_reference(phrase="data structures")} it refers to. The copy uses separate 
{MEMORY_ALLOCATION.key.get_reference(phrase="memory allocations")}, so changing nested data through one object does 
not change the other object through shared {POINTER.key.get_reference(phrase="pointers")}.
"""


DEEP_COPY = _DeepCopy(
    key=DefinitionKey(
        name="deep copy",
        field=FieldName.COMPUTER_SCIENCE,
    )
)