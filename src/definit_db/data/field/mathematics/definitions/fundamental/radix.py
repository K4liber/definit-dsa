from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.distinctness import DISTINCTNESS
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Radix(Definition):
    def _get_content(self) -> str:
        return f"""
A radix is the base of a positional {NUMBER.key.get_reference("number")} system. It is the count of
{DISTINCTNESS.key.get_reference(phrase="distinct")} digits, including zero, used to represent numbers in that
system.

---

Radix 10 (decimal): digits 0–9. The {NUMBER.key.get_reference("number")} 42 means 4×10 + 2.

Radix 2  (binary):  digits 0–1. The {NUMBER.key.get_reference("number")} 101 means 1×4 + 0×2 + 1 = 5.

Radix 16 (hexadecimal): digits 0–9 and A–F. The {NUMBER.key.get_reference("number")} 1F means 1×16 + 15 = 31.
"""


RADIX = _Radix(
    key=DefinitionKey(
        name="radix",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["base"],
)
