from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _Instruction(Definition):
    def _get_content(self) -> str:
        return f"""
A piece of {INFORMATION.key.get_reference(phrase="information")} that describes how something should be done
or operated.

---

"Turn the key to the right" is an instruction: a piece of
{INFORMATION.key.get_reference(phrase="information")} that tells someone how to open a lock.
"""


INSTRUCTION = _Instruction(
    key=DefinitionKey(
        name="instruction",
        field=FieldName.MATHEMATICS,
    )
)
