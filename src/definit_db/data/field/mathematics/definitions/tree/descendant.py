from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.ancestor import ANCESTOR
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Descendant(Definition):
    def _get_content(self) -> str:
        return f"""
In a {TREE.key.get_reference(phrase="tree")}, a descendant of a {NODE.key.get_reference(phrase="node")} is any 
node that can be reached by repeatedly moving from that node to one of its children. Equivalently, a node is a 
descendant of another node exactly when that other node is its {ANCESTOR.key.get_reference(phrase="ancestor")}.

---

In a {TREE.key.get_reference(phrase="tree")} where "A" is the parent of "B" and "C", and "B" is the parent of "D" 
and "E", the descendants of {NODE.key.get_reference(phrase="node")} "A" are "B", "C", "D", and "E", while the 
descendants of "B" are "D" and "E".
"""


DESCENDANT = _Descendant(
    key=DefinitionKey(
        name="descendant",
        field=FieldName.MATHEMATICS,
    )
)
