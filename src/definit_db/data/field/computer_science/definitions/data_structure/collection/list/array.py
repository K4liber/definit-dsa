from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.list import LIST
from definit_db.data.field.computer_science.definitions.fundamental.data_type import DATA_TYPE
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX


class _Array(Definition):
    def _get_content(self) -> str:
        return f"""
Array is a {LIST.key.get_reference(phrase="list")} of elements of the same 
{DATA_TYPE.key.get_reference(phrase="type")}, stored contiguously so that each element can be accessed directly by 
its {INDEX.key.get_reference(phrase="index")}.

---

For example, an array holding the scores [72, 85, 90, 91] stores them in one contiguous block where the value at 
index 0 is 72, at index 1 is 85, and so on. Reading or replacing the value at a given index takes the same time no 
matter where it sits, because the index directly determines the element's position.
"""


ARRAY = _Array(
    key=DefinitionKey(
        name="array",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
