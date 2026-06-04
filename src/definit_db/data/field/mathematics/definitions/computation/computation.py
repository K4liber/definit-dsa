from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Computation(Definition):
    def _get_content(self) -> str:
        return f"""
Computation is the process of transforming {INPUT_DATA.key.get_reference("input")} into output by carrying out a
{SEQUENCE.key.get_reference()} of well-defined {INSTRUCTION.key.get_reference("instructions")} according to
fixed rules.

---

Adding two numbers by hand is a computation: starting from the {INPUT_DATA.key.get_reference("input")} 2 and 3,
you follow a {SEQUENCE.key.get_reference()} of {INSTRUCTION.key.get_reference("instructions")} (align the digits,
add them, carry if needed) to produce the output 5.
"""


COMPUTATION = _Computation(
    key=DefinitionKey(
        name="computation",
        field=FieldName.MATHEMATICS,
    )
)
