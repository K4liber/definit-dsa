from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.base_case import BASE_CASE
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _Recursion(Definition):
    def _get_content(self) -> str:
        return f"""
A method of solving a {PROBLEM.key.get_reference()} where the {SOLUTION.key.get_reference()} depends on solutions 
to smaller instances of the same problem. Recursion involves a {FUNCTION.key.get_reference()} calling itself with 
simpler inputs until reaching a {BASE_CASE.key.get_reference()}.

---

To calculate a sum of a list of numbers from 1 to n, the recursive function adds n to the sum of the numbers 
from 1 to n-1. To calculate a sum up to n-1, the function calls itself with n-1.
The base case is when n equals 1, at which point the sum is simply 1.

On the diagram below we can see the recursive calls and their evaluations:


sum(5) = 5 + sum(4)

-> sum(4) = 4 + sum(3)

-> -> sum(3) = 3 + sum(2)

-> -> -> sum(2) = 2 + sum(1)

-> -> -> -> sum(1) = 1

-> -> -> sum(2) = 2 + 1 = 3

-> -> sum(3) = 3 + 3 = 6

-> sum(4) = 4 + 6 = 10


sum(5) = 5 + 10 = 15


"->" indicates a recursive call. Number of arrows indicates depth of recursion. 
The base case is reached when the function is called with 1 (no further recursive calls are made).
"""


RECURSION = _Recursion(
    key=DefinitionKey(
        name="recursion",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["recursive process"],
)
