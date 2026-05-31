from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.linked_list import LINKED_LIST
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.list import LIST
from definit_db.data.field.computer_science.definitions.fundamental.pointer import POINTER
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _HeadInsertion(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Head insertion")}, also called prepending, is an 
{OPERATION.key.get_reference(phrase="operation")} that adds an {ITEM.key.get_reference(phrase="item")} to the 
beginning of a {LIST.key.get_reference(phrase="list")}. In a {LINKED_LIST.key.get_reference(phrase="linked list")}, 
head insertion commonly creates a new {NODE.key.get_reference(phrase="node")}, points it to the previous first node, 
and updates the head {POINTER.key.get_reference(phrase="pointer")} to the new node.
"""


HEAD_INSERTION = _HeadInsertion(
    key=DefinitionKey(
        name="head insertion",
        field=FieldName.COMPUTER_SCIENCE,
    )
)