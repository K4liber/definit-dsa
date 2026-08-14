from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION


class _Independence(Definition):
    def _get_content(self) -> str:
        return f"""
independence describes a {RELATION.key.get_reference(phrase="relationship")} 
between events where the occurrence of one event does not change the {PROBABILITY.key.get_reference()} of the other.

Two events A and B are independent if P(A and B) = P(A) * P(B).

---

Flipping a fair coin twice: let A be "heads on the first flip" and B be "heads on the second flip".
P(A) = 1/2 and P(B) = 1/2, and since the first flip does not influence the second, P(A and B) = 1/2 * 1/2 = 1/4,
confirming that A and B are independent.

By contrast, rolling a single die, let A be "the roll is even" and B be "the roll is 4". Here P(A and B) = 1/6,
but P(A) * P(B) = 1/2 * 1/6 = 1/12, which is not equal to 1/6 — so A and B are not independent, since knowing the
roll is 4 guarantees that it is also even.
"""


INDEPENDENCE = _Independence(
    key=DefinitionKey(
        name="independence",
        field=FieldName.MATHEMATICS,
    )
)
