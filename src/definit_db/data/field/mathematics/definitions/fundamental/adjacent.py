from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Adjacent(Definition):
    def _get_content(self) -> str:
        return f"""
Two {OBJECT.key.get_reference(phrase="objects")} are adjacent when they are next to each other according to
some ordering, position, or direct connection. Adjacency is most common for neighboring elements in a
{SEQUENCE.key.get_reference()}.

---

In the sequence [a, b, c, d], the element "b" is adjacent to "a" and "c", but not to "d".
"""


ADJACENT = _Adjacent(
    key=DefinitionKey(
        name="adjacent",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("neighboring",),
)
