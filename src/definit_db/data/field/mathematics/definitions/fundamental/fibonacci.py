from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Fibonacci(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference("Fibonacci")} commonly refers to the Fibonacci 
{SEQUENCE.key.get_reference("sequence")} (F0, F1, F2, ...) defined by:

- F0 = 0
- F1 = 1
- Fn = Fn-1 + Fn-2 for n ≥ 2

Each term is an {INTEGER.key.get_reference("integer")}.
"""


FIBONACCI = _Fibonacci(
    key=DefinitionKey(
        name="fibonacci",
        field=FieldName.MATHEMATICS,
    )
)
