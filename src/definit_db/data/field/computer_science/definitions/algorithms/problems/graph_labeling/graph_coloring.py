from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.graph_labeling import (
    GRAPH_LABELING,
)
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.notations.label import LABEL
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION


class _GraphColoring(Definition):
    def _get_content(self) -> str:
        return f"""
A special case of {GRAPH_LABELING.key.get_reference(phrase="graph labeling")} where the 
{LABEL.key.get_reference(phrase="labels")} are colors. The specific rule that the colors must satisfy — such as 
requiring connected {ITEM.key.get_reference("elements")} to differ — defines the particular variant of the 
{PROBLEM.key.get_reference(phrase="problem")}.

---

Assigning the colors red, green, and blue to the three {NODE.key.get_reference(phrase="nodes")} of a triangle gives 
a coloring. Whether it is a valid {SOLUTION.key.get_reference(phrase="solution")} depends on the rule: one variant may 
require that any two nodes joined by an {EDGE.key.get_reference(phrase="edge")} receive different colors, while another 
may impose no such {CONSTRAINT.key.get_reference(phrase="constraint")}.
"""


GRAPH_COLORING = _GraphColoring(
    key=DefinitionKey(
        name="graph_coloring",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
