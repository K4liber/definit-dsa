from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.algorithms.two_pointers_technique import TWO_POINTERS_TECHNIQUE
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.array import ARRAY
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.subarray import SUBARRAY
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.substring import SUBSTRING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _SlidingWindowTechnique(Definition):
    def _get_content(self) -> str:
        return f"""
The sliding window technique is an {ALGORITHM.key.get_reference(phrase="algorithmic")} pattern for 
processing a {SEQUENCE.key.get_reference(phrase="sequence")} by maintaining a contiguous window, often a 
{SUBARRAY.key.get_reference(phrase="subarray")} or {SUBSTRING.key.get_reference(phrase="substring")}, and moving 
its boundaries as the computation proceeds. It is commonly implemented as a specialized 
{TWO_POINTERS_TECHNIQUE.key.get_reference(phrase="two pointers technique")}: one boundary expands the window 
to include new elements, while the other boundary contracts it when the current window no longer satisfies a 
required condition.

---

To find the largest sum of any length-3 {SUBARRAY.key.get_reference(phrase="subarray")} in the
{ARRAY.key.get_reference(phrase="array")} [2, 1, 5, 1, 3, 2], a window of size 3 slides one position at a time:
- window [2, 1, 5]: sum = 8
- window [1, 5, 1]: sum = 7
- window [5, 1, 3]: sum = 9
- window [1, 3, 2]: sum = 6
The maximum sum is 9, from the subarray [5, 1, 3]. At each step the window drops its leftmost value and adds the
next value on the right, so each sum is updated from the previous one instead of recomputed.
"""


SLIDING_WINDOW_TECHNIQUE = _SlidingWindowTechnique(
    key=DefinitionKey(
        name="sliding window technique",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
