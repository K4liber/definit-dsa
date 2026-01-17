from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.intersection import INTERSECTION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _MutualExclusivity(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference("Mutual exclusivity")} means that two events cannot occur at the same time.

In set terms, two {SET.key.get_reference(phrase="sets")} A and B are mutually exclusive if their
{INTERSECTION.key.get_reference()} is empty.
"""


MUTUAL_EXCLUSIVITY = _MutualExclusivity(
    key=DefinitionKey(
        name="mutual exclusivity",
        field=FieldName.MATHEMATICS,
    )
)
