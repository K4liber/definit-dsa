from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _Pointer(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a value that refers to a location in {COMPUTER_MEMORY.key.get_reference()}.

A pointer can be used to indirectly access {INFORMATION.key.get_reference()} stored at that location.
"""


POINTER = _Pointer(
    key=DefinitionKey(
        name="pointer",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
