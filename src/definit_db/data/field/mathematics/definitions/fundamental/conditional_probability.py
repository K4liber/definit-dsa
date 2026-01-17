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
"""


CONDITIONAL_PROBABILITY = _ConditionalProbability(
    key=DefinitionKey(
        name="conditional probability",
        field=FieldName.MATHEMATICS,
    )
)
