from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.objective_function import OBJECTIVE_FUNCTION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.feasible_solution import FEASIBLE_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _MathematicalProgramming(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a mathematical approach to finding the 
{OPTIMAL_SOLUTION.key.get_reference("optimal solution")} to a {PROBLEM.key.get_reference()} by 
{OPTIMIZATION.key.get_reference("optimizing")} an {OBJECTIVE_FUNCTION.key.get_reference()} subject to 
{CONSTRAINT.key.get_reference("constraints")}. The goal is to maximize or minimize the objective function while 
ensuring the solution is a {FEASIBLE_SOLUTION.key.get_reference()}.

---

A factory {PROBLEM.key.get_reference()} of maximizing profit from producing two products, subject to a limited 
number of labor hours and raw materials as {CONSTRAINT.key.get_reference("constraints")}, is a case of 
{self.key.get_reference("mathematical programming")}: the profit formula is the 
{OBJECTIVE_FUNCTION.key.get_reference()}, every production plan that respects the labor and material limits is a 
{FEASIBLE_SOLUTION.key.get_reference()}, and the plan yielding the highest profit among them is the 
{OPTIMAL_SOLUTION.key.get_reference("optimal solution")}.
"""


MATHEMATICAL_PROGRAMMING = _MathematicalProgramming(
    DefinitionKey(name="mathematical programming", field=FieldName.MATHEMATICS)
)
