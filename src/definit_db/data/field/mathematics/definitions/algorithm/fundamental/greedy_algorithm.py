from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _GreedyAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {ALGORITHM.key.get_reference()} that builds up a {SOLUTION.key.get_reference()} piece by piece, always 
choosing the next piece that offers the most immediate benefit. Greedy algorithms do not always produce the 
{OPTIMAL_SOLUTION.key.get_reference("optimal solution")}, but they are often faster and simpler than other 
approaches.

---

The goal is to travel to North. You have a compass, so you know the direction to North, but you don't know 
if there are any obstacles in the way. The greedy algorithm could be to always take a step in the known direction 
of North. If you encounter an obstacle, you would need to go around it by taking a direction that is closest to 
the North direction. It could not be an optimal solution since having a map at the start you could find a shorter
path with a more efficient plan of how to omit obstacles.

"""


GREEDY_ALGORITHM = _GreedyAlgorithm(
    key=DefinitionKey(
        name="greedy_algorithm",
        field=FieldName.MATHEMATICS,
    )
)
