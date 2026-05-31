from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Information(Definition):
    def _get_content(self) -> str:
        return f"""
An abstract concept that refers to something which has the power to inform. 
At the most fundamental level, it pertains to the interpretation (perhaps formally) of that which may be 
sensed, or their abstractions. Any natural process that is not completely random and any observable 
pattern in any medium can be said to convey some amount of information.

---

Whether an {OBJECT.key.get_reference("object")} is present or absent at a given place
conveys information about that place.
"""


INFORMATION = _Information(
    key=DefinitionKey(
        name="information",
        field=FieldName.MATHEMATICS,
    )
)
