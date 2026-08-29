from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Median(Definition):
    def _get_content(self) -> str:
        return f"""
The median of a {SEQUENCE.key.get_reference()} of {NUMBER.key.get_reference(phrase="values")}
is the middle value when the values are ordered.

If there is an even number of values, the median is typically taken to be the average of the two middle values.

---

For the sequence (3, 1, 2), ordering the values gives (1, 2, 3), so the median is 2.

For the sequence (3, 1, 4, 2), ordering the values gives (1, 2, 3, 4). Since there is an even number of values,
the median is the average of the two middle values, 2 and 3, which is 2.5.
"""


MEDIAN = _Median(
    key=DefinitionKey(
        name="median",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["middle value"],
)
