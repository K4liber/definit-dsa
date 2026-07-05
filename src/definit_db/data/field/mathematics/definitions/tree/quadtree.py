from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.partitioning import PARTITIONING
from definit_db.data.field.mathematics.definitions.fundamental.quadrant import QUADRANT
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Quadtree(Definition):
    def _get_content(self) -> str:
        return f"""
A quadtree is a {TREE.key.get_reference(phrase="tree")} data structure used for recursive 
{PARTITIONING.key.get_reference(phrase="partitioning")} of a two-dimensional space. Each internal 
{NODE.key.get_reference(phrase="node")} represents a region and has four children corresponding to four 
subregions, often called {QUADRANT.key.get_reference(phrase="quadrants")}.

---

A 2D area containing several points can be organized into a quadtree: the root {NODE.key.get_reference(phrase="node")}
represents the whole area. Whenever a region holds more points than a chosen limit, it is split into four equal
quadrants — northwest, northeast, southwest, and southeast — each becoming a child node, and the split repeats
within any child that still holds too many points. A search for points near a given location can then skip entire
quadrants that do not overlap the search area, instead of checking every point individually.
"""


QUADTREE = _Quadtree(
    key=DefinitionKey(
        name="quadtree",
        field=FieldName.MATHEMATICS,
    )
)
