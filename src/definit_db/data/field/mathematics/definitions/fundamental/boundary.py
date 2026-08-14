from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Boundary(Definition):
    def _get_content(self) -> str:
        return f"""
A {BOUND.key.get_reference()} that marks an endpoint of a range, region, or {SET.key.get_reference()} of allowed values.
Boundaries delimit where a range begins and ends, separating values inside it from those outside it.

---

For the integer range 0 through 4, the boundaries are 0 and 4: any value inside this range is valid, while a
value outside it (such as -1 or 5) crosses a boundary and lies out of range.
"""


BOUNDARY = _Boundary(
    key=DefinitionKey(
        name="boundary",
        field=FieldName.MATHEMATICS,
    )
)
