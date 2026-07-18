from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.radix import RADIX


class _NumeralSystem(Definition):
    def _get_content(self) -> str:
        return f"""
A method for representing {NUMBER.key.get_reference("numbers")}
using a set of symbols and rules. Positional numeral systems are characterized by their
{RADIX.key.get_reference("radix")} — the count of distinct symbols available.

---

Decimal is a numeral system with {RADIX.key.get_reference("radix")} 10: it uses
symbols 0–9 and each position represents a power of 10.

Binary is a numeral system with {RADIX.key.get_reference("radix")} 2: it uses only
0 and 1. The {NUMBER.key.get_reference("number")} ten is written as 1010.
"""


NUMERAL_SYSTEM = _NumeralSystem(
    key=DefinitionKey(
        name="numeral system",
        field=FieldName.MATHEMATICS,
    )
)
