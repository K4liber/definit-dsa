from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Data(Definition):
    def _get_content(self) -> str:
        return f"""
A collection of discrete or continuous values that convey {INFORMATION.key.get_reference(phrase="information")}, 
describing quantities, qualities, facts, or simply {SEQUENCE.key.get_reference(phrase="sequences")} of symbols that may 
be further interpreted formally.

---

The {NUMBER.key.get_reference(phrase="numbers")} (72, 85, 90) are data representing three exam scores. On their own they are just values, but when
interpreted as "scores out of 100", they convey information about how well a group of students performed.
"""


DATA = _Data(
    key=DefinitionKey(
        name="data",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
