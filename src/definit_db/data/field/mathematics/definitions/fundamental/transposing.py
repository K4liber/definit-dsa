from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.matrix import MATRIX
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _Transposing(Definition):
    def _get_content(self) -> str:
        return f"""
Transposing is an {OPERATION.key.get_reference(phrase="operation")} on a 
{MATRIX.key.get_reference(phrase="matrix")} that exchanges its rows and columns. For a matrix A, the 
transpose A^T has the entry at row i and column j equal to the entry at row j and column i of A. If A 
has m rows and n columns, then A^T has n rows and m columns.
"""


TRANSPOSING = _Transposing(
    key=DefinitionKey(
        name="transposing",
        field=FieldName.MATHEMATICS,
    )
)
