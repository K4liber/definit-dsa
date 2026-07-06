from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _Map(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {DATA_STRUCTURE.key.get_reference(phrase="data structure")} that associates each key 
{ITEM.key.get_reference(phrase="item")} with at most one value item. It models the mathematical 
{FUNCTION.key.get_reference(phrase="function")} abstraction, where the set of keys forms the function's domain and 
each key maps to exactly one value.

---

For example, a map from student names to exam scores might contain the pairs ("Alice", 92), ("Bob", 85), and 
("Carol", 78). Looking up the key "Alice" returns the value 92; looking up a key that is not present (such as "Dan") 
returns nothing. Assigning "Alice" a second time replaces 92 with the new value, which is what keeps the "at most one 
value per key" rule intact.
"""


MAP = _Map(
    key=DefinitionKey(
        name="map",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
