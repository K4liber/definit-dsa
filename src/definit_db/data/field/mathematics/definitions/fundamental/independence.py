from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION


class _Independence(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} describes a {RELATION.key.get_reference(phrase="relationship")} 
between events where the occurrence of one event does not change the {PROBABILITY.key.get_reference()} of the other.

Two events A and B are independent if P(A and B) = P(A) * P(B).
"""


INDEPENDENCE = _Independence(
    key=DefinitionKey(
        name="independence",
        field=FieldName.MATHEMATICS,
    )
)
