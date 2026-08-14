from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.palindrome import PALINDROME
from definit_db.data.field.mathematics.definitions.fundamental.reflection import REFLECTION
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.fundamental.rotation import ROTATION
from definit_db.data.field.mathematics.definitions.fundamental.transformation import TRANSFORMATION


class _Symmetry(Definition):
    def _get_content(self) -> str:
        return f"""
Symmetry is a {RELATION.key.get_reference(phrase="relation")} between an 
{OBJECT.key.get_reference(phrase="object")} and an {OPERATION.key.get_reference(phrase="operation")} where applying 
the operation leaves the object unchanged in the aspects being considered. A symmetric object therefore has a 
form or behavior that is preserved under some {TRANSFORMATION.key.get_reference(phrase="transformation")}, such as 
{REFLECTION.key.get_reference(phrase="reflection")}, {ROTATION.key.get_reference(phrase="rotation")}, or exchange 
of parts.

---

A {PALINDROME.key.get_reference(phrase="palindrome")} exhibits symmetry under the operation of reversal:
reversing the sequence (1, 2, 3, 2, 1) leaves it unchanged. In contrast, reversing the sequence (1, 2, 3)
yields (3, 2, 1), which is different from the original, so this sequence does not exhibit symmetry under
reversal.
"""


SYMMETRY = _Symmetry(
    key=DefinitionKey(
        name="symmetry",
        field=FieldName.MATHEMATICS,
    )
)
