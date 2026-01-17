from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.conditional_probability import CONDITIONAL_PROBABILITY
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY


class _BayesTheorem(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference("Bayes theorem")} is a rule for calculating 
{CONDITIONAL_PROBABILITY.key.get_reference(phrase="conditional probabilities")}.

For two events A and B with P(B) != 0, it relates P(A | B) to P(B | A) using {PROBABILITY.key.get_reference()}.
"""


BAYES_THEOREM = _BayesTheorem(
    key=DefinitionKey(
        name="Bayes theorem",
        field=FieldName.MATHEMATICS,
    )
)
