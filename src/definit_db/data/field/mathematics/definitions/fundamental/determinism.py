from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _Determinism(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
Determinism is the property of a {FUNCTION.key.get_reference()} or process whereby its output is fully 
determined by its {INPUT_DATA.key.get_reference("input")}: given the same input, it always produces the same 
result, with no variation between calls.

---

The function f(x) = x + 1 has determinism: every call with the input 3 returns 4. A function that returns the 
current time lacks determinism, because the same input (no input at all) yields a different result on each call.
"""


DETERMINISM = _Determinism(DefinitionKey(name="determinism", field=FieldName.MATHEMATICS))
