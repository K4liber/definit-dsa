from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.object import OBJECT
from definit_db.data.field.computer_science.definitions.fundamental.pointer import POINTER


class _Null(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a special value that represents "no value" or 
"no {OBJECT.key.get_reference(phrase="object")}".

It is often used to indicate that a {POINTER.key.get_reference(phrase="pointer")} does not refer to
a valid {COMPUTER_MEMORY.key.get_reference(phrase="memory")} location (i.e., it points to nothing).
"""


NULL = _Null(
    key=DefinitionKey(
        name="null",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
