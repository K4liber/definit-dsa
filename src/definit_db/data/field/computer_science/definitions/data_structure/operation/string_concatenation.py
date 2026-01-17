from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _StringConcatenation(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference("String concatenation")} is the {OPERATION.key.get_reference("operation")} of 
joining two or more {STRING.key.get_reference("strings")} end-to-end to form a new string.
"""


STRING_CONCATENATION = _StringConcatenation(
    key=DefinitionKey(
        name="string concatenation",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
