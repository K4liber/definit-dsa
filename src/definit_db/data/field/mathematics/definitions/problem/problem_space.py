from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _ProblemSpace(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
The {SET.key.get_reference()} of all possible candidates for 
{SOLUTION.key.get_reference("solutions")} to a {PROBLEM.key.get_reference()}. It represents the entire 
domain that must be searched through to find a valid or {OPTIMAL_SOLUTION.key.get_reference("optimal solution")}.

---

For the {PROBLEM.key.get_reference()} "choose an even {NUMBER.key.get_reference("number")} from "2", "4", "5", and 
"7"", the problem space is the {SET.key.get_reference()} containing "2", "4", "5", and "7" — every candidate that 
must be examined. Inspecting each one shows that "2" and "4" are the valid 
{SOLUTION.key.get_reference("solutions")}.
"""


PROBLEM_SPACE = _ProblemSpace(DefinitionKey(name="problem space", field=FieldName.MATHEMATICS))
