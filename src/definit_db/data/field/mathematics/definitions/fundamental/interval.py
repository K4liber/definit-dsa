from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.real_number import REAL_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Interval(Definition):
    def _get_content(self) -> str:
        return f"""
An interval is a {SET.key.get_reference(phrase="set")} of {REAL_NUMBER.key.get_reference(phrase="real numbers")} 
between two endpoints. The endpoints act as {BOUND.key.get_reference(phrase="bounds")}, and each endpoint may be 
included in or excluded from the interval.
"""


INTERVAL = _Interval(
    key=DefinitionKey(
        name="interval",
        field=FieldName.MATHEMATICS,
    )
)
