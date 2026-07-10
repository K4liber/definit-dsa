from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.queue import QUEUE
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.last_in_first_out import LAST_IN_FIRST_OUT
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Stack(Definition):
    def _get_content(self) -> str:
        return f"""
Stack is a {DATA_STRUCTURE.key.get_reference(phrase="data structure")} providing 
{LAST_IN_FIRST_OUT.key.get_reference()} semantics; also called a LIFO 
{QUEUE.key.get_reference(phrase="queue")}. Serves as a {COLLECTION.key.get_reference(phrase="collection")} 
of elements with two main {OPERATION.key.get_reference(phrase="operations")}:
- Push, which adds an element to the collection, and
- Pop, which removes the most recently added element.
Additionally, a peek {OPERATION.key.get_reference(phrase="operation")} can, without modifying the stack, return 
the value of the last element added. The name stack is an analogy to a {SET.key.get_reference(phrase="set")} of 
physical items stacked one atop another, such as a stack of plates.

---

Starting empty, pushing A, then B, then C places C on top. The first pop removes C, the most recently added element; 
the next removes B; the last removes A. The element added last is always the one removed next.
"""


STACK = _Stack(
    key=DefinitionKey(
        name="stack",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
