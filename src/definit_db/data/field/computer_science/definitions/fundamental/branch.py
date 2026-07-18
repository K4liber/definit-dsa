from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.if_statement import IF_STATEMENT
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.graph.path import PATH


class _Branch(Definition):
    def _get_content(self) -> str:
        return f"""
A branch is one possible {PATH.key.get_reference("path")} of execution in a
{PROGRAM.key.get_reference("program")}, typically chosen by evaluating a 
{BOOLEAN_EXPRESSION.key.get_reference(phrase="condition")}.

---

An {IF_STATEMENT.key.get_reference()} creates two branches: one taken when the condition is true, the other when it is false. Each
branch holds its own sequence of {INSTRUCTION.key.get_reference("instructions")}, and exactly one of the two
sequences runs on any given execution — the choice between them is what makes the program's behavior depend on
its input.
"""


BRANCH = _Branch(
    key=DefinitionKey(
        name="branch",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
