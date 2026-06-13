from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.ancestor import ANCESTOR
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _LowestCommonAncestor(Definition):
    def _get_content(self) -> str:
        return f"""
The lowest common ancestor of two {NODE.key.get_reference(phrase="nodes")} in a 
{TREE.key.get_reference(phrase="tree")} is the deepest node that is an 
{ANCESTOR.key.get_reference(phrase="ancestor")} of both nodes. Equivalently, it is the common ancestor farthest 
from the root and closest to the two given nodes.

---

In a {TREE.key.get_reference(phrase="tree")} where "A" is the parent of "B" and "C", and "B" is the parent of "D" 
and "E", the lowest common {ANCESTOR.key.get_reference(phrase="ancestor")} of {NODE.key.get_reference(phrase="nodes")} 
"D" and "E" is "B", while the lowest common ancestor of "D" and "C" is "A".
"""


LOWEST_COMMON_ANCESTOR = _LowestCommonAncestor(
    key=DefinitionKey(
        name="lowest common ancestor",
        field=FieldName.MATHEMATICS,
    )
)