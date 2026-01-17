from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.matrix import MATRIX
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _AdjacencyMatrix(Definition):
    def _get_content(self) -> str:
        return f"""
An {self.key.get_reference()} is a way of representing a {GRAPH.key.get_reference(phrase="graph")} as a 
{MATRIX.key.get_reference(phrase="matrix")}.

If the rows and columns correspond to the {NODE.key.get_reference(phrase="nodes")} of the graph, then the 
entry in row i, column j indicates whether there is an {EDGE.key.get_reference(phrase="edge")} from node i to node j.
"""


ADJACENCY_MATRIX = _AdjacencyMatrix(
    key=DefinitionKey(
        name="adjacency matrix",
        field=FieldName.MATHEMATICS,
    )
)
