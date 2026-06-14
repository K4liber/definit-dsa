from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _Heuristic(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {FUNCTION.key.get_reference()} or strategy used in an 
{ALGORITHM.key.get_reference()} to guide decision-making when finding a {SOLUTION.key.get_reference()} to a 
{PROBLEM.key.get_reference()}. It provides an estimate that helps the algorithm make more informed choices 
by evaluating different options, allowing algorithms to explore more promising paths first and improve efficiency.

---

To quickly find a large {NUMBER.key.get_reference(phrase="number")} in the sequence "3", "7", "9", a heuristic 
such as "return the first number greater than "5"" yields the good-enough {SOLUTION.key.get_reference()} "7" 
without examining every number, rather than guaranteeing the largest.
"""


HEURISTIC = _Heuristic(DefinitionKey(name="heuristic", field=FieldName.MATHEMATICS))
