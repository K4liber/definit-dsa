from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _LastInFirstOut(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an ordering principle for a {SEQUENCE.key.get_reference()} where the most 
recently added element is the first one to be removed.

---

A stack of plates follows last in first out: you add and remove plates only from the top, so the plate
added most recently is the first one taken off.
"""


LAST_IN_FIRST_OUT = _LastInFirstOut(DefinitionKey(name="last in first out", field=FieldName.MATHEMATICS))
