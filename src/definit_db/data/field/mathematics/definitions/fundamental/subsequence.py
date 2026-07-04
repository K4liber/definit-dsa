from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Subsequence(Definition):
    def _get_content(self) -> str:
        return f"""
A {SEQUENCE.key.get_reference(phrase="sequence")} derived from another sequence by deleting zero or 
more {ITEM.key.get_reference(phrase="items")} without changing the relative order of the remaining 
items. Formally, a sequence (b_0, b_1, ..., b_{{k-1}}) is a subsequence of (a_0, a_1, ..., a_{{n-1}}) 
if there exist {INDEX.key.get_reference(phrase="indices")} 0 <= i_0 < i_1 < ... < i_{{k-1}} <= n-1 
such that b_j = a_{{i_j}} for every j. The selected items need not be contiguous in the original 
sequence.

---

The sequence (1, 3, 5) is a subsequence of (1, 2, 3, 4, 5): selecting indices 0, 2, 4 (values 1, 3, 5)
preserves their relative order even though the selected items are not contiguous in the original sequence.

The sequence (3, 1) is not a subsequence of (1, 2, 3, 4, 5), since no choice of increasing indices produces
the values 3 followed by 1.
"""


SUBSEQUENCE = _Subsequence(
    key=DefinitionKey(
        name="subsequence",
        field=FieldName.MATHEMATICS,
    )
)
