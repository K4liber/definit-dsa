from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.binary_fractions import BINARY_FRACTIONS
from definit_db.data.field.computer_science.definitions.fundamental.float import FLOAT
from definit_db.data.field.mathematics.definitions.fundamental.real_number import REAL_NUMBER


class _FloatingPointPrecision(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Floating-point precision")} is the limited accuracy with which a 
{FLOAT.key.get_reference(phrase="float")} can represent a 
{REAL_NUMBER.key.get_reference(phrase="real number")}, which causes rounding errors in computations.

Many decimal fractions have no exact finite representation as 
{BINARY_FRACTIONS.key.get_reference(phrase="binary fractions")}. For example, the decimal value 0.1 is a repeating
fraction in binary (0.0001100110011...), so it cannot be stored exactly and is instead held as the nearest
representable approximation.

---

Because 0.1 is stored approximately, adding it to itself three times does not produce exactly 0.3:
0.1 + 0.1 + 0.1 = 0.30000000000000004. In contrast, values such as 0.5 and 0.25 are stored exactly, because they
are negative powers of two (2^-1 and 2^-2).
"""


FLOATING_POINT_PRECISION = _FloatingPointPrecision(
    key=DefinitionKey(
        name="floating-point precision",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
