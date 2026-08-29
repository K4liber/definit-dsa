from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.hash_table import (
    HASH_TABLE,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.set import SET
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.array import ARRAY
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.map import MAP
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.fundamental.distinctness import DISTINCTNESS
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _HashSet(Definition):
    def _get_content(self) -> str:
        return f"""
A hash set is a {SET.key.get_reference(phrase="set")} implementation that uses a 
{HASH_TABLE.key.get_reference(phrase="hash table")} to store {DISTINCTNESS.key.get_reference(phrase="distinct")} 
{ITEM.key.get_reference(phrase="elements")}. It {MAP.key.get_reference(phrase="maps")} each element through a 
hash-based structure so membership tests, insertions, and removals can 
usually be performed {EFFICIENCY.key.get_reference(phrase="efficiently")}.

---

For example, a hash set of registered usernames {{"alice", "bob", "carol"}} stores only the names themselves, with 
no associated values. To check whether "bob" is already registered, the name is hashed to locate a position in the 
underlying {ARRAY.key.get_reference(phrase="array")}, and the stored element at that position is compared directly. 
Adding "alice" a second time is detected and ignored, keeping each name present at most once.
"""


HASH_SET = _HashSet(
    key=DefinitionKey(
        name="hash set",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=("hashset", "set"),
)
