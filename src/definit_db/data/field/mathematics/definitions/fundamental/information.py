from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.observable import OBSERVABLE
from definit_db.data.field.mathematics.definitions.fundamental.randomness import RANDOMNESS


class _Information(Definition):
    def _get_content(self) -> str:
        return f"""
An abstract concept that refers to something which has the power to inform. Any natural process that is not completely 
{RANDOMNESS.key.get_reference(phrase="random")} and any {OBSERVABLE.key.get_reference(phrase="observable")} pattern in 
any medium can be said to convey some amount of information.

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
