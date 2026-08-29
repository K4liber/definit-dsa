from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _ProgrammingLanguage(Definition):
    def _get_content(self) -> str:
        return f"""
A formal system of syntax and vocabulary used to write 
{PROGRAM.key.get_reference("programs")} as text. It defines which 
{SEQUENCE.key.get_reference("sequences")} of {INSTRUCTION.key.get_reference("instructions")} are valid 
and what each one means, so that a {COMPUTER.key.get_reference()} can parse and execute them.

---

Different programming languages use different symbols and keywords for the same {OPERATION.key.get_reference()}. 
The instruction "add two numbers" might be written with a `+` symbol in one language, a keyword like `ADD` in another, 
or a single symbol in a third. Each language provides its own syntax for expressing the same underlying instruction.
"""


PROGRAMMING_LANGUAGE = _ProgrammingLanguage(
    key=DefinitionKey(
        name="programming language",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=["coding language"],
)
