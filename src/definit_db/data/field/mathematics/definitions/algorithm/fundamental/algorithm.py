from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.finite_sequence import FINITE_SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _Algorithm(Definition):
    def _get_content(self) -> str:
        return f"""
A {FINITE_SEQUENCE.key.get_reference(phrase="finite sequence")} of mathematically rigorous 
{INSTRUCTION.key.get_reference(phrase="instructions")}, typically used to solve a 
{PROBLEM.key.get_reference(phrase="problem")}.

---

To solve the {PROBLEM.key.get_reference(phrase="problem")} of finding the larger of the two 
{NUMBER.key.get_reference(phrase="numbers")} "3" and "5", an algorithm is the finite sequence of 
{INSTRUCTION.key.get_reference(phrase="instructions")}: "compare "3" and "5"", then "return the larger value", 
which yields "5".
"""


ALGORITHM = _Algorithm(
    key=DefinitionKey(
        name="algorithm",
        field=FieldName.MATHEMATICS,
    )
)
