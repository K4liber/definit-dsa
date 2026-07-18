from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subset_sum import SUBSET_SUM


class _Optimization(Definition):
    def _get_content(self) -> str:
        return f"""
The process of improving an {ALGORITHM.key.get_reference()} or {SOLUTION.key.get_reference()} to make it more 
efficient by reducing resource consumption. optimization 
involves finding the best approach to solve a {PROBLEM.key.get_reference()} within given 
{CONSTRAINT.key.get_reference("constraints")}, often by minimizing costs or maximizing benefits.

---

A first {SOLUTION.key.get_reference()} to the {SUBSET_SUM.key.get_reference()} {PROBLEM.key.get_reference()} checks 
every possible subset before answering. Optimizing this solution to stop as soon as a 
subset satisfying the target-sum {CONSTRAINT.key.get_reference()} is found avoids examining the remaining subsets, 
reducing the work performed.
"""


OPTIMIZATION = _Optimization(
    key=DefinitionKey(
        name="optimization",
        field=FieldName.MATHEMATICS,
    )
)
