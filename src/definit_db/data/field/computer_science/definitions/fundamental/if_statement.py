from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.control_structure import CONTROL_STRUCTURE
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _IfStatement(Definition):
    def _get_content(self) -> str:
        return f"""
A {CONTROL_STRUCTURE.key.get_reference()} that executes a block of
{INSTRUCTION.key.get_reference("instructions")} only when a given 
{BOOLEAN_EXPRESSION.key.get_reference(phrase="condition")} evaluates to true. It is the most direct way to make 
execution depend on the {PROGRAM.key.get_reference(phrase="program")}'s state or 
{INPUT_DATA.key.get_reference("input")}.

---

"If the temperature is above 30, turn on the fan" is an if-statement: the condition "temperature above 30" is
checked, and the instruction "turn on the fan" runs only when that condition holds. When the condition is false,
the instruction is skipped and execution continues with whatever follows.
"""


IF_STATEMENT = _IfStatement(
    key=DefinitionKey(
        name="if-statement",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
