from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.programming_language import PROGRAMMING_LANGUAGE
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _Code(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the textual form of a {PROGRAM.key.get_reference()} written in a
{PROGRAMMING_LANGUAGE.key.get_reference(phrase="programming language")}. It is a sequence of
{INSTRUCTION.key.get_reference("instructions")} expressed using the syntax and vocabulary of a specific language
so that a {COMPUTER.key.get_reference()} can parse and execute it.

---

The same instruction "add two numbers" can be written as code in many different programming languages. In one
language it might appear as `a + b`, in another as a keyword like `ADD`, and in yet another as a single symbol.
Each snippet is valid code in its own language, but the underlying instruction is the same — only the textual
representation differs.
"""


CODE = _Code(
    key=DefinitionKey(
        name="code",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
