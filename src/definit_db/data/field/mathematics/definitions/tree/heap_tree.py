from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _HeapTree(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {TREE.key.get_reference(phrase="tree")} data structure that satisfies the heap property: the value of 
each {NODE.key.get_reference(phrase="node")} is greater than or equal to (or less than or equal to) the values of 
its children. This property allows for efficient retrieval of the minimum (or maximum) element in the tree.

---

Arrange {NODE.key.get_reference(phrase="nodes")} in a {TREE.key.get_reference(phrase="tree")} so the root holds 
"9" with children "5" and "4", and "5" has a child "2". Every parent's value is greater than or equal to its 
children's ("9" ≥ "5" and "4"; "5" ≥ "2"), so the heap property holds and the maximum element "9" sits at the 
root, ready to be read in a single step.
"""


HEAP_TREE = _HeapTree(
    key=DefinitionKey(
        name="heap_tree",
        field=FieldName.MATHEMATICS,
    )
)
