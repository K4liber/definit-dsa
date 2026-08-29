from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity_theory import COMPLEXITY_THEORY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.computation.deterministic_turing_machine import (
    DETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _PClass(Definition):
    def _get_content(self) -> str:
        return f"""
A {COMPLEXITY.key.get_reference("complexity")} class in computational 
{COMPLEXITY_THEORY.key.get_reference("complexity theory")} that contains all decision 
{PROBLEM.key.get_reference("problems")} that can be solved 
by a {DETERMINISTIC_TURING_MACHINE.key.get_reference("deterministic Turing machine")} in 
{POLYNOMIAL.key.get_reference("polynomial")} {TIME_COMPLEXITY.key.get_reference("time complexity")}. 
A problem is in P if there exists an {ALGORITHM.key.get_reference()} that can solve any instance of the 
problem in time {BIG_O_NOTATION.key.get_reference("O(n^k)")} for some constant k, where n is the size 
of the {INPUT_DATA.key.get_reference()}. In other words, there is a {COMPUTATION.key.get_reference()} that
produces a correct {SOLUTION.key.get_reference()} in polynomial time. Problems in P are considered
{EFFICIENCY.key.get_reference(phrase="efficiently")} solvable or tractable.

---

Finding the maximum {ITEM.key.get_reference("element")} in a {SEQUENCE.key.get_reference()} of n numbers 
is in P class:
a single pass compares each {ITEM.key.get_reference("element")} once, always finishing in O(n) 
{TIME_COMPLEXITY.key.get_reference("time")} —
{POLYNOMIAL.key.get_reference("polynomial")} in the size of the {INPUT_DATA.key.get_reference()}.


Input: [3, 1, 4, 1, 5, 9, 2, 6]  →  maximum = 9  (7 comparisons, always O(n))


No matter what the input is, the {ALGORITHM.key.get_reference()} finishes in polynomial time.
"""


P_CLASS = _PClass(
    DefinitionKey(name="P class", field=FieldName.MATHEMATICS),
    aliases=["P", "complexity class P"],
)
