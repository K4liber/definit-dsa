from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.reordering import REORDERING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Permutation(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {REORDERING.key.get_reference("reordering")} of the elements of a
{SEQUENCE.key.get_reference("sequence")}, i.e., the same elements arranged in a different order.
"""


PERMUTATION = _Permutation(
    key=DefinitionKey(
        name="permutation",
        field=FieldName.MATHEMATICS,
    )
)
