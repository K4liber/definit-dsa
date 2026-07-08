from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.abstract_data_type import (
    ABSTRACT_DATA_TYPE,
)
from definit_db.data.field.mathematics.definitions.fundamental.finite_set import FINITE_SET
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS


class _Set(Definition):
    def _get_content(self) -> str:
        return f"""
A set is an {ABSTRACT_DATA_TYPE.key.get_reference(phrase="abstract data type")} that can store 
{UNIQUENESS.key.get_reference(phrase="unique")} values, without any particular order. It is a computer 
implementation of the mathematical concept of a {FINITE_SET.key.get_reference(phrase="finite set")}. Unlike most 
other {COLLECTION.key.get_reference(phrase="collection")} types, rather than retrieving a specific element from a 
set, one typically tests a value for membership in a set.

---

For example, a set might store the registered usernames {{"alice", "bob", "carol"}}. Adding "alice" again has no 
effect, since a value can appear at most once. The main operation is testing whether a name belongs to the set: 
asking "is bob a member?" returns yes, while "is dan a member?" returns no.
"""


SET = _Set(
    key=DefinitionKey(
        name="set",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
