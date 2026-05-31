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
"""


RANDOMNESS = _Randomness(
    key=DefinitionKey(
        name="randomness",
        field=FieldName.MATHEMATICS,
    )
)
