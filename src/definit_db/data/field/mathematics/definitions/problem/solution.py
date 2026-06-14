from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _Solution(Definition):
    def _get_content(self) -> str:
        return f"""
An answer to a {PROBLEM.key.get_reference(phrase="problem")} — a value, or a 
{SEQUENCE.key.get_reference(phrase="sequence")} of values, that the problem asks one to find. A solution states 
what satisfies the problem, independent of the method used to arrive at it.

---

The {PROBLEM.key.get_reference(phrase="problem")} "find a {NUMBER.key.get_reference(phrase="number")} that, when 
multiplied by itself, equals 9" has the solution "3", since "3" multiplied by "3" equals 9.
"""


SOLUTION = _Solution(
    key=DefinitionKey(
        name="solution",
        field=FieldName.MATHEMATICS,
    )
)
