from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Probability(Definition):
    def _get_content(self) -> str:
        return f"""
Probability is a measure that quantifies the likelihood of elements in a {SET.key.get_reference("set")} 
or events, typically expressed as a {NUMBER.key.get_reference("number")} between 0 and 1. Probabilities indicate 
how likely different {OBJECT.key.get_reference(phrase="objects")} or outcomes are to occur.

---

A bag contains 3 red balls and 2 blue balls (5 total). The probability of each outcome when
drawing one ball at random:

P(red)  = 3/5 = 0.6
P(blue) = 2/5 = 0.4
P(green) = 0   (impossible — no green balls)
P(red or blue) = 1 (certain — every ball is one of the two)

All probabilities lie in [0, 1] and the probabilities of all possible outcomes sum to 1.
"""


PROBABILITY = _Probability(
    key=DefinitionKey(
        name="probability",
        field=FieldName.MATHEMATICS,
    )
)
