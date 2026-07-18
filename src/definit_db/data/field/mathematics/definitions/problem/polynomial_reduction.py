from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.reduction import REDUCTION


class _PolynomialReduction(Definition):
    def _get_content(self) -> str:
        return f"""
A polynomial reduction (also called a many-one reduction or Karp reduction) is a type of 
{REDUCTION.key.get_reference()} used in computational complexity theory. {PROBLEM.key.get_reference()} A 
is polynomially reducible to {PROBLEM.key.get_reference()} B if there exists a 
{POLYNOMIAL.key.get_reference("polynomial")}-{TIME_COMPLEXITY.key.get_reference("time")} computable 
function that transforms any instance of A into an equivalent instance of B — meaning A's answer is "yes" 
if and only if the transformed B instance's answer is "yes". This is written A ≤ₚ B and is interpreted as 
"A is no harder than B": an efficient solver for B can be used to solve A via the transformation.

---

Suppose we want to show that {PROBLEM.key.get_reference()} A reduces to {PROBLEM.key.get_reference()} B:

  Instance of A  →  (poly-time transformation f)  →  Instance of B
                                                             ↓
                                                        Solve B
                                                             ↓
  Answer for A  ←  (same yes/no answer)  ←  Answer for B

If f runs in {POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")} and
preserves the yes/no answer, then A ≤ₚ B. This means B is at least as hard as A: if B were
efficiently solvable, A would be too (apply f first, then solve B).
"""


POLYNOMIAL_REDUCTION = _PolynomialReduction(
    key=DefinitionKey(
        name="polynomial reduction",
        field=FieldName.MATHEMATICS,
    )
)
