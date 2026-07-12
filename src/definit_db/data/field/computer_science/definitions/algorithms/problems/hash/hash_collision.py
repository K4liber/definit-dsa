from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.hash_table import (
    HASH_TABLE,
)
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.hash import HASH
from definit_db.data.field.mathematics.definitions.fundamental.hash_function import HASH_FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _HashCollision(Definition):
    def _get_content(self) -> str:
        return f"""
A situation in which two different {INPUT_DATA.key.get_reference(phrase="inputs")} produce the same 
{HASH.key.get_reference(phrase="hash value")} when processed by a 
{HASH_FUNCTION.key.get_reference(phrase="hash function")}. This can lead to 
{DATA.key.get_reference(phrase="data")} integrity issues and is a key consideration in the design of hash functions 
and {HASH_TABLE.key.get_reference(phrase="hash tables")}.

---

Under a {HASH_FUNCTION.key.get_reference(phrase="hash function")} that returns the last digit of a 
{NUMBER.key.get_reference(phrase="number")}, the {INPUT_DATA.key.get_reference(phrase="inputs")} 17 and 27 both 
produce the {HASH.key.get_reference(phrase="hash")} 7, so they collide. When stored in a 
{HASH_TABLE.key.get_reference(phrase="hash table")}, both entries land in the same slot, which the table must resolve 
(for example by chaining) so that neither value is lost.
"""


HASH_COLLISION = _HashCollision(
    key=DefinitionKey(
        name="hash_collision",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
