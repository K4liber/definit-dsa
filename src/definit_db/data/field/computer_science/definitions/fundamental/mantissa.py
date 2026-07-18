from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Mantissa(Definition):
    def _get_content(self) -> str:
        return f"""
Mantissa (also called significand) is the part of a floating-point 
{NUMBER.key.get_reference(phrase="number")} that holds its significant digits, determining the precision of the 
value. Together with a sign and an exponent, the mantissa encodes the full number: the exponent sets the scale 
(magnitude) while the mantissa sets the significant digits that are kept.

---

In the scientific notation value 6.022 x 10^23, the mantissa is 6.022 and the exponent is 23. Because a fixed 
{BIT.key.get_reference(phrase="number of bits")} is allocated to the mantissa, only a limited count of significant 
digits can be stored; any digits beyond that are rounded away.
"""


MANTISSA = _Mantissa(
    key=DefinitionKey(
        name="mantissa",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
