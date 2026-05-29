from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.tree.root import ROOT
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Ancestor(Definition):
    def _get_content(self) -> str:
        return f"""
In a {TREE.key.get_reference(phrase="tree")}, an ancestor of a {NODE.key.get_reference(phrase="node")} is any 
node on the {PATH.key.get_reference(phrase="path")} from the {ROOT.key.get_reference(phrase="root")} to that node. 
Depending on convention, the node itself may also be considered its own ancestor.
"""


ANCESTOR = _Ancestor(
    key=DefinitionKey(
        name="ancestor",
        field=FieldName.MATHEMATICS,
    )
)