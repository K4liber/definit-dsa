from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.mathematics.definitions.fundamental.multiset import MULTISET
from definit_db.data.field.mathematics.definitions.fundamental.permutation import PERMUTATION
from definit_db.data.field.mathematics.definitions.fundamental.reordering import REORDERING


class _Anagram(Definition):
    def _get_content(self) -> str:
        return f"""
An anagram is a {STRING.key.get_reference(phrase="string")} formed by 
{REORDERING.key.get_reference(phrase="rearranging")} the {CHARACTER.key.get_reference(phrase="characters")} of another 
string. Equivalently, two strings are anagrams when one is a {PERMUTATION.key.get_reference(phrase="permutation")} of 
the other and both strings have the same {MULTISET.key.get_reference(phrase="multiset")} of characters.

---

The strings `listen` and `silent` are anagrams: both contain exactly the same characters (one `s`, one `i`, one `l`, 
one `e`, one `n`, one `t`), and `silent` is a reordering of `listen`. The strings `hello` and `world` are not 
anagrams, since they contain different characters and therefore different multisets.
"""


ANAGRAM = _Anagram(
    key=DefinitionKey(
        name="anagram",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
