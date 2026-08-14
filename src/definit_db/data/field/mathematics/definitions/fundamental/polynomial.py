from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.expression import EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _Polynomial(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A mathematical {EXPRESSION.key.get_reference()} consisting of variables and coefficients, 
involving only the {OPERATION.key.get_reference("operations")} of addition, subtraction, multiplication, 
and non-negative {INTEGER.key.get_reference("integer")} exponentiation of variables. 
A type of {FUNCTION.key.get_reference()} that can be written in the form 
a_n*x^n + a_(n-1)*x^(n-1) + ... + a_1*x + a_0, where the coefficients a_i are constants and n is a 
non-negative {INTEGER.key.get_reference("integer")} called the degree of the polynomial.

---

3x² + 2x - 5 is a polynomial of degree 2, with coefficients a_2=3, a_1=2, a_0=-5.

Evaluating it at x=4 using the {OPERATION.key.get_reference("operations")} of the definition:

  3(4²) + 2(4) - 5 = 3(16) + 8 - 5 = 48 + 8 - 5 = 51

Non-example: 3/x is not a polynomial because the exponent of x is -1,
which is not a non-negative {INTEGER.key.get_reference("integer")}.
"""


POLYNOMIAL = _Polynomial(DefinitionKey(name="polynomial", field=FieldName.MATHEMATICS))
