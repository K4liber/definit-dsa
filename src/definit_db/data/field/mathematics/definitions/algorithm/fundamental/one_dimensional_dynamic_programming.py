from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.fundamental.fibonacci import FIBONACCI
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.recurrence import RECURRENCE
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.table import TABLE
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _OneDimensionalDynamicProgramming(Definition):
    def _get_content(self) -> str:
        return f"""
1D Dynamic Programming is a form of {DYNAMIC_PROGRAMMING.key.get_reference(phrase="dynamic programming")} where each 
{SUBPROBLEM.key.get_reference(phrase="subproblem")} state can be represented by a single {INDEX.key.get_reference()} 
over a {SEQUENCE.key.get_reference()}. It is often used when the {RECURRENCE.key.get_reference()} depends on earlier 
positions in one ordered dimension.

---

Computing the {FIBONACCI.key.get_reference(phrase="Fibonacci")} number F(6) using a 1D 
{TABLE.key.get_reference(phrase="table")}, where each {SUBPROBLEM.key.get_reference()} state is a single 
{INDEX.key.get_reference()} i:


dp = [0] * 7 ← allocate a {SEQUENCE.key.get_reference()} of length 7

dp[0] = 0 ← base case

dp[1] = 1 ← base case

dp[2] = dp[1] + dp[0] = 1

dp[3] = dp[2] + dp[1] = 2

dp[4] = dp[3] + dp[2] = 3

dp[5] = dp[4] + dp[3] = 5

dp[6] = dp[5] + dp[4] = 8


Each entry depends only on the two preceding indices — a single ordered dimension — so
one array is sufficient to store all {SUBPROBLEM.key.get_reference(phrase="subproblem")} results.
"""


ONE_DIMENSIONAL_DYNAMIC_PROGRAMMING = _OneDimensionalDynamicProgramming(
    key=DefinitionKey(
        name="1D Dynamic Programming",
        field=FieldName.MATHEMATICS,
    )
)
