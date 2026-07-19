from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Index(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
An {INTEGER.key.get_reference()} value that identifies the position of an {ITEM.key.get_reference(phrase="element")}
within a {SEQUENCE.key.get_reference()}. Indices are used to access, modify, or reference specific
elements, and can be zero-based (starting at 0) or one-based (starting at 1) depending on the context.

---

Given the {SEQUENCE.key.get_reference()} ['a', 'b', 'c', 'd']:

  Zero-based indices: 0 → 'a',  1 → 'b',  2 → 'c',  3 → 'd'

  One-based  indices: 1 → 'a',  2 → 'b',  3 → 'c',  4 → 'd'

Using zero-based indexing, the element at index 2 is 'c'.
"""


INDEX = _Index(DefinitionKey(name="index", field=FieldName.MATHEMATICS))
