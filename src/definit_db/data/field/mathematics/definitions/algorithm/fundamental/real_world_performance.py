from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _RealWorldPerformance(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} of an {ALGORITHM.key.get_reference()} refers to its actual execution 
efficiency in practical applications, as opposed to theoretical 
{COMPLEXITY.key.get_reference()} analysis. While {TIME_COMPLEXITY.key.get_reference("time complexity")} 
and {SPACE_COMPLEXITY.key.get_reference("space complexity")} provide 
{ASYMPTOTIC_BEHAVIOR.key.get_reference("asymptotic")} {BOUND.key.get_reference("bounds")} that describe 
how an algorithm scales, real-world performance considers the actual runtime behavior with typical 
{INPUT_DATA.key.get_reference("input data")} and implementation-specific factors. An algorithm with better 
theoretical complexity may perform worse in practice, and vice versa.
"""


REAL_WORLD_PERFORMANCE = _RealWorldPerformance(
    DefinitionKey(name="real-world performance", field=FieldName.MATHEMATICS)
)
