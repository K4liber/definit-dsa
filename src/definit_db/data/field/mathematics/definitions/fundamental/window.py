from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.boundary import BOUNDARY
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.subsequence import SUBSEQUENCE


class _Window(Definition):
    def _get_content(self) -> str:
        return f"""
A contiguous {SUBSEQUENCE.key.get_reference(phrase="subsequence")} of a 
{SEQUENCE.key.get_reference(phrase="sequence")} being examined as a unit. A window is defined by its two 
{BOUNDARY.key.get_reference(phrase="boundaries")} — a start and an end — and contains exactly the 
{ITEM.key.get_reference(phrase="items")} between them in their original order. The 
boundaries may be moved to shift the window across the sequence, changing which items it covers without 
rebuilding it from scratch.

---

On the sequence [4, 2, 7, 1, 9], a window of size 3 starting at the left covers [4, 2, 7]. Moving the start 
one step right and the end one step right shifts the window to cover [2, 7, 1], then [7, 1, 9]. At each step 
the window drops its leftmost item and picks up the next item on the right, so the contents are updated 
incrementally rather than re-examined from the beginning.
"""


WINDOW = _Window(
    key=DefinitionKey(
        name="window",
        field=FieldName.MATHEMATICS,
    )
)
