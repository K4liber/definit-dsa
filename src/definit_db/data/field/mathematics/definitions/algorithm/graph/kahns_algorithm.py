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

---

Given the {DIRECTED_ACYCLIC_GRAPH.key.get_reference(phrase="DAG")} A→B→D, A→C→D:

{IN_DEGREE.key.get_reference(phrase="In-degrees")}: A=0, B=1, C=1, D=2

Step 1: Pick A (in-degree 0) → remove {EDGE.key.get_reference(phrase="edges")} A→B, A→C → in-degrees: B=0, C=0, D=2

Step 2: Pick B (in-degree 0) → remove {EDGE.key.get_reference(phrase="edge")} B→D → in-degrees: C=0, D=1

Step 3: Pick C (in-degree 0) → remove {EDGE.key.get_reference(phrase="edge")} C→D → in-degrees: D=0

Step 4: Pick D (in-degree 0) → done

Result: [A, B, C, D] ✓
"""


KAHNS_ALGORITHM = _KahnsAlgorithm(
    key=DefinitionKey(
        name="Kahn's Algorithm",
        field=FieldName.MATHEMATICS,
    )
)
