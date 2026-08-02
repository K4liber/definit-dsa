from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.searching.binary_search import BINARY_SEARCH
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _HalfAndHalfApproach(Definition):
    def _get_content(self) -> str:
        return f"""
A {ALGORITHM.key.get_reference()} design approach that solves a {PROBLEM.key.get_reference()} by dividing it 
into two equal or nearly equal halves, solving each half independently (often using {RECURSION.key.get_reference()}), 
and then combining the {SOLUTION.key.get_reference("solutions")} from both halves. This approach is particularly 
{EFFICIENCY.key.get_reference(phrase="efficient")} for problems where the 
{SUBPROBLEM.key.get_reference("subproblems")} can be balanced and 
solved in parallel or sequentially with reduced {COMPLEXITY.key.get_reference()}.

---

{BINARY_SEARCH.key.get_reference("Binary search")} applies the half-and-half approach: to find "9" in the 
{SEQUENCE.key.get_reference("sequence")} "1, 3, 5, 7, 9, 11, 13", it compares "9" to the middle 
{ITEM.key.get_reference("element")} "7", 
discards the half that cannot contain the target, and repeats the same halving step on the remaining 
"9, 11, 13" until the {SOLUTION.key.get_reference("solution")} is found.
"""


HALF_AND_HALF_APPROACH = _HalfAndHalfApproach(
    key=DefinitionKey(
        name="half_and_half_approach",
        field=FieldName.MATHEMATICS,
    )
)
