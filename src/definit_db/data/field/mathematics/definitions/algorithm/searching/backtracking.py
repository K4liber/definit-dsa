from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.searching.depth_first_search import DEPTH_FIRST_SEARCH
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.problem_space import PROBLEM_SPACE
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _Backtracking(Definition):
    def _get_content(self) -> str:
        return f"""
Backtracking is an {ALGORITHM.key.get_reference(phrase="algorithmic")} technique that explores a 
{PROBLEM_SPACE.key.get_reference(phrase="problem space")} by building a partial 
{SOLUTION.key.get_reference(phrase="solution")} step by step. When the partial solution violates a 
{CONSTRAINT.key.get_reference(phrase="constraint")} or cannot lead to a valid solution, the algorithm abandons 
that branch and tries another choice. It is commonly implemented with {RECURSION.key.get_reference()} and follows 
the search pattern of {DEPTH_FIRST_SEARCH.key.get_reference(phrase="depth-first search")}.
"""


BACKTRACKING = _Backtracking(
    key=DefinitionKey(
        name="backtracking",
        field=FieldName.MATHEMATICS,
    )
)