from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _GraphDistance(Definition):
    def _get_content(self) -> str:
        return f"""
A measure of the shortest {PATH.key.get_reference(phrase="path")} between two 
{NODE.key.get_reference(phrase="nodes")} in a {GRAPH.key.get_reference(phrase="graph")}.

---

Take a {GRAPH.key.get_reference(phrase="graph")} of cities "A", "B", and "C" with the 
{EDGE.key.get_reference(phrase="edges")} "A-B", "B-C", and "A-C". The {PATH.key.get_reference(phrase="path")} 
A-B-C uses two edges, but the direct edge "A-C" uses one. The graph distance between 
{NODE.key.get_reference(phrase="nodes")} "A" and "C" is therefore 1, the length of the shortest path.
"""


GRAPH_DISTANCE = _GraphDistance(
    key=DefinitionKey(
        name="graph_distance",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("shortest path distance", "geodesic distance"),
)
