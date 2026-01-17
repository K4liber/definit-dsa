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
A {self.key.get_reference()} is a {PROCESS.key.get_reference(phrase="process")}, 
{THREAD.key.get_reference(phrase="thread")}, or {MACHINE.key.get_reference(phrase="machine")} 
that performs a unit of work as part of a larger computation.

In distributed or {PARALLELISM.key.get_reference(phrase="parallel")} systems, workers execute parts of a
{PROGRAM.key.get_reference(phrase="program")} (tasks) assigned by a coordinator.
"""


WORKER = _Worker(
    key=DefinitionKey(
        name="worker",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
