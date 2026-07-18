from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.machine import MACHINE
from definit_db.data.field.computer_science.definitions.fundamental.parallelism import PARALLELISM
from definit_db.data.field.computer_science.definitions.fundamental.process import PROCESS
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.thread import THREAD


class _Worker(Definition):
    def _get_content(self) -> str:
        return f"""
A {PROCESS.key.get_reference(phrase="process")}, 
{THREAD.key.get_reference(phrase="thread")}, or {MACHINE.key.get_reference(phrase="machine")} 
that performs a unit of work as part of a larger computation.

In distributed or {PARALLELISM.key.get_reference(phrase="parallel")} systems, workers execute parts of a
{PROGRAM.key.get_reference(phrase="program")} (tasks) assigned by a coordinator.

---

When a {PROGRAM.key.get_reference(phrase="program")} must process one thousand images, the work can be split across
four {THREAD.key.get_reference(phrase="threads")}, each acting as a worker that handles two hundred fifty images.
The workers run at the same time, so the {PARALLELISM.key.get_reference(phrase="parallelism")} lets the whole batch
finish roughly four times faster than a single worker would.
"""


WORKER = _Worker(
    key=DefinitionKey(
        name="worker",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
