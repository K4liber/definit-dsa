from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _DeliveryRouteProblem(Definition):
    def _get_content(self) -> str:
        return f"""
An {OPTIMIZATION.key.get_reference()} {PROBLEM.key.get_reference()} in which one or more vehicles must deliver goods
from a depot to a set of locations, and the goal is to choose routes that satisfy the
{CONSTRAINT.key.get_reference("constraints")} of the task (such as vehicle capacity, delivery time windows,
or the requirement that each location is visited exactly once) while keeping a cost such as the total
distance traveled as low as possible.

---

A depot must deliver packages to four locations. Each vehicle can carry at most 10 packages, and each
location must be visited exactly once. Finding an assignment of locations to vehicles and an ordering
of stops for each vehicle, so that no vehicle exceeds its capacity constraint while the total distance
traveled is kept small, is a delivery-route problem.
"""


DELIVERY_ROUTE_PROBLEM = _DeliveryRouteProblem(
    key=DefinitionKey(
        name="delivery-route problem",
        field=FieldName.MATHEMATICS,
    )
)
