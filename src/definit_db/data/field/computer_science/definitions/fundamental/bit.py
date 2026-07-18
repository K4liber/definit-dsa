from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _Bit(Definition):
    def _get_content(self) -> str:
        return f"""
The bit (binary digit) is the smallest unit of data in computing, representing a binary state of 
either 0 or 1. Bits are the fundamental building blocks of {DATA.key.get_reference(phrase="data")} and can convey basic 
forms of {INFORMATION.key.get_reference(phrase="information")} by representing true/false or on/off states.

---

The sequence 1011 consists of four bits — 1, 0, 1, and 1 — each representing a binary state that can convey
one basic unit of information, such as on or off.
"""


BIT = _Bit(
    key=DefinitionKey(
        name="bit",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
