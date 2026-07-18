from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _WeightedGraph(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {GRAPH.key.get_reference()} in which each {EDGE.key.get_reference()} 
has an associated {NUMBER.key.get_reference(phrase="numerical value")} called a weight. The weight typically 
represents a cost, distance, capacity, or other metric relevant to the problem being modeled. Weighted graphs 
are used in many algorithms where the {RELATION.key.get_reference("relationship")} between nodes has varying 
significance or cost.

---

Take a {GRAPH.key.get_reference()} of cities "A", "B", and "C" with the 
{EDGE.key.get_reference(phrase="edges")} "A-B" and "B-C". Label "A-B" with the 
{NUMBER.key.get_reference(phrase="number")} 5 and "B-C" with 3 to represent the kilometers between the 
{NODE.key.get_reference(phrase="nodes")}. These weights make it a weighted graph, so traveling A-B-C costs 
5 + 3 = 8 kilometers.
"""


WEIGHTED_GRAPH = _WeightedGraph(DefinitionKey(name="weighted graph", field=FieldName.MATHEMATICS))
