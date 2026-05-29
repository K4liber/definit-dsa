from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.partitioning import PARTITIONING
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Quadtree(Definition):
    def _get_content(self) -> str:
        return f"""
A quadtree is a {TREE.key.get_reference(phrase="tree")} data structure used for recursive 
{PARTITIONING.key.get_reference(phrase="partitioning")} of a two-dimensional space. Each internal 
{NODE.key.get_reference(phrase="node")} represents a region and has four children corresponding to four 
subregions, often called quadrants.
"""


QUADTREE = _Quadtree(
    key=DefinitionKey(
        name="quadtree",
        field=FieldName.MATHEMATICS,
    )
)