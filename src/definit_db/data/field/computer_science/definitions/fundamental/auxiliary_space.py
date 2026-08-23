from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.storage import STORAGE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _AuxiliarySpace(Definition):
    def _get_content(self) -> str:
        return f"""
The extra {COMPUTER_MEMORY.key.get_reference(phrase="memory")} an
{ALGORITHM.key.get_reference(phrase="algorithm")} uses beyond the space needed to 
{STORAGE.key.get_reference(phrase="store")} its 
{INPUT_DATA.key.get_reference(phrase="input")} (or output).

---

An algorithm that processes its input using only a fixed number of temporary values has constant auxiliary space,
regardless of how large the input grows. In contrast, an algorithm that builds a full copy of its input into a
separate structure uses auxiliary memory that grows in proportion to the input size.
"""


AUXILIARY_SPACE = _AuxiliarySpace(
    key=DefinitionKey(
        name="auxiliary space",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=("extra space",),
)
