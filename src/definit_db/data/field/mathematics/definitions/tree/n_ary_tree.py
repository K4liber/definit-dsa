from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _NAryTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {TREE.key.get_reference("tree")} in which each 
{NODE.key.get_reference("node")} has no more than n children.

---

Fix n = 3 and build a {TREE.key.get_reference("tree")} where no {NODE.key.get_reference("node")} 
may have more than three children: "A" has children "B", "C", "D", and "B" has a single child "E". 
Every node stays within the limit of three children, so this is an n-ary tree with n = 3.
"""


N_ARY_TREE = _NAryTree(
    key=DefinitionKey(
        name="n-ary tree",
        field=FieldName.MATHEMATICS,
    )
)
