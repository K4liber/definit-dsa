from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.intersection import INTERSECTION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.fundamental.union import UNION


class _VennDiagram(Definition):
    def _get_content(self) -> str:
        return f"""
A diagram that represents one or more
{SET.key.get_reference(phrase="sets")} as overlapping regions (often circles) to visualize their relationships.

In particular, it can illustrate set operations such as {UNION.key.get_reference(phrase="union")} and
{INTERSECTION.key.get_reference(phrase="intersection")}.

---

For {SET.key.get_reference(phrase="sets")} A = (1, 2, 3) and B = (2, 3, 4), a Venn diagram draws A and B as two
overlapping circles. The overlapping region represents their {INTERSECTION.key.get_reference(phrase="intersection")}
(2, 3), while the entire area covered by both circles together represents their
{UNION.key.get_reference(phrase="union")} (1, 2, 3, 4).
"""


VENN_DIAGRAM = _VennDiagram(
    key=DefinitionKey(
        name="Venn diagram",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["set diagram"],
)
