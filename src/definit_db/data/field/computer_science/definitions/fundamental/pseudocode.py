from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM


class _Pseudocode(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an informal, human-readable description of the steps of an 
{ALGORITHM.key.get_reference("algorithm")} or {PROGRAM.key.get_reference("program")}, 
written in a way that resembles code but is not tied to any specific programming language.
Pseudocode is used to communicate ideas and logic without implementation details.
"""


PSEUDOCODE = _Pseudocode(
    key=DefinitionKey(
        name="pseudocode",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
