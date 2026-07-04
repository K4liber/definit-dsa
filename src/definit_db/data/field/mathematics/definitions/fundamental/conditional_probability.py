from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY


class _ConditionalProbability(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Conditional probability")} is the {PROBABILITY.key.get_reference()} of an event A
occurring given that another event B has occurred.

It is typically written as P(A | B).

---

Rolling a fair six-sided die, let A be "the roll is 4" and B be "the roll is even" (2, 4, or 6).

The unconditional {PROBABILITY.key.get_reference()} of A is 1/6, since only one of the six faces is a 4.
Once it is known that B has occurred, only 3 outcomes remain possible (2, 4, 6), and 1 of them is a 4, so
P(A | B) = 1/3 — higher than the unconditional 1/6, because knowing B narrowed down the possible outcomes.
"""


CONDITIONAL_PROBABILITY = _ConditionalProbability(
    key=DefinitionKey(
        name="conditional probability",
        field=FieldName.MATHEMATICS,
    )
)
