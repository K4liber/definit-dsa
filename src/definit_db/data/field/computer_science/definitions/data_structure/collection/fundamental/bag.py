from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.abstract_data_type import (
    ABSTRACT_DATA_TYPE,
)
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.iteration import ITERATION
from definit_db.data.field.mathematics.definitions.fundamental.multiset import MULTISET


class _Bag(Definition):
    def _get_content(self) -> str:
        return f"""
A bag is a {COLLECTION.key.get_reference(phrase="collection")} that allows for the storage of multiple 
{ITEM.key.get_reference(phrase="items")}, where the same item can be stored multiple times. It realizes the 
{MULTISET.key.get_reference(phrase="multiset")} abstraction as an 
{ABSTRACT_DATA_TYPE.key.get_reference(phrase="abstract data type")}, but focuses on the operations of adding items and 
{ITERATION.key.get_reference(phrase="iterating")} over them; removing items is not supported.

---

For example, a bag collecting exam scores might hold {72, 85, 72, 90}: the score 72 appears twice, and that 
multiplicity is preserved. A program can add more scores and walk through every stored item, but it cannot remove a 
specific one.
"""


BAG = _Bag(
    key=DefinitionKey(
        name="bag",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
