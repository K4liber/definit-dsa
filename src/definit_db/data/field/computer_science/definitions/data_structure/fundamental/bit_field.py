from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE


class _BitField(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {DATA_STRUCTURE.key.get_reference(phrase="data structure")} that consists of one or 
more adjacent {BIT.key.get_reference(phrase="bits")} which have been allocated for specific purposes, so that any 
single bit or group of bits within the structure can be set or inspected.

---

For example, a 3-bit field can store three independent permission flags - read, write, and 
execute - one per bit. Setting the read bit to 1 grants read access, clearing it to 0 revokes read access, 
and the same idea applies independently to the write and execute bits. Because each flag occupies its own bit, all 
three can be inspected or changed in a single operation without disturbing the others.
"""


BIT_FIELD = _BitField(
    key=DefinitionKey(
        name="bit_field",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
