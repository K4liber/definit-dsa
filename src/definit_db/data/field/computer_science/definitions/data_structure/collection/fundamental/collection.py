from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.abstract_data_type import (
    ABSTRACT_DATA_TYPE,
)
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _Collection(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an {ABSTRACT_DATA_TYPE.key.get_reference(phrase="abstract data type")} that groups a 
variable number of {ITEM.key.get_reference(phrase="items")} (possibly zero) that share some significance and need to be 
{OPERATION.key.get_reference(phrase="operated")} upon together in a controlled fashion.

---

A collection of three items supports adding a new item, removing one that is no longer needed, and asking how many 
items it currently holds. Different kinds of collections impose different rules - some keep the items in the order they 
were added, some prevent duplicates - but all of them treat the grouped items as a single unit that can be processed 
together.
"""


COLLECTION = _Collection(
    key=DefinitionKey(
        name="collection",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
