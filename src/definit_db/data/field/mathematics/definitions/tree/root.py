from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Root(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} of a {TREE.key.get_reference("tree")} is the unique 
{NODE.key.get_reference("node")} with no parent.
"""


ROOT = _Root(
    key=DefinitionKey(
        name="root",
        field=FieldName.MATHEMATICS,
    )
)
