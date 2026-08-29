from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _FirstInFirstOut(Definition):
    def _get_content(self) -> str:
        return f"""
An ordering principle for a {SEQUENCE.key.get_reference()} where the earliest added element is the first one to be 
removed.

---

A line of customers waiting at a counter follows first in first out: the person who joined the line earliest is the 
first one served.
"""


FIRST_IN_FIRST_OUT = _FirstInFirstOut(
    DefinitionKey(name="first in first out", field=FieldName.MATHEMATICS),
    aliases=("FIFO", "first-in-first-out"),
)
