from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.concurrency import CONCURRENCY
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.processor import PROCESSOR
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.performance import PERFORMANCE
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.quadrant import QUADRANT


class _Parallelism(Definition):
    def _get_content(self) -> str:
        return f"""
A form of {CONCURRENCY.key.get_reference()} where multiple 
{OPERATION.key.get_reference("operations")} or tasks are executed simultaneously at the exact same time, typically by 
utilizing multiple {PROCESSOR.key.get_reference("processors")} or processing units. Unlike 
{CONCURRENCY.key.get_reference()}, which is about managing multiple tasks that may overlap in time, 
parallelism specifically requires the physical simultaneous execution of tasks. This approach enables 
{PROGRAM.key.get_reference("programs")} to achieve significant {PERFORMANCE.key.get_reference(phrase="performance")} improvements by dividing work across 
multiple processing units.

---

Rendering a 4K video frame can be split into four {QUADRANT.key.get_reference(phrase="quadrants")}, each assigned to a 
separate processor that applies the same stream of {INSTRUCTION.key.get_reference("instructions")} to its quadrant at 
the exact same instant. All four finish together, so the frame renders roughly four times faster than on a single 
processor — true parallel execution, not just overlapping progress.
"""


PARALLELISM = _Parallelism(DefinitionKey(name="parallelism", field=FieldName.COMPUTER_SCIENCE))
