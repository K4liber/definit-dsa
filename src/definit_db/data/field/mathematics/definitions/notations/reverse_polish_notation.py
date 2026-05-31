from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _ReversePolishNotation(Definition):
    def _get_content(self) -> str:
        return f"""
Reverse Polish notation, also called postfix notation, is a way of writing a {SEQUENCE.key.get_reference()} of 
operands and {OPERATION.key.get_reference(phrase="operations")} so that each operation appears after the operands 
it applies to. For example, the expression "3 4 +" means applying addition to 3 and 4.
"""


REVERSE_POLISH_NOTATION = _ReversePolishNotation(
    key=DefinitionKey(
        name="Reverse Polish notation",
        field=FieldName.MATHEMATICS,
    )
)
