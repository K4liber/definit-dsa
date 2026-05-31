from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.operand import OPERAND
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _CommutativeOperation(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is an {OPERATION.key.get_reference(phrase="operation")} whose result does not 
depend on the order of its {OPERAND.key.get_reference(phrase="operands")}.

---

Addition is commutative: 2 + 3 and 3 + 2 both give the same result, 5.
"""


COMMUTATIVE_OPERATION = _CommutativeOperation(
    key=DefinitionKey(
        name="commutative operation",
        field=FieldName.MATHEMATICS,
    )
)