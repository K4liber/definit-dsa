from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Median(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} of a {SEQUENCE.key.get_reference()} of values is the middle value when the values
are ordered.

If there is an even number of values, the median is typically taken to be the average of the two middle values.
"""


MEDIAN = _Median(
    key=DefinitionKey(
        name="median",
        field=FieldName.MATHEMATICS,
    )
)
