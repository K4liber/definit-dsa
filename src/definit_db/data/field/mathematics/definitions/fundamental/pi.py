from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.irrational import IRRATIONAL
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Pi(Definition):
    def _get_content(self) -> str:
        return f"""
A mathematical constant (written π) equal to the ratio of a circle's circumference to its diameter. Its value
is approximately 3.14159, and it is an {IRRATIONAL.key.get_reference()} {NUMBER.key.get_reference(phrase="number")}: 
its decimal expansion never terminates or repeats.

---

For any circle, dividing the circumference by the diameter always gives the same {NUMBER.key.get_reference()}
π ≈ 3.14159, regardless of the circle's size. This invariance is what makes π a universal constant rather than
a property of any particular circle.
"""


PI = _Pi(
    key=DefinitionKey(
        name="pi",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["π"],
)
