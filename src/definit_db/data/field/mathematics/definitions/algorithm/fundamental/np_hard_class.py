from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity_theory import COMPLEXITY_THEORY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_class import NP_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.p_class import P_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.problem.polynomial_reduction import POLYNOMIAL_REDUCTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _NPHardClass(Definition):
    def _get_content(self) -> str:
        return f"""
A class of {PROBLEM.key.get_reference("problems")} in {COMPUTATION.key.get_reference("computational")}
{COMPLEXITY_THEORY.key.get_reference("complexity theory")} that are at least as hard as the hardest problems in
{NP_CLASS.key.get_reference("NP")}.
A problem is NP-Hard if every problem in NP can be {POLYNOMIAL_REDUCTION.key.get_reference("reduced")} to it in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")}. This means that 
if we had an {ALGORITHM.key.get_reference()} to {SOLUTION.key.get_reference("solve")} an NP-Hard problem
{EFFICIENCY.key.get_reference("efficiently")}, we could use it to {SOLUTION.key.get_reference("solve")} 
all NP problems {EFFICIENCY.key.get_reference("efficiently")}. 
NP-Hard problems are not necessarily in NP themselves - they may be even
harder, with no way to verify {SOLUTION.key.get_reference("solutions")} quickly. 
The {POLYNOMIAL_REDUCTION.key.get_reference()} is used as a
theoretical tool to prove hardness, not to {SOLUTION.key.get_reference("solve")} problems. The size of the
{INPUT_DATA.key.get_reference()} determines the complexity of {SOLUTION.key.get_reference("solving")} 
NP-Hard problems.

---

Suppose {PROBLEM.key.get_reference()} H is NP-Hard. This means every {PROBLEM.key.get_reference()} in
{NP_CLASS.key.get_reference("NP")} can be {POLYNOMIAL_REDUCTION.key.get_reference("reduced")} to H in
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")}:

Every NP problem → (poly-time reduction) → H

In practice, proving H is NP-Hard does not require constructing a separate reduction from each NP
{PROBLEM.key.get_reference()}. Because {POLYNOMIAL_REDUCTION.key.get_reference("reductions")} are transitive, it
suffices to reduce a single already-known NP-Hard {PROBLEM.key.get_reference()} to H:

Known NP-Hard problem → (poly-time reduction) → H

↑

All of NP already reduces to this

NP-hardness does not prove that an {EFFICIENCY.key.get_reference("efficient")}
{ALGORITHM.key.get_reference()} for H cannot exist. If one did exist, every {PROBLEM.key.get_reference()} in
{NP_CLASS.key.get_reference("NP")} could be {POLYNOMIAL_REDUCTION.key.get_reference("reduced")} to H in
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")} and then
{SOLUTION.key.get_reference("solved")} by that algorithm. Every problem in NP would therefore also be in
{P_CLASS.key.get_reference("P")}, implying P = NP. Whether P equals NP remains an open question.

This consequence makes such an algorithm important, not logically impossible. H also does not need to be in NP:
NP-hardness does not require H's own {SOLUTION.key.get_reference("solutions")} 
to be verifiable in polynomial time.
"""


NP_HARD_CLASS = _NPHardClass(
    DefinitionKey(name="NP-Hard class", field=FieldName.MATHEMATICS),
    aliases=["NP-Hard"],
)
