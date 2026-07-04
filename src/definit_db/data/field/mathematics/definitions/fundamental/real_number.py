from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _RealNumber(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Real number")} is a {NUMBER.key.get_reference(phrase="number")} that can represent a
quantity on the continuous number line.

---

3, -7, and 0 are real numbers — each is also an {INTEGER.key.get_reference(phrase="integer")}.
0.5 and π (≈ 3.14159) are real numbers too, even though neither is an {INTEGER.key.get_reference(phrase="integer")}.
"""


REAL_NUMBER = _RealNumber(
    key=DefinitionKey(
        name="Real number",
        field=FieldName.MATHEMATICS,
    )
)
