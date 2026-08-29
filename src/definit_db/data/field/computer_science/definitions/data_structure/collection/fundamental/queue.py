from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.first_in_first_out import FIRST_IN_FIRST_OUT
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM


class _Queue(Definition):
    def _get_content(self) -> str:
        return f"""
Queue is a {DATA_STRUCTURE.key.get_reference(phrase="data structure")} providing 
{FIRST_IN_FIRST_OUT.key.get_reference()} semantics. Serves as a {COLLECTION.key.get_reference(phrase="collection")} 
of {ITEM.key.get_reference(phrase="elements")} with two main {OPERATION.key.get_reference(phrase="operations")}:

- Enqueue, which adds an {ITEM.key.get_reference(phrase="element")} to the rear of the queue, and

- Dequeue, which removes an {ITEM.key.get_reference(phrase="element")} from the front.

Additionally, a peek {OPERATION.key.get_reference(phrase="operation")} can, without modifying the queue, return 
the value of the next {ITEM.key.get_reference(phrase="element")} to be dequeued without dequeuing it.

---

Starting empty, enqueueing A, then B, then C places them in the queue in that order. The first dequeue removes A, 
the {ITEM.key.get_reference(phrase="element")} added earliest; the next removes B; the last removes C. The 
{ITEM.key.get_reference(phrase="element")} that has waited longest is always the one removed next.
"""


QUEUE = _Queue(
    key=DefinitionKey(
        name="queue",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=["FIFO queue"],
)
