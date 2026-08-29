from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.machine import MACHINE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _ProgrammingModel(Definition):
    def _get_content(self) -> str:
        return f"""
An abstraction that describes how {PROGRAM.key.get_reference(phrase="programs")} are structured and how 
{OPERATION.key.get_reference(phrase="operations")} within them are organized and coordinated. A programming model 
defines a consistent way to express {COMPUTATION.key.get_reference()} so that the same program can be carried out in 
a particular manner, such as stage by stage or across many {MACHINE.key.get_reference(phrase="machines")}.

---

A programming model might express every computation as a series of stages, where each stage takes the output of 
the previous one as its {INPUT_DATA.key.get_reference(phrase="input")}. A programmer writes each stage as a small program, and the model guarantees that the 
stages are connected and scheduled in the right order. This lets the programmer focus on what each stage does 
without managing the details of how {DATA.key.get_reference(phrase="data")} moves between them.
"""


PROGRAMMING_MODEL = _ProgrammingModel(
    key=DefinitionKey(
        name="programming model",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=["computational model"],
)
