from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.domain import DOMAIN
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Distribution(Definition):
    def _get_content(self) -> str:
        return f"""
A distribution describes how values (or outcomes) are spread over a {DOMAIN.key.get_reference(phrase="domain")}. 
Typically it associates {ITEM.key.get_reference(phrase="elements")} of a {SET.key.get_reference("set")} or values to 
their frequencies or {PROBABILITY.key.get_reference(phrase="probabilities")}, describing how likely or how common 
different {OBJECT.key.get_reference(phrase="objects")} are.

---

A six-sided die has the following distribution over its outcomes:

Outcome:     1     2     3     4     5     6

Probability: 1/6   1/6   1/6   1/6   1/6   1/6

Each outcome is equally likely. A loaded die might have a different distribution:

Outcome:     1     2     3     4     5     6

Probability: 0.1   0.1   0.1   0.1   0.1   0.5

Here the value 6 is five times more likely than any other outcome. Both are valid distributions
because all probabilities are in [0, 1] and sum to 1.
"""


DISTRIBUTION = _Distribution(
    key=DefinitionKey(
        name="distribution",
        field=FieldName.MATHEMATICS,
    )
)
