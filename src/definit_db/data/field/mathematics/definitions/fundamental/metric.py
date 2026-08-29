from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Metric(Definition):
    def _get_content(self) -> str:
        return f"""
A quantifiable measure, expressed as a {NUMBER.key.get_reference(phrase="number")}, used to evaluate, compare, or
describe something. A metric assigns a numerical value to each {OBJECT.key.get_reference(phrase="instance")} 
being studied so that they can be compared on a common scale.

---

For a fleet of vehicles, fuel consumption in liters per 100 km is a metric: each vehicle receives a
{NUMBER.key.get_reference(phrase="number")} (e.g. 6.5, 8.2, 11.0), allowing direct comparison — a vehicle rated 6.5
uses less fuel than one rated 8.2.
"""


METRIC = _Metric(
    key=DefinitionKey(
        name="metric",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["performance measure", "measure"],
)
