from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.graph.directed_acyclic_graph import DIRECTED_ACYCLIC_GRAPH
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.node import NODE


class _TopologicalSort(Definition):
    def _get_content(self) -> str:
        return f"""
Topological Sort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} applied to a 
{DIRECTED_ACYCLIC_GRAPH.key.get_reference(phrase="directed acyclic graph")}. It produces a linear ordering 
of the graph's {NODE.key.get_reference("nodes")} such that for every 
{EDGE.key.get_reference(phrase="directed edge")} (u, v), u comes before v in the ordering.

---

Given a {DIRECTED_ACYCLIC_GRAPH.key.get_reference(phrase="DAG")} with {NODE.key.get_reference("nodes")} 
A, B, C, D and {EDGE.key.get_reference("edges")} A→B, A→C, B→D, C→D:

One valid topological ordering is [A, B, C, D].

Another valid topological ordering is [A, C, B, D].

Both place A first (it has no incoming edge) and D last (it depends on both B and C).
"""


TOPOLOGICAL_SORT = _TopologicalSort(
    key=DefinitionKey(
        name="topological_sort",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["topological ordering", "topsort"],
)
