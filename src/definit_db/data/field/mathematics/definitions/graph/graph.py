from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _Graph(Definition):
    def _get_content(self) -> str:
        return f"""
Graphs are used to model pairwise {RELATION.key.get_reference(phrase="relations")} between objects. 
A graph is made up of {NODE.key.get_reference(phrase="nodes")} and {EDGE.key.get_reference(phrase="edges")}. 
Graphs can represent various types of relationships in different fields.

---

Consider three cities "A", "B", and "C", each a {NODE.key.get_reference(phrase="node")}. The roads 
"A-B" and "B-C" are {EDGE.key.get_reference(phrase="edges")}. Together these nodes and edges form a 
graph that captures the {RELATION.key.get_reference(phrase="relation")} "is connected by road to" 
across all three cities.
"""


GRAPH = _Graph(
    key=DefinitionKey(
        name="graph",
        field=FieldName.MATHEMATICS,
    )
)
