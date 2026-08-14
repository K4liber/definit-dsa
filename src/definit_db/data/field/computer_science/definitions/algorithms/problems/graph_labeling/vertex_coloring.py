from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.graph_coloring import (
    GRAPH_COLORING,
)
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _VertexColoring(Definition):
    def _get_content(self) -> str:
        return f"""
A specific type of {GRAPH_COLORING.key.get_reference(phrase="graph coloring")} where the goal is to ensure that 
no two {NODE.key.get_reference(phrase="nodes")} joined by an {EDGE.key.get_reference(phrase="edge")} share the same 
color.

---

In a triangle with {NODE.key.get_reference(phrase="nodes")} A, B, and C, each pair is joined by an 
{EDGE.key.get_reference(phrase="edge")}, so all three need different colors: A red, B green, C blue. In a path 
A-B-C, only A-B and B-C are joined by edges, so A and C can share a color: A red, B green, C red.
"""


VERTEX_COLORING = _VertexColoring(
    key=DefinitionKey(
        name="vertex_coloring",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
