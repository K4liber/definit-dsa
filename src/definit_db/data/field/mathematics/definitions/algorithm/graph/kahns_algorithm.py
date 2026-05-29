from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.topological_sort import TOPOLOGICAL_SORT
from definit_db.data.field.mathematics.definitions.graph.directed_acyclic_graph import DIRECTED_ACYCLIC_GRAPH
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.in_degree import IN_DEGREE
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _KahnsAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
Kahn's Algorithm is an {ALGORITHM.key.get_reference(phrase="algorithm")} for 
{TOPOLOGICAL_SORT.key.get_reference(phrase="topological sorting")} a 
{DIRECTED_ACYCLIC_GRAPH.key.get_reference(phrase="directed acyclic graph")}. It repeatedly chooses a 
{NODE.key.get_reference(phrase="node")} with {IN_DEGREE.key.get_reference(phrase="in-degree")} zero, appends it 
to the ordering, and removes its outgoing {EDGE.key.get_reference(phrase="edges")}. If every node is removed, the 
result is a topological ordering.
"""


KAHNS_ALGORITHM = _KahnsAlgorithm(
    key=DefinitionKey(
        name="Kahn's Algorithm",
        field=FieldName.MATHEMATICS,
    )
)