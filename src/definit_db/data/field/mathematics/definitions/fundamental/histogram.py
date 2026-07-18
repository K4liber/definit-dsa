from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION


class _Histogram(Definition):
    def _get_content(self) -> str:
        return f"""
A chart that summarizes how values are 
{DISTRIBUTION.key.get_reference(phrase="distributed")} by grouping them into ranges (bins) and showing 
the frequency in each bin.

---

Given the values (72, 85, 90, 63, 77, 95, 81, 68, 74, 89), grouping them into bins of width 10 produces:

  60-69: 2   (63, 68)
  70-79: 3   (72, 74, 77)
  80-89: 3   (81, 85, 89)
  90-99: 2   (90, 95)

This histogram shows that most values are concentrated in the 70-89 range.
"""


HISTOGRAM = _Histogram(
    key=DefinitionKey(
        name="histogram",
        field=FieldName.MATHEMATICS,
    )
)
