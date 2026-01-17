from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.intersection import INTERSECTION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.fundamental.union import UNION


class _VennDiagram(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference(phrase="Venn diagram")} is a diagram that represents one or more
{SET.key.get_reference(phrase="sets")} as overlapping regions (often circles) to visualize their relationships.

In particular, it can illustrate set operations such as {UNION.key.get_reference(phrase="union")} and
{INTERSECTION.key.get_reference(phrase="intersection")}.
"""


VENN_DIAGRAM = _VennDiagram(
    key=DefinitionKey(
        name="Venn diagram",
        field=FieldName.MATHEMATICS,
    )
)
