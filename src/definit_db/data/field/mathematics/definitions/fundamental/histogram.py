from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION


class _Histogram(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a chart that summarizes how values are 
{DISTRIBUTION.key.get_reference(phrase="distributed")} by grouping them into ranges (bins) and showing 
the frequency in each bin.

A histogram is often used to visualize a distribution.
"""


HISTOGRAM = _Histogram(
    key=DefinitionKey(
        name="histogram",
        field=FieldName.MATHEMATICS,
    )
)
