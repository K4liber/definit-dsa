from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.linked_list import LINKED_LIST
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _CircularLinkedList(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {LINKED_LIST.key.get_reference("linked list")} in which the last 
{NODE.key.get_reference("node")} points back to the first node.

This forms a {CYCLE.key.get_reference("cycle")} and allows traversal to wrap around indefinitely.

---

For example, three nodes holding 7, 9, and 2 can be linked so that the last node points back to the first: 
7 → 9 → 2 → (back to 7). Starting at the node holding 7 and following each link visits 7, 9, 2, 7, 9, 2, ... 
repeating forever instead of reaching an end.
"""


CIRCULAR_LINKED_LIST = _CircularLinkedList(
    key=DefinitionKey(
        name="circular linked list",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
