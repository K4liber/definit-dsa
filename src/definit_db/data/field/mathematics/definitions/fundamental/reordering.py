from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Reordering(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a change in the order of items in a
{SEQUENCE.key.get_reference("sequence")}, without changing which items are present.
"""


REORDERING = _Reordering(
    key=DefinitionKey(
        name="reordering",
        field=FieldName.MATHEMATICS,
    )
)
