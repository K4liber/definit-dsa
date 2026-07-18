from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.data_type import DATA_TYPE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.last_in_first_out import LAST_IN_FIRST_OUT


class _AbstractDataType(Definition):
    def _get_content(self) -> str:
        return f"""
A mathematical model of a {DATA_TYPE.key.get_reference(phrase="data type")}, defined by 
its behavior from the point of view of a user of the {DATA.key.get_reference(phrase="data")}, specifically in terms 
of possible values, possible {OPERATION.key.get_reference(phrase="operations")} on data of this type, and the 
behavior of these operations.

---

For example, an abstract data type might describe a container that supports adding 
{ITEM.key.get_reference(phrase="items")}, removing the most recently added one, and checking whether it is empty - 
a {LAST_IN_FIRST_OUT.key.get_reference()} discipline - without specifying whether the items are stored as a contiguous 
block of {COMPUTER_MEMORY.key.get_reference(phrase="memory")} or as a chain of linked nodes. Any concrete realization 
that provides those operations with the agreed behavior is a valid implementation of that abstract data type.
"""


ABSTRACT_DATA_TYPE = _AbstractDataType(
    key=DefinitionKey(
        name="abstract_data_type",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
