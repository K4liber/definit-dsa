from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_world_performance import (
    REAL_WORLD_PERFORMANCE,
)
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _RealLifeEfficiency(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is {EFFICIENCY.key.get_reference("efficiency")} as observed in practice.

It is closely related to {REAL_WORLD_PERFORMANCE.key.get_reference("real-world performance")}, 
and depends on factors such as the implementation, constant factors, and typical 
{INPUT_DATA.key.get_reference("inputs")}.

---

Two implementations of the same {ALGORITHM.key.get_reference()} both run in O(n), but their
real-life {EFFICIENCY.key.get_reference("efficiency")} differs significantly:

  Implementation A: processes each element in-place using 2 operations per element.
  Implementation B: same logic, but copies the entire {INPUT_DATA.key.get_reference("input")}
                    into a new buffer first, adding n extra operations of overhead.

For n = 1 000 000:
  A: ~2 000 000 operations                  → fast in practice
  B: ~2 000 000 operations + 1 000 000 copy → 50% slower in practice

Both are O(n) — identical theoretical complexity — but implementation B has worse real-life
efficiency due to a constant-factor overhead that theory ignores.
"""


REAL_LIFE_EFFICIENCY = _RealLifeEfficiency(
    key=DefinitionKey(
        name="real-life efficiency",
        field=FieldName.MATHEMATICS,
    )
)
