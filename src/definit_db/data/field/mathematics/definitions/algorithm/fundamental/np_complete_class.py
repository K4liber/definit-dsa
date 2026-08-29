from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_class import NP_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_hard_class import NP_HARD_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.computation.deterministic_turing_machine import (
    DETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.problem.polynomial_reduction import POLYNOMIAL_REDUCTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subset_sum import SUBSET_SUM


class _NPCompleteClass(Definition):
    def _get_content(self) -> str:
        return f"""
A class of {PROBLEM.key.get_reference("problems")} that are both in 
{NP_CLASS.key.get_reference("NP")} and {NP_HARD_CLASS.key.get_reference("NP-Hard")}. A problem is 
NP-Complete if: (1) given a proposed {SOLUTION.key.get_reference()}, it can be verified by a 
{DETERMINISTIC_TURING_MACHINE.key.get_reference("deterministic Turing machine")} in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")}, and (2) every 
problem in NP can be {POLYNOMIAL_REDUCTION.key.get_reference("reduced")} to it in polynomial time. NP-Complete 
problems are the "hardest" problems in NP - if any NP-Complete problem can be solved efficiently, then all 
problems in NP can be solved efficiently. The size of the {INPUT_DATA.key.get_reference()} affects the 
computational difficulty.

---

{SUBSET_SUM.key.get_reference()} is NP-Complete:

1. It is in {NP_CLASS.key.get_reference("NP")}: given a certificate (a subset), a
   {DETERMINISTIC_TURING_MACHINE.key.get_reference("deterministic Turing machine")} can verify it
   sums to T in {POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")}.

2. It is {NP_HARD_CLASS.key.get_reference("NP-Hard")}: every {PROBLEM.key.get_reference()} in NP can be
   {POLYNOMIAL_REDUCTION.key.get_reference("reduced")} to {SUBSET_SUM.key.get_reference()} in polynomial time.

Because it satisfies both conditions, {SUBSET_SUM.key.get_reference()} sits at the intersection of NP and NP-Hard —
the definition of NP-Complete class.
"""


NP_COMPLETE_CLASS = _NPCompleteClass(
    DefinitionKey(name="NP-Complete class", field=FieldName.MATHEMATICS),
    aliases=["NP-Complete", "NP-C"],
)
