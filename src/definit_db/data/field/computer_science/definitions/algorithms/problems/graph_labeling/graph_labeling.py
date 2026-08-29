from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.primitive.integer import INTEGER
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.notations.label import LABEL
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _GraphLabeling(Definition):
    def _get_content(self) -> str:
        return f"""
A {PROBLEM.key.get_reference()} of assigning {LABEL.key.get_reference(phrase="labels")}, traditionally 
represented by {INTEGER.key.get_reference(phrase="integers")}, to {EDGE.key.get_reference(phrase="edges")} and/or 
{NODE.key.get_reference(phrase="nodes")} of a {GRAPH.key.get_reference(phrase="graph")}.

---

In a {GRAPH.key.get_reference(phrase="graph")} with three {NODE.key.get_reference(phrase="nodes")} connected in a 
triangle, one labeling assigns the integer 1 to the first node, 2 to the second, and 3 to the third, while another 
assigns 0, 0, and 1. Each assignment is a valid labeling; whether it satisfies a given rule depends on the specific 
problem, such as requiring adjacent nodes to receive different labels.
"""


GRAPH_LABELING = _GraphLabeling(
    key=DefinitionKey(
        name="graph_labeling",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=("graph labelling",),
)
