from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.boundary import BOUNDARY
from definit_db.data.field.mathematics.definitions.fundamental.real_number import REAL_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Interval(Definition):
    def _get_content(self) -> str:
        return f"""
An interval is a {SET.key.get_reference(phrase="set")} of {REAL_NUMBER.key.get_reference(phrase="real numbers")} 
between two endpoints. The endpoints act as {BOUNDARY.key.get_reference(phrase="boundaries")}, and each endpoint may be 
included in or excluded from the interval.

---

The interval [2, 5] is the {SET.key.get_reference(phrase="set")} of 
{REAL_NUMBER.key.get_reference(phrase="real numbers")} from 2 to 5, including both endpoints.
The interval (2, 5) is the same {SET.key.get_reference(phrase="set")}, except the endpoints 2 and 5 are excluded.
"""


INTERVAL = _Interval(
    key=DefinitionKey(
        name="interval",
        field=FieldName.MATHEMATICS,
    )
)
