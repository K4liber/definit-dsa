from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity_theory import COMPLEXITY_THEORY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_class import NP_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.computation.deterministic_turing_machine import (
    DETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.computation.nondeterministic_turing_machine import (
    NONDETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.problem.complement_problem import COMPLEMENT_PROBLEM
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subset_sum import SUBSET_SUM


class _CoNPClass(Definition):
    def _get_content(self) -> str:
        return f"""
A {COMPLEXITY.key.get_reference("complexity")} class in
{COMPUTATION.key.get_reference("computational")} 
{COMPLEXITY_THEORY.key.get_reference("complexity theory")} that
contains all decision {PROBLEM.key.get_reference("problems")} whose
{COMPLEMENT_PROBLEM.key.get_reference("complement")} is in {NP_CLASS.key.get_reference("NP")}. A 
problem is in Co-NP if the "no" instances can be verified by a 
{DETERMINISTIC_TURING_MACHINE.key.get_reference("deterministic Turing machine")} in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time complexity")}. 
Equivalently, the {COMPLEMENT_PROBLEM.key.get_reference("complement")} of the problem can be
{SOLUTION.key.get_reference("solved")} by a
{NONDETERMINISTIC_TURING_MACHINE.key.get_reference("nondeterministic Turing machine")} in time 
{BIG_O_NOTATION.key.get_reference("O(n^k)")} for some constant k, where n is the size of the 
{INPUT_DATA.key.get_reference()}. Co-NP stands for "Complement of NP."

---

The {COMPLEMENT_PROBLEM.key.get_reference("complement")} of {SUBSET_SUM.key.get_reference()} - 

"does NO subset of the integers sum to T?" is in Co-NP class.

Input: {{3, 1, 4, 1, 5}}, T = 9

A "no" answer to the complement means a subset DOES exist ({{4, 5}} sums to 9).


That certificate can be verified quickly by a 
{DETERMINISTIC_TURING_MACHINE.key.get_reference("deterministic Turing machine")}
in {POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time")}, 
satisfying the Co-NP definition.
"""


CO_NP_CLASS = _CoNPClass(DefinitionKey(name="Co-NP class", field=FieldName.MATHEMATICS))
