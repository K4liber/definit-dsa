from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.list import LIST
from definit_db.data.field.computer_science.definitions.fundamental.pointer import POINTER
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _LinkedList(Definition):
    def _get_content(self) -> str:
        return f"""
A {LIST.key.get_reference(phrase="list")} implemented as an ordered {COLLECTION.key.get_reference(phrase="collection")} 
of {ITEM.key.get_reference(phrase="elements")}. Each {ITEM.key.get_reference(phrase="element")} is stored in a 
{NODE.key.get_reference(phrase="node")} that contains a {POINTER.key.get_reference(phrase="reference")} 
to the next node. Linked lists can be singly linked or doubly linked, 
depending on whether each node has a reference to the next node only or both the next and previous nodes.

---

For example, a singly linked list holding the values 7, 9, and 2 consists of three nodes: the first stores 7 and a 
link to the second, the second stores 9 and a link to the third, and the third stores 2 with a link pointing to 
nothing (the end of the list). Starting from the first node and following each link visits the values in order. 
In a doubly linked list, each node would also carry a backward link to the previous node.
"""


LINKED_LIST = _LinkedList(
    key=DefinitionKey(
        name="linked_list",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
