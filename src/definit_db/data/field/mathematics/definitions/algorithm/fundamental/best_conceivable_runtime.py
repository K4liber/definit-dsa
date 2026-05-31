from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _BestConceivableRuntime(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} (BCR) is the theoretical best {TIME_COMPLEXITY.key.get_reference("time complexity")} 
that any {ALGORITHM.key.get_reference()} could possibly achieve for solving a particular {PROBLEM.key.get_reference()}. 
It represents a lower {BOUND.key.get_reference()} on the runtime based on the fundamental {CONSTRAINT.key.get_reference("constraints")} of the problem, 
such as the amount of {INPUT_DATA.key.get_reference("input")} that must be examined or the output that must be produced. The BCR helps identify whether 
an algorithm can be further optimized or if it has already achieved the best possible performance.
"""


BEST_CONCEIVABLE_RUNTIME = _BestConceivableRuntime(
    DefinitionKey(name="best conceivable runtime", field=FieldName.MATHEMATICS)
)
