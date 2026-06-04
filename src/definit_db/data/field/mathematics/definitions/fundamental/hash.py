from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Hash(Definition):
    def _get_content(self) -> str:
        return f"""
A hash (also called a 'digest') is a fixed-size value used as a compact representation of an
{OBJECT.key.get_reference(phrase="object")} of arbitrary size.

---

The short code "a1b2c3" could serve as a hash of a long document: it is a small, fixed-size value standing in
for a much larger {OBJECT.key.get_reference(phrase="object")}.
Because the hash is much smaller than the document, two different documents may share the same hash.
"""


HASH = _Hash(
    key=DefinitionKey(
        name="hash",
        field=FieldName.MATHEMATICS,
    )
)
