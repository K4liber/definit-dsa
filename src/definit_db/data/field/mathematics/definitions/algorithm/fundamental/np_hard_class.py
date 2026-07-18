from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_class import NP_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.problem.polynomial_reduction import POLYNOMIAL_REDUCTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _NPHardClass(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A class of {PROBLEM.key.get_reference("problems")} in computational 
complexity theory that are at least as hard as the hardest problems in {NP_CLASS.key.get_reference("NP")}. 
A problem is NP-Hard if every problem in NP can be {POLYNOMIAL_REDUCTION.key.get_reference("reduced")} to it in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")}. This means that 
if we had an {ALGORITHM.key.get_reference()} to solve an NP-Hard problem efficiently, we could use it to 
solve all NP problems efficiently. NP-Hard problems are not necessarily in NP themselves - they may be even 
harder, with no way to verify solutions quickly. The {POLYNOMIAL_REDUCTION.key.get_reference()} is used as a 
theoretical tool to prove hardness, not to solve problems. The size of the {INPUT_DATA.key.get_reference()} 
determines the complexity of solving NP-Hard problems.

---

Suppose {PROBLEM.key.get_reference()} H is NP-Hard. This means every {PROBLEM.key.get_reference()} in
{NP_CLASS.key.get_reference("NP")} can be {POLYNOMIAL_REDUCTION.key.get_reference("reduced")} to H in
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")}:

  Every NP problem  →  (poly-time reduction)  →  H

In practice, proving H is NP-Hard does not require constructing a separate reduction from each NP
{PROBLEM.key.get_reference()}. Because {POLYNOMIAL_REDUCTION.key.get_reference("reductions")} are transitive, it
suffices to reduce a single already-known NP-Hard {PROBLEM.key.get_reference()} to H:

  Known NP-Hard problem  →  (poly-time reduction)  →  H
  ↑
  All of NP already reduces to this

If an efficient {ALGORITHM.key.get_reference()} for H existed, it could be used (via the chain of
reductions) to solve every NP {PROBLEM.key.get_reference()} efficiently. H is therefore at least as
hard as the hardest problems in NP — even if H's own {SOLUTION.key.get_reference("solutions")} cannot
be verified quickly, which means H does not need to be in NP itself.
"""


NP_HARD_CLASS = _NPHardClass(DefinitionKey(name="NP-Hard class", field=FieldName.MATHEMATICS))
