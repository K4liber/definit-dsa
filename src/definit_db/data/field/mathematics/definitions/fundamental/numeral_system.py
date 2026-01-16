from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.radix import RADIX


class _NumeralSystem(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a method for representing {NUMBER.key.get_reference("numbers")} 
using a set of symbols and rules.
"""


NUMERAL_SYSTEM = _NumeralSystem(
    key=DefinitionKey(
        name="numeral system",
        field=FieldName.MATHEMATICS,
    )
)
