from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.hash_table import (
    HASH_TABLE,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.set import SET


class _HashSet(Definition):
    def _get_content(self) -> str:
        return f"""
A hash set is a {SET.key.get_reference(phrase="set")} implementation that uses a 
{HASH_TABLE.key.get_reference(phrase="hash table")} to store unique elements. It maps each element through a 
hash-based structure so membership tests, insertions, and removals can usually be performed efficiently.
"""


HASH_SET = _HashSet(
    key=DefinitionKey(
        name="hash_set",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
