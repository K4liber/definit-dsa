from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Root(Definition):
    def _get_content(self) -> str:
        return f"""
The root of a {TREE.key.get_reference("tree")} is the {UNIQUENESS.key.get_reference(phrase="unique")} 
{NODE.key.get_reference("node")} with no parent.

---

In a {TREE.key.get_reference("tree")} where {NODE.key.get_reference("node")} "A" is the parent of "B" 
and "C", and "B" is the parent of "D", only "A" has no parent. "A" is therefore the root of the tree.
"""


ROOT = _Root(
    key=DefinitionKey(
        name="root",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["root node"],
)
