from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.processor import PROCESSOR
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _Concurrency(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the ability of a {PROGRAM.key.get_reference()} to execute multiple tasks or 
{OPERATION.key.get_reference("operations")} simultaneously or in overlapping time periods. In concurrent execution, 
multiple streams of {INSTRUCTION.key.get_reference("instructions")} make progress without necessarily running at the 
exact same instant, allowing for more efficient use of system resources and improved responsiveness. Concurrency 
enables programs to handle multiple operations such as user input or background processing at the same time.

---

A web browser that downloads images while the user scrolls a page is not running both tasks at the
exact same instant on a single {PROCESSOR.key.get_reference()}. Instead, the processor rapidly switches between the two 
instruction streams, so each makes progress and the application stays responsive.
"""


CONCURRENCY = _Concurrency(DefinitionKey(name="concurrency", field=FieldName.COMPUTER_SCIENCE))
