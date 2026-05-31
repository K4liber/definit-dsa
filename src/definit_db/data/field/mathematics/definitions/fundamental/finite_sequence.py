from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _FiniteSequence(Definition):
    def _get_content(self) -> str:
        return f"""
A {SEQUENCE.key.get_reference(phrase="sequence")} that has a finite number of 
{OBJECT.key.get_reference(phrase="objects")}. Informally, a finite sequence is a sequence which one could in 
principle count and finish counting.

---

(2, 4, 6, 8, 10) is a finite sequence with five elements.
"""


FINITE_SEQUENCE = _FiniteSequence(
    key=DefinitionKey(
        name="finite_sequence",
        field=FieldName.MATHEMATICS,
    )
)
