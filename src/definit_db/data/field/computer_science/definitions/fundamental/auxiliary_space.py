from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _AuxiliarySpace(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the extra {COMPUTER_MEMORY.key.get_reference(phrase="memory")} an
{ALGORITHM.key.get_reference(phrase="algorithm")} uses beyond the space needed to store its 
{INPUT_DATA.key.get_reference(phrase="input")} (or output).
"""


AUXILIARY_SPACE = _AuxiliarySpace(
    key=DefinitionKey(
        name="auxiliary space",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
