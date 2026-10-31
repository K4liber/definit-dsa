from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.parent import PARENT
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Child(Definition):
    def _get_content(self) -> str:
        return f"""
In a {TREE.key.get_reference(phrase="tree")}, a child of a {NODE.key.get_reference(phrase="node")} is a node 
that lies directly below it: a node whose {PARENT.key.get_reference(phrase="parent")} is that node. A node can 
have zero or more children, and every node except the root is a child of exactly one node.

---

In a {TREE.key.get_reference(phrase="tree")} where "A" branches to "B" and "C", and "B" branches to "D", the 
children of "A" are "B" and "C", the children of "B" consist of the single node "D", and "C" has no children.
"""


CHILD = _Child(
    key=DefinitionKey(
        name="child",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["child node"],
)
