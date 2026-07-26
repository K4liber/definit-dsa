from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.merge import MERGE
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _DivideAndConquer(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {ALGORITHM.key.get_reference()} that solves a {PROBLEM.key.get_reference()} by 
{RECURSION.key.get_reference("recursively")} breaking it down into smaller 
{SUBPROBLEM.key.get_reference("subproblems")}, solving each subproblem independently, and then combining their 
{SOLUTION.key.get_reference("solutions")} to form a solution to the original problem. Divide and conquer 
algorithms often lead to {EFFICIENCY.key.get_reference(phrase="efficient")} and elegant solutions. 
They may or may not always produce the {OPTIMAL_SOLUTION.key.get_reference("optimal solution")}.

---

{SORTING.key.get_reference(phrase="Sorting")} the {SEQUENCE.key.get_reference(phrase="array")} [5, 2, 8, 1] 
by recursively splitting it in half, sorting each half independently, and merging the sorted halves back together:

Divide:


[5, 2, 8, 1]


├─[5, 2]

│├─[5]  ← base case, a single element is already sorted

│└─[2]  ← base case

└─[8, 1]

─├─[8]  ← base case

─└─[1]  ← base case

Conquer ({MERGE.key.get_reference(phrase="merge")} sorted halves bottom-up):


[5] + [2] → [2, 5]

[8] + [1] → [1, 8]


Combine:


[2, 5] + [1, 8] → [1, 2, 5, 8]


Each subproblem ([5,2] and [8,1]) is solved entirely independently before the results are
combined — this independence is the hallmark of divide and conquer.
"""


DIVIDE_AND_CONQUER = _DivideAndConquer(
    key=DefinitionKey(
        name="divide_and_conquer",
        field=FieldName.MATHEMATICS,
    )
)
