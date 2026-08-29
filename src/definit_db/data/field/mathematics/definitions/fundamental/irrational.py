from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.real_number import REAL_NUMBER


class _Irrational(Definition):
    def _get_content(self) -> str:
        return f"""
An {REAL_NUMBER.key.get_reference(phrase="real number")} that cannot be written as a ratio of two 
{INTEGER.key.get_reference(phrase="integers")}. Equivalently, it is a {NUMBER.key.get_reference(phrase="number")} 
whose decimal expansion never terminates and never falls into a repeating pattern.

---

√2 ≈ 1.41421356... is irrational: its decimal expansion continues forever with no repeating block, and no
fraction of two integers exactly equals it. By contrast, 0.5 = 1/2 and 0.333... = 1/3 are not irrational,
since each can be written as a ratio of integers.
"""


IRRATIONAL = _Irrational(
    key=DefinitionKey(
        name="irrational",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["irrational number"],
)
