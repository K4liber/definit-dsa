from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY


class _Randomness(Definition):
    def _get_content(self) -> str:
        return f"""
Randomness is the quality of an outcome, event, or process that cannot be predicted with certainty.
In mathematics, randomness is modeled using {PROBABILITY.key.get_reference(phrase="probabilities")} and 
{DISTRIBUTION.key.get_reference(phrase="distributions")}: individual outcomes may be uncertain, while their 
long-run behavior can still have a precise mathematical description.

---

A fair coin flip is random: no individual outcome (heads or tails) can be predicted with certainty.
Yet the process is not without structure — its distribution is fully described by:

P(heads) = 0.5
P(tails) = 0.5

Flipping the coin 10 times might produce: H T H H T T H T T H (unpredictable in advance).
Flipping it 1,000,000 times will produce heads approximately 500,000 times — the randomness of
individual outcomes averages out to a predictable long-run behavior.
"""


RANDOMNESS = _Randomness(
    key=DefinitionKey(
        name="randomness",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["random behavior"],
)
