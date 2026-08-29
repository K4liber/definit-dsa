from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.operand import OPERAND
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _ReversePolishNotation(Definition):
    def _get_content(self) -> str:
        return f"""
Reverse Polish notation, also called postfix notation, is a way of writing a {SEQUENCE.key.get_reference()} of
{OPERAND.key.get_reference(phrase="operands")} and {OPERATION.key.get_reference(phrase="operations")} so that
each operation appears after the operands it applies to.

---

The expression "3 4 +" is written in Reverse Polish notation. It means applying the addition
{OPERATION.key.get_reference(phrase="operation")} to the {OPERAND.key.get_reference(phrase="operands")} 3 and 4,
which gives 7.
"""


REVERSE_POLISH_NOTATION = _ReversePolishNotation(
    key=DefinitionKey(
        name="Reverse Polish notation",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["RPN", "postfix notation"],
)
