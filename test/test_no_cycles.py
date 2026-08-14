from definit_db.serialize import _FIELDS  # type: ignore
from definit_db.serialize import get_field_index
from definit_db.serialize import topological_sort


def test_definition_references_are_acyclic() -> None:
    """Fail fast if the definitions cannot form a DAG.

    Every definition may only reference lower-level definitions, so the reference graph must be
    acyclic. This uses Kahn's algorithm via ``topological_sort`` (O(V + E)) directly on the
    in-memory definitions, so it detects cycles in milliseconds without the expensive
    ``serialize`` + ``get_dag`` round-trip used by ``test_generate_and_load``.

    If a cycle is introduced, ``topological_sort`` raises ``ValueError`` listing the definitions
    that take part in the cycle, making the offending references easy to find.
    """
    definitions = [definition for field in _FIELDS for definition in get_field_index(field)]

    # Raises ValueError listing the offending definitions if a cycle exists.
    ordered = topological_sort(definitions=definitions)

    assert len(ordered) == len(definitions)
