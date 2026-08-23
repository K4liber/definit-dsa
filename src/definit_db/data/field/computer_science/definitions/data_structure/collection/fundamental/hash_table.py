from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.associative_array import (
    ASSOCIATIVE_ARRAY,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.array import ARRAY
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.hash_function import HASH_FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX


class _HashTable(Definition):
    def _get_content(self) -> str:
        return f"""
{DATA_STRUCTURE.key.get_reference(phrase="Data structure")} that implements 
{ASSOCIATIVE_ARRAY.key.get_reference(phrase="associative array")} using a 
{HASH_FUNCTION.key.get_reference(phrase="hash function")} to 
{COMPUTATION.key.get_reference(phrase="compute")} an {INDEX.key.get_reference(phrase="index")} 
into an {ARRAY.key.get_reference(phrase="array")} of buckets or slots, from which the desired value can be found.

---

For example, to store a phone book in a hash table, the key "Alice" is passed through a hash 
{FUNCTION.key.get_reference(phrase="function")} that produces an index such as 42. The pair ("Alice", "555-0100") 
is then stored at position 42 in the underlying array. To retrieve 
Alice's number later, the same key is hashed again to obtain index 42, and the value is read directly from that 
position, making lookup very fast on average.
"""


HASH_TABLE = _HashTable(
    key=DefinitionKey(
        name="hash table",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=("hash map", "hashmap"),
)
