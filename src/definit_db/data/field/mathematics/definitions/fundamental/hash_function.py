from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.hash import HASH
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _HashFunction(Definition):
    def _get_content(self) -> str:
        return f"""
A {FUNCTION.key.get_reference(phrase="function")} that maps an input {OBJECT.key.get_reference(phrase="object")}
of arbitrary size to a {HASH.key.get_reference(phrase="hash")} (or 'digest') of fixed size.
A good hash function makes it unlikely that two different inputs produce the same digest, but such collisions
are still possible.

---

A {FUNCTION.key.get_reference(phrase="function")} that returns the remainder of an
{INTEGER.key.get_reference(phrase="integer")} divided by 10 is a simple hash function: it maps any
{INTEGER.key.get_reference(phrase="integer")} to a fixed-size digest between 0 and 9.
For instance, 27 maps to 7 and 42 maps to 2. Because only ten digests exist, different inputs such as 7 and 17
map to the same digest.
"""


HASH_FUNCTION = _HashFunction(
    key=DefinitionKey(
        name="hash_function",
        field=FieldName.MATHEMATICS,
    )
)
