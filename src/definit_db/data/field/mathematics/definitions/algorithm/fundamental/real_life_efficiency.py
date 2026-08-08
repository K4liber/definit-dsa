from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_world_performance import (
    REAL_WORLD_PERFORMANCE,
)
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _RealLifeEfficiency(Definition):
    def _get_content(self) -> str:
        return f"""
real-life efficiency is {EFFICIENCY.key.get_reference("efficiency")} as observed in practice.

It is closely related to {REAL_WORLD_PERFORMANCE.key.get_reference("real-world performance")}, 
and depends on factors such as the {ALGORITHM.key.get_reference("implementation")}, constant factors, and typical 
{INPUT_DATA.key.get_reference("inputs")}.

---

Two {ALGORITHM.key.get_reference("implementations")} of the same {ALGORITHM.key.get_reference()} both run in
{BIG_O_NOTATION.key.get_reference("O(n)")}, but their
real-life {EFFICIENCY.key.get_reference("efficiency")} differs significantly:

Implementation A: {COMPUTATION.key.get_reference("processes")} each {ITEM.key.get_reference("element")} 
in-place, using 2 {OPERATION.key.get_reference("operations")} per element.

  Implementation B: same logic, but copies the entire {INPUT_DATA.key.get_reference("input")}
into a new {INPUT_DATA.key.get_reference("buffer")} first, adding n extra
{OPERATION.key.get_reference("operations")} of
{EFFICIENCY.key.get_reference("overhead")}.


For n = 1 000 000:

A: ~2 000 000 {OPERATION.key.get_reference("operations")} -> fast in practice

B: ~2 000 000 {OPERATION.key.get_reference("operations")} + 1 000 000 copy -> 50% slower in practice


Both are {BIG_O_NOTATION.key.get_reference("O(n)")} — identical theoretical complexity — but implementation B
has worse real-life {EFFICIENCY.key.get_reference()} due to a constant-factor
{EFFICIENCY.key.get_reference("overhead")} that theory ignores.
"""


REAL_LIFE_EFFICIENCY = _RealLifeEfficiency(
    key=DefinitionKey(
        name="real-life efficiency",
        field=FieldName.MATHEMATICS,
    )
)
