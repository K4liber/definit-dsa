from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.fibonacci import FIBONACCI
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Recurrence(Definition):
    def _get_content(self) -> str:
        return f"""
A recurrence is an equation that defines each term of a {SEQUENCE.key.get_reference(phrase="sequence")} as a
{FUNCTION.key.get_reference(phrase="function")} of one or more earlier terms, together with one or more starting
values. It specifies a {SEQUENCE.key.get_reference()} indirectly: rather than giving a closed formula for every
term, it gives a rule that must be applied repeatedly to obtain successive values.

---

The {FIBONACCI.key.get_reference(phrase="Fibonacci")} sequence is defined by the recurrence F(n) = F(n-1) + F(n-2) with starting values
F(0) = 0 and F(1) = 1. Applying the rule repeatedly yields F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, F(6) = 8:
each {NUMBER.key.get_reference(phrase="number")} in the sequence is the sum of the two preceding numbers.
"""


RECURRENCE = _Recurrence(
    key=DefinitionKey(
        name="recurrence",
        field=FieldName.MATHEMATICS,
    )
)
