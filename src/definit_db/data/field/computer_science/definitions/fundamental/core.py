from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.parallelism import PARALLELISM
from definit_db.data.field.computer_science.definitions.fundamental.processor import PROCESSOR
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION


class _Core(Definition):
    def _get_content(self) -> str:
        return f"""
An independent processing unit within a {PROCESSOR.key.get_reference()} 
that can execute {INSTRUCTION.key.get_reference("instructions")} and perform {OPERATION.key.get_reference("operations")} 
independently of other cores. Modern processors often contain multiple cores, enabling them to execute multiple 
tasks simultaneously, which is essential for {PARALLELISM.key.get_reference(phrase="parallel computing")}.

---

A quad-core processor has four cores, each running its own stream of instructions. While one core renders video
frames for a {PROGRAM.key.get_reference()}, the other three can handle audio decoding, network input, and user
interface updates — all at the same time, with each core unaware of the others' work.
"""


CORE = _Core(DefinitionKey(name="core", field=FieldName.COMPUTER_SCIENCE))
