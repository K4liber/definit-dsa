from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.primitive_data_type import (
    PRIMITIVE_DATA_TYPE,
)
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER as MATH_INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Integer(Definition):
    def _get_content(self) -> str:
        return f"""
A {PRIMITIVE_DATA_TYPE.key.get_reference(phrase="primitive data type")} that represents whole 
{NUMBER.key.get_reference(phrase="numbers")}, i.e. {MATH_INTEGER.key.get_reference(phrase="integers")} stored in a 
fixed amount of memory. Integers can be positive, negative, or zero.

---

A signed 8-{BIT.key.get_reference(phrase="bit")} integer can store values from -128 to 127. The value 42 fits, while 200 does not, because it exceeds 
the range that 8 bits can hold.
"""


INTEGER = _Integer(
    key=DefinitionKey(
        name="integer",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
