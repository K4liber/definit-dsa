from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _CommutativeOperation(Definition):
    def _get_content(self) -> str:
        return f"""
A commutative operation is an {OPERATION.key.get_reference(phrase="operation")} whose result does not depend on 
the order of its inputs. For two inputs a and b, the operation gives the same result when applied as a * b or b * a.
"""


COMMUTATIVE_OPERATION = _CommutativeOperation(
    key=DefinitionKey(
        name="commutative operation",
        field=FieldName.MATHEMATICS,
    )
)