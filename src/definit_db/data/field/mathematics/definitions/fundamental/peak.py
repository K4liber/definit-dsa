from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.adjacent import ADJACENT
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Peak(Definition):
    def _get_content(self) -> str:
        return f"""
A peak is an {ITEM.key.get_reference(phrase="element")} in a {SEQUENCE.key.get_reference(phrase="sequence")} 
whose value is greater than or equal to the values of its {ADJACENT.key.get_reference(phrase="adjacent")} elements. 
A peak is often identified by an {INDEX.key.get_reference(phrase="index")}; the first and last elements are 
compared only with the single neighbor that exists.

---

For the sequence (1, 3, 2, 4, 4, 1):

  index: 0  1  2  3  4  5
  value: 1  3  2  4  4  1

The element at index 1 (value 3) is a peak, since it is greater than or equal to both neighbors (1 and 2).
The elements at index 3 and index 4 (both value 4) are also peaks, since each is greater than or equal to its
neighbors, illustrating that equal adjacent values can both be peaks. The element at index 0 (value 1) is not a
peak because it is compared only to its single existing neighbor (3), which is greater. Likewise, the element at
index 5 (value 1) is not a peak.
"""


PEAK = _Peak(
    key=DefinitionKey(
        name="peak",
        field=FieldName.MATHEMATICS,
    )
)
