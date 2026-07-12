from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.algorithms.two_pointers_technique import TWO_POINTERS_TECHNIQUE
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.linked_list import LINKED_LIST
from definit_db.data.field.computer_science.definitions.fundamental.pointer import POINTER
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.graph.cycle_detection import CYCLE_DETECTION
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _FloydsTortoiseAndHareAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
Floyd's Tortoise and Hare algorithm is a {CYCLE_DETECTION.key.get_reference(phrase="cycle detection")} 
{ALGORITHM.key.get_reference(phrase="algorithm")} that uses the 
{TWO_POINTERS_TECHNIQUE.key.get_reference(phrase="two pointers technique")}. One 
{POINTER.key.get_reference(phrase="pointer")}, the tortoise, advances one step at a time, while the other pointer, 
the hare, advances two steps at a time. If the two pointers meet, a {CYCLE.key.get_reference(phrase="cycle")} exists; 
if the hare reaches the end, no cycle exists. It is commonly used to detect cycles in a 
{LINKED_LIST.key.get_reference(phrase="linked list")}.

---

Consider a {LINKED_LIST.key.get_reference(phrase="linked list")} whose {NODE.key.get_reference(phrase="nodes")} run
A then B then C then D, where D points back to B, forming a cycle. Both pointers start at A:
- After one step: tortoise at B, hare at C
- After two steps: tortoise at C, hare at B (having wrapped around)
- After three steps: tortoise at D, hare at D
Because the faster hare has caught the tortoise, a cycle is confirmed.
"""


FLOYDS_TORTOISE_AND_HARE_ALGORITHM = _FloydsTortoiseAndHareAlgorithm(
    key=DefinitionKey(
        name="Floyd's Tortoise and Hare algorithm",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
