from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.intersection import INTERSECTION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.fundamental.union import UNION


class _Partitioning(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the process of dividing a {SET.key.get_reference()} into a collection of
non-empty, pairwise-disjoint subsets whose {UNION.key.get_reference()} is the original set.

Equivalently, a partition is a set of subsets whose pairwise {INTERSECTION.key.get_reference()} is empty.
"""


PARTITIONING = _Partitioning(
    key=DefinitionKey(
        name="partitioning",
        field=FieldName.MATHEMATICS,
    )
)
