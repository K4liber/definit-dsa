from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.bit_field import BIT_FIELD
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.primitive_data_type import (
    PRIMITIVE_DATA_TYPE,
)
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _Boolean(Definition):
    def _get_content(self) -> str:
        return f"""
Boolean (sometimes shortened to Bool) is a {PRIMITIVE_DATA_TYPE.key.get_reference(phrase="primitive data type")} 
that has one of two possible values usually denoted true and false. Boolean is a 
{BIT_FIELD.key.get_reference(phrase="bit field")} that stores a single {BIT.key.get_reference(phrase="bit")} of 
{INFORMATION.key.get_reference(phrase="information")}.

---

A boolean can represent whether a light is on (true) or off (false). Since there are only two possibilities, a 
single bit suffices to distinguish them.
"""


BOOLEAN = _Boolean(
    key=DefinitionKey(
        name="boolean",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
