from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.one_dimensional_dynamic_programming import (
    ONE_DIMENSIONAL_DYNAMIC_PROGRAMMING,
)
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.matrix import MATRIX
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _MultidimensionalDynamicProgramming(Definition):
    def _get_content(self) -> str:
        return f"""
Multidimensional Dynamic Programming is a form of 
{DYNAMIC_PROGRAMMING.key.get_reference(phrase="dynamic programming")} where each 
{SUBPROBLEM.key.get_reference(phrase="subproblem")} state is identified by multiple 
{INDEX.key.get_reference(phrase="indices")}. Unlike 
{ONE_DIMENSIONAL_DYNAMIC_PROGRAMMING.key.get_reference(phrase="1D dynamic programming")}, it stores states across a 
multi-axis structure such as a {MATRIX.key.get_reference()}.

---

Count the number of paths from (0,0) to (2,2) in a grid, moving only right or down.
Each {SUBPROBLEM.key.get_reference()} state is identified by two {INDEX.key.get_reference(phrase="indices")} (i, j)
and stored in a {MATRIX.key.get_reference()}:

dp[i][j] = number of paths to reach cell (i, j).

Base case 1: dp[0][j] = 1 (only one way: go right along the top row).

Base case 2: dp[i][0] = 1 (only one way: go down along the left column).

Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1].

After filling the table, the matrix is:

Row 0: 1, 1, 1

Row 1: 1, 2, 3

Row 2: 1, 3, 6

There are 6 paths from (0,0) to (2,2). The state space is two-dimensional (row × column),
which is why a single {INDEX.key.get_reference()}, as in 
{ONE_DIMENSIONAL_DYNAMIC_PROGRAMMING.key.get_reference(phrase="1D dynamic programming")}, is not sufficient.
"""


MULTIDIMENSIONAL_DYNAMIC_PROGRAMMING = _MultidimensionalDynamicProgramming(
    key=DefinitionKey(
        name="Multidimensional Dynamic Programming",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["multidimensional DP"],
)
