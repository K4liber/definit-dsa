from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.abstract_data_type import (
    ABSTRACT_DATA_TYPE,
)
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.map import MAP
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.distinctness import DISTINCTNESS


class _AssociativeArray(Definition):
    def _get_content(self) -> str:
        return f"""
An {ABSTRACT_DATA_TYPE.key.get_reference(phrase="abstract data type")} that 
{MAP.key.get_reference(phrase="maps")} keys to values. It is a {COLLECTION.key.get_reference(phrase="collection")} 
of key-value pairs, where each key is {DISTINCTNESS.key.get_reference(phrase="distinct")} and is used to access the 
corresponding value. Associative arrays allow for efficient {OPERATION.key.get_reference(phrase="operations")}: 
retrieval, insertion, and deletion of values based on their keys.

---

For example, a phone book can be modeled as an associative array where each person's name serves as the key and their 
phone number as the value. Looking up the key "Alice" retrieves her number, inserting a new contact adds a new 
key-value pair, and deleting "Alice" removes her entry. Because each key must be distinct, assigning a second number 
to "Alice" replaces the previous value rather than creating a duplicate entry.
"""


ASSOCIATIVE_ARRAY = _AssociativeArray(
    key=DefinitionKey(
        name="associative_array",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
