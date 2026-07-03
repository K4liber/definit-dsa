from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _ObjectiveFunction(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a {FUNCTION.key.get_reference()} that represents the goal or objective 
to be {OPTIMIZATION.key.get_reference("optimized")} in a {PROBLEM.key.get_reference()}. 
The objective function is either maximized or minimized to find the best solution, and its value determines 
the quality of any given solution.

---

For a delivery-route {PROBLEM.key.get_reference()}, the total distance traveled is the 
{self.key.get_reference("objective function")}: it is a {FUNCTION.key.get_reference()} of the chosen route, and 
{OPTIMIZATION.key.get_reference("optimizing")} the route means minimizing this function's value to find the 
shortest route among all valid routes.
"""


OBJECTIVE_FUNCTION = _ObjectiveFunction(DefinitionKey(name="objective function", field=FieldName.MATHEMATICS))
