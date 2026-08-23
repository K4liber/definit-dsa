from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.data_type import DATA_TYPE
from definit_db.data.field.computer_science.definitions.fundamental.float import FLOAT
from definit_db.data.field.computer_science.definitions.fundamental.mantissa import MANTISSA
from definit_db.data.field.mathematics.definitions.fundamental.real_number import REAL_NUMBER


class _Double(Definition):
    def _get_content(self) -> str:
        return f"""
Double (short for double precision) is a floating-point
{DATA_TYPE.key.get_reference(phrase="data type")} used to represent an approximation of a
{REAL_NUMBER.key.get_reference(phrase="real number")} with finite precision. In many systems, a double provides
about twice the precision of a {FLOAT.key.get_reference(phrase="float")} because it allocates more
{BIT.key.get_reference(phrase="bits")} to its {MANTISSA.key.get_reference(phrase="mantissa")} and exponent.

---

A 32-bit single-precision float typically keeps about 7 significant decimal digits, while a 64-bit double keeps
about 15-16. For example, the constant pi (approximately 3.14159265358979) can be stored more accurately in a
double than in a float, because its larger mantissa retains more significant bits.
"""


DOUBLE = _Double(
    key=DefinitionKey(
        name="Double",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=("double precision", "double-precision float"),
)
