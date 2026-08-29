from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.performance import PERFORMANCE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _RealWorldPerformance(Definition):
    def _get_content(self) -> str:
        return f"""
The real-world {PERFORMANCE.key.get_reference()} of an {ALGORITHM.key.get_reference()} refers to its actual execution 
{EFFICIENCY.key.get_reference()} in practical applications, as opposed to theoretical 
{COMPLEXITY.key.get_reference()} analysis. While {TIME_COMPLEXITY.key.get_reference("time complexity")} 
and {SPACE_COMPLEXITY.key.get_reference("space complexity")} provide 
{ASYMPTOTIC_BEHAVIOR.key.get_reference("asymptotic")} {BOUND.key.get_reference("bounds")} that describe 
how an algorithm scales, real-world performance considers the actual runtime behavior with typical 
{INPUT_DATA.key.get_reference("input data")} and implementation-specific factors. An algorithm with better 
theoretical complexity may perform worse in practice, and vice versa.

---

Consider two algorithms solving the same {PROBLEM.key.get_reference()}:


Algorithm A: 100·n   operations  — O(n),  but a large constant factor of 100

Algorithm B:    n²   operations  — O(n²), constant factor of 1


Theoretical {COMPLEXITY.key.get_reference()} says A is asymptotically better. Yet for small
{INPUT_DATA.key.get_reference("inputs")} A is actually slower:


n =  5: A = 500 ops, B = 25 ops → B wins

n = 50: A = 5 000 ops, B = 2 500 ops → B wins

n = 100: A = 10 000 ops, B = 10 000 ops → tie

n = 200: A = 20 000 ops, B = 40 000 ops → A wins

For real-world workloads where n is usually small, the {ALGORITHM.key.get_reference()} with the
worse theoretical {COMPLEXITY.key.get_reference()} can be the better practical choice.
"""


REAL_WORLD_PERFORMANCE = _RealWorldPerformance(
    DefinitionKey(name="real-world performance", field=FieldName.MATHEMATICS)
)
