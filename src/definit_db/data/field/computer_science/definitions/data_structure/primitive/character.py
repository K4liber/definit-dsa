from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.primitive_data_type import (
    PRIMITIVE_DATA_TYPE,
)
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _Character(Definition):
    def _get_content(self) -> str:
        return f"""
A {PRIMITIVE_DATA_TYPE.key.get_reference(phrase="primitive data type")} that represents 
a single textual symbol, such as a letter, digit, or punctuation mark. It is the atomic unit of 
{INFORMATION.key.get_reference(phrase="information")} from which text is composed.

---

The symbols `A`, `7`, and `?` are each a single character. A piece of text such as `Hello` is built from five 
characters taken together, and each one can be inspected, compared, or replaced independently of the others.
"""


CHARACTER = _Character(
    key=DefinitionKey(
        name="character",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=("char",),
)
