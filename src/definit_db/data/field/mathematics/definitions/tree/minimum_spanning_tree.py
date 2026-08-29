from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.weighted_graph import WEIGHTED_GRAPH
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _MinimumSpanningTree(Definition):
    def _get_content(self) -> str:
        return f"""
A {TREE.key.get_reference(phrase="tree")} that connects all the {NODE.key.get_reference(phrase="nodes")} in a 
{WEIGHTED_GRAPH.key.get_reference(phrase="weighted graph")} with the minimum possible total 
{EDGE.key.get_reference(phrase="edge")} weight. In other words, it is a subset of the edges of the 
{GRAPH.key.get_reference(phrase="graph")} that forms a tree and includes every node, such 
that the sum of the weights of the edges is minimized.

---

Consider a {WEIGHTED_GRAPH.key.get_reference(phrase="weighted graph")} of three cities "A", "B", and "C", where 
the road A-B has weight 1, B-C has weight 2, and A-C has weight 4. The minimum spanning 
{TREE.key.get_reference(phrase="tree")} connects all three cities using roads A-B and B-C (total weight 3), since 
including A-C instead would give a larger total {EDGE.key.get_reference(phrase="edge")} weight.
"""


MINIMUM_SPANNING_TREE = _MinimumSpanningTree(
    key=DefinitionKey(
        name="minimum_spanning_tree",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["MST"],
)
