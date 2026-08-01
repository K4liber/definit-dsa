from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity_theory import COMPLEXITY_THEORY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.computation.deterministic_turing_machine import (
    DETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.computation.nondeterministic_turing_machine import (
    NONDETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.fundamental.exponential import EXPONENTIAL
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.fundamental.subset import SUBSET
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subset_sum import SUBSET_SUM


class _NPClass(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {COMPLEXITY.key.get_reference("complexity")} class in 
{COMPUTATION.key.get_reference(phrase="computational")} 
{COMPLEXITY_THEORY.key.get_reference("complexity theory")} that contains all decision 
{PROBLEM.key.get_reference("problems")} that can be solved 
by a {NONDETERMINISTIC_TURING_MACHINE.key.get_reference("nondeterministic Turing machine")} in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time complexity")}. 
Equivalently, a problem is in NP if, given a proposed {SOLUTION.key.get_reference()}, there exists a 
{DETERMINISTIC_TURING_MACHINE.key.get_reference("deterministic Turing machine")} that can verify the 
solution's correctness in time {BIG_O_NOTATION.key.get_reference("O(n^k)")} for some constant k, where 
n is the size of the {INPUT_DATA.key.get_reference()}. NP stands for "Nondeterministic Polynomial time."

---

{SUBSET_SUM.key.get_reference()}: given a set of {INTEGER.key.get_reference("integers")} and a target T, 
does any {SUBSET.key.get_reference()} sum to T?

Input: {{3, 1, 4, 1, 5}}, T = 9.

Finding a {SOLUTION.key.get_reference()} may require checking {EXPONENTIAL.key.get_reference(phrase="exponentially")} 
many {SUBSET.key.get_reference("subsets")}.

But verifying a proposed {SOLUTION.key.get_reference()} is easy — given the certificate {{4, 5}}:

4 + 5 = 9, checked in O(n) {TIME_COMPLEXITY.key.get_reference("time")}.

Because {SOLUTION.key.get_reference("solutions")} can be verified in 
{POLYNOMIAL.key.get_reference("polynomial")} time,
subset-sum is in NP class.
"""


NP_CLASS = _NPClass(DefinitionKey(name="NP class", field=FieldName.MATHEMATICS))
