from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.intersection import INTERSECTION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.fundamental.subset import SUBSET
from definit_db.data.field.mathematics.definitions.fundamental.union import UNION


class _Partitioning(Definition):
    def _get_content(self) -> str:
        return f"""
The process of dividing a {SET.key.get_reference()} into a {COLLECTION.key.get_reference()} of
non-empty, pairwise-disjoint {SUBSET.key.get_reference("subsets")} whose {UNION.key.get_reference()} is the original 
set.

Equivalently, a partition is a set of subsets whose pairwise {INTERSECTION.key.get_reference()} is empty.

---

The {SET.key.get_reference()} (1, 2, 3, 4, 5, 6) can be partitioned into the subsets (1, 3, 5) and (2, 4, 6): both
are non-empty, their {INTERSECTION.key.get_reference()} is empty, and their {UNION.key.get_reference()} recovers
the original set.

(1, 2, 3) and (3, 4, 5, 6) would not be a valid partition of the same set, since they share the element 3 —
their intersection is not empty.
"""


PARTITIONING = _Partitioning(
    key=DefinitionKey(
        name="partitioning",
        field=FieldName.MATHEMATICS,
    )
)
