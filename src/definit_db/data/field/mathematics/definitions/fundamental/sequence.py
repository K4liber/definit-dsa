from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Sequence(Definition):
    def _get_content(self) -> str:
        return f"""
A collection of {OBJECT.key.get_reference(phrase="objects")} in which repetitions are allowed and order 
matters.

---

The sequence (3, 3, 5) lists three {OBJECT.key.get_reference(phrase="objects")} where order matters,
so it is different from the sequence (5, 3, 3).
"""


SEQUENCE = _Sequence(
    key=DefinitionKey(
        name="sequence",
        field=FieldName.MATHEMATICS,
    )
)
