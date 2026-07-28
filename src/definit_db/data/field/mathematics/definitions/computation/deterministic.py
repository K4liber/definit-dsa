from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _Deterministic(Definition):
    def _get_content(self) -> str:
        return f"""
A property of a {COMPUTATION.key.get_reference()} or system: given the same
{INPUT_DATA.key.get_reference("input")}, a deterministic process always produces the same output by following the
same sequence of steps, with no randomness or arbitrary choice involved.

---

A function that adds 2 to its {INPUT_DATA.key.get_reference("input")} is deterministic: feeding in 3 always
yields 5, never 4 or 6. Running it a thousand times on the same value never changes the result, because every
step of the {COMPUTATION.key.get_reference()} is fixed in advance.
"""


DETERMINISTIC = _Deterministic(
    key=DefinitionKey(
        name="deterministic",
        field=FieldName.MATHEMATICS,
    )
)
