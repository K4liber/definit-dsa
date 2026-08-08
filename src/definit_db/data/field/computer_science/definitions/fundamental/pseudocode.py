from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.list import LIST
from definit_db.data.field.computer_science.definitions.fundamental.code import CODE
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _Pseudocode(Definition):
    def _get_content(self) -> str:
        return f"""
An informal, human-readable description of the steps of an 
{ALGORITHM.key.get_reference("algorithm")} or {PROGRAM.key.get_reference("program")}, 
written in a way that resembles {CODE.key.get_reference()} but is not tied to any specific language.
Pseudocode is used to communicate ideas and logic without implementation details.

---

To describe finding the largest value in a {LIST.key.get_reference(phrase="list")}, pseudocode might read: 
"set max to the first {ITEM.key.get_reference(phrase="element")}; for each
remaining {ITEM.key.get_reference(phrase="element")}, if it is greater than max, update max; return max." 
Each line is an {INSTRUCTION.key.get_reference(phrase="instruction")} a programmer could later translate 
into any language without changing the underlying logic.
"""


PSEUDOCODE = _Pseudocode(
    key=DefinitionKey(
        name="pseudocode",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
