from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.intersection import INTERSECTION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _MutualExclusivity(Definition):
    def _get_content(self) -> str:
        return f"""
Mutual exclusivity means that two events cannot occur at the same time.

In set terms, two {SET.key.get_reference(phrase="sets")} A and B are mutually exclusive if their
{INTERSECTION.key.get_reference()} is empty.

---

Rolling a single die, let A be "the roll is 1" and B be "the roll is 2". As {SET.key.get_reference(phrase="sets")},
A = (1) and B = (2) have an empty {INTERSECTION.key.get_reference()}, so A and B are mutually exclusive — a single
roll cannot be both 1 and 2 at once.

By contrast, let C be "the roll is even" (2, 4, 6). B and C are not mutually exclusive, since a roll of 2 belongs
to both.
"""


MUTUAL_EXCLUSIVITY = _MutualExclusivity(
    key=DefinitionKey(
        name="mutual exclusivity",
        field=FieldName.MATHEMATICS,
    )
)
