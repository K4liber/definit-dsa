from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.object import OBJECT


class _Operation(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an action that is carried out to accomplish a given task. In the most simple scenario, 
it is an action performed on at least one {OBJECT.key.get_reference(phrase="object")}.

---

Appending a new score to the object (72, 85, 90), producing (72, 85, 90, 91), is an operation: it is an action
carried out on that object to accomplish the task of adding a value.
"""


OPERATION = _Operation(
    key=DefinitionKey(
        name="operation",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
