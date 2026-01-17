from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _NAryTree(Definition):
    def _get_content(self) -> str:
        return f"""
An {self.key.get_reference()} is a {TREE.key.get_reference("tree")} in which each 
{NODE.key.get_reference("node")} can have an arbitrary number of children.
"""


N_ARY_TREE = _NAryTree(
    key=DefinitionKey(
        name="n-ary tree",
        field=FieldName.MATHEMATICS,
    )
)
