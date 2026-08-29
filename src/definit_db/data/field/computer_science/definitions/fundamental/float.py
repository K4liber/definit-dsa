from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_type import DATA_TYPE
from definit_db.data.field.computer_science.definitions.fundamental.mantissa import MANTISSA
from definit_db.data.field.mathematics.definitions.fundamental.pi import PI
from definit_db.data.field.mathematics.definitions.fundamental.real_number import REAL_NUMBER


class _Float(Definition):
    def _get_content(self) -> str:
        return f"""
A floating-point {DATA_TYPE.key.get_reference(phrase="data type")} used 
to represent an approximation of a {REAL_NUMBER.key.get_reference(phrase="real number")} with finite precision.

---

A float can hold common values such as 3.14 (an approximation of {PI.key.get_reference(phrase="pi")}) and 2.5, as well 
as very large magnitudes such as 6.022e23 and very small ones such as 1.6e-19, since it uses a sign bit, an exponent, 
and a {MANTISSA.key.get_reference(phrase="mantissa")} to encode the value.
"""


FLOAT = _Float(
    key=DefinitionKey(
        name="Float",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=("single precision", "single-precision float"),
)
