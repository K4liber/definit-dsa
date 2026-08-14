from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.searching.depth_first_search import DEPTH_FIRST_SEARCH
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.directed_graph import DIRECTED_GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _CycleDetection(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
An {ALGORITHM.key.get_reference()} for determining whether a 
{GRAPH.key.get_reference()} contains a {CYCLE.key.get_reference()}. The algorithm typically uses 
{DEPTH_FIRST_SEARCH.key.get_reference("depth-first search")} to traverse the graph while tracking 
visited {NODE.key.get_reference("nodes")} and the current {PATH.key.get_reference()}. If a node is encountered 
that is already in the current path, a cycle has been detected. Different approaches are used for 
{DIRECTED_GRAPH.key.get_reference("directed")} versus undirected graphs.

---

{DIRECTED_GRAPH.key.get_reference("Directed graph")} edges: A→B, B→C, C→A

  {DEPTH_FIRST_SEARCH.key.get_reference("DFS")} from A: visit A → visit B → visit C
  → C points back to A, which is already in the current {PATH.key.get_reference()} 
  → {CYCLE.key.get_reference()} detected ✓

Removing edge C→A (edges: A→B, B→C): DFS completes without revisiting any {NODE.key.get_reference("node")} 
  → no {CYCLE.key.get_reference()} ✓
"""


CYCLE_DETECTION = _CycleDetection(DefinitionKey(name="cycle detection", field=FieldName.MATHEMATICS))
