from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.subtree import SUBTREE


class _TreeRotation(Definition):
    def _get_content(self) -> str:
        return f"""
An {OPERATION.key.get_reference(phrase="operation")} on a {BINARY_TREE.key.get_reference(phrase="binary tree")} 
that changes the structure without disturbing the order of the {NODE.key.get_reference(phrase="nodes")}. A rotation 
moves a {NODE.key.get_reference(phrase="node")} down and brings its child up, preserving the in-order 
{SEQUENCE.key.get_reference(phrase="sequence")} of {ITEM.key.get_reference(phrase="elements")}.

---

Consider a {BINARY_TREE.key.get_reference(phrase="binary tree")} where {NODE.key.get_reference(phrase="node")} "A" 
has a right child "B". A left rotation at "A" makes "B" the new parent: "B" takes the place of "A", and "A" becomes 
the left child of "B". The in-order traversal remains unchanged — any {SUBTREE.key.get_reference(phrase="subtree")} 
that was between "A" and "B" stays between them after the rotation.
"""


TREE_ROTATION = _TreeRotation(
    key=DefinitionKey(
        name="tree_rotation",
        field=FieldName.MATHEMATICS,
    )
)
