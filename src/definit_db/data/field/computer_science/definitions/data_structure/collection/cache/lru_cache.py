from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.hash_table import (
    HASH_TABLE,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.linked_list import LINKED_LIST
from definit_db.data.field.computer_science.definitions.fundamental.cache import CACHE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION


class _LruCache(Definition):
    def _get_content(self) -> str:
        return f"""
An LRU cache is a {CACHE.key.get_reference(phrase="cache")} that keeps recently used entries and removes the 
least recently used entry when it needs space for a new one. A common implementation combines a 
{HASH_TABLE.key.get_reference(phrase="hash table")} for fast lookup with a 
{LINKED_LIST.key.get_reference(phrase="linked list")} that records entries from most recently used to least 
recently used. Read and write {OPERATION.key.get_reference(phrase="operations")} update that recency order.
"""


LRU_CACHE = _LruCache(
    key=DefinitionKey(
        name="LRU cache",
        field=FieldName.COMPUTER_SCIENCE,
    )
)