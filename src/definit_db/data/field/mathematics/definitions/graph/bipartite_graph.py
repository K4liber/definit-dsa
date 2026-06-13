from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _BipartiteGraph(Definition):
    def _get_content(self) -> str:
        return f"""
A {GRAPH.key.get_reference(phrase="graph")} whose {NODE.key.get_reference(phrase="nodes")} can be divided into 
two disjoint {SET.key.get_reference(phrase="sets")} such that every {EDGE.key.get_reference(phrase="edge")} 
connects a node in one set to a node in the other set. In other words, there are no edges connecting nodes 
within the same set.

---

Consider students "S1", "S2" and clubs "C1", "C2", each a {NODE.key.get_reference(phrase="node")}. 
Put the students in one {SET.key.get_reference(phrase="set")} and the clubs in another. Every 
{EDGE.key.get_reference(phrase="edge")} links a student to a club they belong to (for example "S1-C1" 
and "S2-C1"), and never one student to another. This {GRAPH.key.get_reference(phrase="graph")} is bipartite.
"""


BIPARTITE_GRAPH = _BipartiteGraph(
    key=DefinitionKey(
        name="bipartite_graph",
        field=FieldName.MATHEMATICS,
    )
)
