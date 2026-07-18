from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.conditional_probability import CONDITIONAL_PROBABILITY
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY


class _BayesTheorem(Definition):
    def _get_content(self) -> str:
        return f"""
A rule for calculating 
{CONDITIONAL_PROBABILITY.key.get_reference(phrase="conditional probabilities")}.

For two events A and B with P(B) != 0, it states:

P(A | B) = P(B | A) * P(A) / P(B)

This lets P(A | B) be computed from the reverse
{CONDITIONAL_PROBABILITY.key.get_reference(phrase="conditional probability")} P(B | A), together with the
individual {PROBABILITY.key.get_reference(phrase="probabilities")} of A and B.

---

1% of a population has a disease (P(disease) = 0.01). A test correctly detects the disease 90% of the time
(P(positive | disease) = 0.9) but also gives a false positive for 5% of healthy people
(P(positive | no disease) = 0.05).

P(positive) = P(positive | disease) * P(disease) + P(positive | no disease) * P(no disease)
            = 0.9 * 0.01 + 0.05 * 0.99 = 0.009 + 0.0495 = 0.0585

P(disease | positive) = P(positive | disease) * P(disease) / P(positive) = 0.009 / 0.0585 ≈ 0.154

So even after a positive test, there is only about a 15.4% chance of actually having the disease.
"""


BAYES_THEOREM = _BayesTheorem(
    key=DefinitionKey(
        name="Bayes theorem",
        field=FieldName.MATHEMATICS,
    )
)
