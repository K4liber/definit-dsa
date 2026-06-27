from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.graph.directed_acyclic_graph import DIRECTED_ACYCLIC_GRAPH


class _TopologicalSort(Definition):
    def _get_content(self) -> str:
        return f"""
Topological Sort is a {SORTING.key.get_reference()} {ALGORITHM.key.get_reference()} applied to a 
{DIRECTED_ACYCLIC_GRAPH.key.get_reference(phrase="directed acyclic graph")}. It produces a linear ordering 
of the graph's vertices such that for every directed edge (u, v), u comes before v in the ordering.

---

Given the {DIRECTED_ACYCLIC_GRAPH.key.get_reference(phrase="DAG")}:

  A → B → D
  A → C → D

Valid topological orderings: [A, B, C, D] or [A, C, B, D].
Both place A first (it has no dependencies) and D last (it depends on B and C).
"""


TOPOLOGICAL_SORT = _TopologicalSort(
    key=DefinitionKey(
        name="topological_sort",
        field=FieldName.MATHEMATICS,
    )
)
