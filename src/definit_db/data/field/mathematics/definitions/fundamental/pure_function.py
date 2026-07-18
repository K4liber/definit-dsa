from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _PureFunction(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {FUNCTION.key.get_reference()} that always returns the same result 
for the same {INPUT_DATA.key.get_reference("input")}. 
Pure functions are deterministic and depend only on their input values to produce their output values.

---

f(x) = x + 1 is a pure function: calling it with the {NUMBER.key.get_reference(phrase="number")} 3 always 
returns 4. A function that returns the current time is not pure, because its output changes between calls.
"""


PURE_FUNCTION = _PureFunction(DefinitionKey(name="pure function", field=FieldName.MATHEMATICS))
