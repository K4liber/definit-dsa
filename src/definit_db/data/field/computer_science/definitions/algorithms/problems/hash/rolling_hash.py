from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.hash_function import HASH_FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _RollingHash(Definition):
    def _get_content(self) -> str:
        return f"""
A rolling hash is an approach designed to enable efficient execution of the 
{HASH_FUNCTION.key.get_reference(phrase="hash function")} when the input is modified incrementally, such as when 
a window of fixed size moves over a {SEQUENCE.key.get_reference(phrase="sequence")}.

---

A naive {HASH_FUNCTION.key.get_reference(phrase="hash function")} recomputes the hash of each length-3 window in 
the {SEQUENCE.key.get_reference(phrase="sequence")} `[4, 7, 2, 9, 1]` from scratch, hashing `[4, 7, 2]`, then 
`[7, 2, 9]`, then `[2, 9, 1]` independently. A rolling hash instead updates the previous hash when the window slides: 
removing the contribution of `4`, shifting, and adding the contribution of `9` turns the hash of `[4, 7, 2]` into the 
hash of `[7, 2, 9]` in constant time, without reprocessing the overlapping `7` and `2`.
"""


ROLLING_HASH = _RollingHash(
    key=DefinitionKey(
        name="rolling_hash",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
