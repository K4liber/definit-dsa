from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.axis import AXIS
from definit_db.data.field.mathematics.definitions.fundamental.cartesian_plane import CARTESIAN_PLANE
from definit_db.data.field.mathematics.definitions.fundamental.partitioning import PARTITIONING
from definit_db.data.field.mathematics.definitions.fundamental.plane import PLANE


class _Quadrant(Definition):
    def _get_content(self) -> str:
        return f"""
A quadrant is one of the four regions produced by dividing a two-dimensional {PLANE.key.get_reference()} with two
perpendicular lines (typically the horizontal and vertical {AXIS.key.get_reference(phrase="axes")} through a
common center). The four resulting
regions together form a {PARTITIONING.key.get_reference(phrase="partition")} of the original plane: they are
non-overlapping and cover it completely.

---

In the {CARTESIAN_PLANE.key.get_reference(phrase="Cartesian plane")}, the x-axis and y-axis divide the plane into four 
quadrants labeled I, II, III, and IV. Point (3, 4) lies in quadrant I (positive x, positive y), while point (-3, 4) 
lies in quadrant II (negative x, positive y). A square image can also be split into four equal quadrants — northwest, 
northeast, southwest, and southeast — which is the spatial layout a quadtree uses for its child regions.
"""


QUADRANT = _Quadrant(
    key=DefinitionKey(
        name="quadrant",
        field=FieldName.MATHEMATICS,
    )
)
