from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName


class _Observable(Definition):
    def _get_content(self) -> str:
        return f"""
A property, quantity, or phenomenon that can be perceived, detected, or measured. As an adjective, "observable" 
describes anything whose presence, absence, or value can in principle be determined.

---

Whether a light is on or off is observable: anyone in the room can see it.
"""


OBSERVABLE = _Observable(
    key=DefinitionKey(
        name="observable",
        field=FieldName.MATHEMATICS,
    )
)
