from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _Operand(Definition):
    def _get_content(self) -> str:
        return f"""
An {OBJECT.key.get_reference()} that an {OPERATION.key.get_reference()} is applied to.

---

In the expression 2 + 3, the {OBJECT.key.get_reference(phrase="objects")} 2 and 3 are the operands of the
addition.
"""


OPERAND = _Operand(
    key=DefinitionKey(
        name="operand",
        field=FieldName.MATHEMATICS,
    )
)
