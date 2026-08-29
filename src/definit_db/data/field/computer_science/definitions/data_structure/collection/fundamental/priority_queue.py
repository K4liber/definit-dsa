from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.queue import QUEUE
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.abstract_data_type import (
    ABSTRACT_DATA_TYPE,
)
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.first_in_first_out import FIRST_IN_FIRST_OUT
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _PriorityQueue(Definition):
    def _get_content(self) -> str:
        return f"""
A priority queue is an {ABSTRACT_DATA_TYPE.key.get_reference(phrase="abstract data type")} that 
{OPERATION.key.get_reference(phrase="operates")} similarly 
to a regular {QUEUE.key.get_reference(phrase="queue")} but with an added feature: each 
{ITEM.key.get_reference(phrase="element")} in the priority queue has a 'priority' associated with it. 
{ITEM.key.get_reference(phrase="Elements")} with higher priority are served before 
{ITEM.key.get_reference(phrase="elements")} with lower priority. 
If two {ITEM.key.get_reference(phrase="elements")} have the same priority, they are served according to their 
{FIRST_IN_FIRST_OUT.key.get_reference()} order.

---

Suppose four tasks arrive in order A (priority 1), B (priority 3), C (priority 3), D (priority 2), where a higher 
{NUMBER.key.get_reference(phrase="number")} means higher priority. They are served in the order B, C, D, A: B and C 
share the highest priority, so they are served in the order they arrived; then D; finally A, the lowest priority, 
is served last.
"""


PRIORITY_QUEUE = _PriorityQueue(
    key=DefinitionKey(
        name="priority_queue",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=["PQ", "heap"],
)
