from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.root import ROOT
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Parent(Definition):
    def _get_content(self) -> str:
        return f"""
In a {TREE.key.get_reference(phrase="tree")}, the parent of a {NODE.key.get_reference(phrase="node")} is the 
{UNIQUENESS.key.get_reference(phrase="unique")} node that lies directly above it: the single node from which it 
can be reached by following exactly one {EDGE.key.get_reference(phrase="edge")} upward toward the 
{ROOT.key.get_reference(phrase="root")}. Each node has at most one parent, and only the root has none.

---

In a {TREE.key.get_reference(phrase="tree")} where "A" branches to "B" and "C", and "B" branches to "D", the 
parent of "D" is "B", the parent of "B" is "A", and the parent of "C" is also "A". 
"""


PARENT = _Parent(
    key=DefinitionKey(
        name="parent",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["parent node"],
)
