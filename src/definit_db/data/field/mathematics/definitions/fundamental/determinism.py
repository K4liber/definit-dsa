from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _Determinism(Definition):
    def _get_content(self) -> str:
        return f"""
Determinism is the property of a {FUNCTION.key.get_reference()} or process whereby its output is fully 
determined by its {INPUT_DATA.key.get_reference("input")}: given the same input, it always produces the same 
result by following the same sequence of steps, with no randomness, arbitrary choice, or variation between 
calls.

---

The function f(x) = x + 1 has determinism: every call with the input 3 returns 4. A function g(x) that returns
x plus a random number lacks determinism: calling g(3) might return 4 on one call and 7 on the next, because the
output depends on more than just the input.
"""


DETERMINISM = _Determinism(DefinitionKey(name="determinism", field=FieldName.MATHEMATICS))
