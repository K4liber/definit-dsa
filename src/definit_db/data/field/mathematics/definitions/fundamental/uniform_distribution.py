from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _UniformDistribution(Definition):
    def _get_content(self) -> str:
        return f"""
A uniform distribution is a {DISTRIBUTION.key.get_reference()} in which all 
{ITEM.key.get_reference(phrase="elements")} of a {SET.key.get_reference("set")} are assigned equal weight or 
{PROBABILITY.key.get_reference()}, so each outcome is equally likely.

---

A fair six-sided die produces a uniform distribution over the set {{1, 2, 3, 4, 5, 6}}:

P(1) = P(2) = P(3) = P(4) = P(5) = P(6) = 1/6 ≈ 0.167

No outcome is favoured over any other. Contrast this with the loaded die from the distribution
example, where P(6) = 0.5 — that is not a uniform distribution.
"""


UNIFORM_DISTRIBUTION = _UniformDistribution(
    key=DefinitionKey(
        name="uniform_distribution",
        field=FieldName.MATHEMATICS,
    )
)
