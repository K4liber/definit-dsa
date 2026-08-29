from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.real_number import REAL_NUMBER


class _ScientificNotation(Definition):
    def _get_content(self) -> str:
        return f"""
A way of writing a {REAL_NUMBER.key.get_reference(phrase="real number")} as the product of a coefficient and a 
power of ten: a × 10^n, where the coefficient a satisfies 1 ≤ |a| < 10 and the exponent n is an 
{INTEGER.key.get_reference(phrase="integer")}. The exponent sets the magnitude of the 
{NUMBER.key.get_reference(phrase="number")}, while the coefficient carries its significant digits.

---

The number 602200000000000000000000 is written in scientific notation as 6.022 × 10^23:
the coefficient is 6.022 (significant digits) and the exponent 23 sets the magnitude.
Likewise, 0.00032 is written as 3.2 × 10^-4, where the negative exponent indicates a small magnitude.
"""


SCIENTIFIC_NOTATION = _ScientificNotation(
    key=DefinitionKey(
        name="scientific notation",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["standard form"],
)
