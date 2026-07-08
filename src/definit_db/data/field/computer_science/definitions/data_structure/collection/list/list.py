from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.computer_science.definitions.fundamental.data_type import DATA_TYPE
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _List(Definition):
    def _get_content(self) -> str:
        return f"""
An ordered {COLLECTION.key.get_reference(phrase="collection")}. Also known as a 
{SEQUENCE.key.get_reference(phrase="sequence")}. One can add, remove, and pop any element from the list. A list 
can store elements of different {DATA_TYPE.key.get_reference(phrase="types")}.

---

For example, a list holding the exam scores [72, 85, 90] keeps them in that exact order. Adding 91 to the end 
produces [72, 85, 90, 91], removing 85 leaves [72, 90, 91], and popping the last element returns 91 and leaves 
[72, 90]. Because order matters, [72, 85, 90] is a different list from [90, 85, 72].
"""


LIST = _List(
    key=DefinitionKey(
        name="list",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
