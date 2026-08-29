from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Exponential(Definition):
    def _get_content(self) -> str:
        return f"""
Growth or scaling where each step multiplies a quantity by the same {NUMBER.key.get_reference()}. A value is
exponential when it follows a pattern such as 2^n, 3^n, or more generally a*b^n.

---

The sequence 1, 2, 4, 8, 16 is exponential because each term is obtained by multiplying the previous one by the
same {NUMBER.key.get_reference()}: 2.
"""


EXPONENTIAL = _Exponential(
    key=DefinitionKey(
        name="exponential",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("exponential growth",),
)
