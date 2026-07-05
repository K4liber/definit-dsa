from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.queue import QUEUE
from definit_db.data.field.computer_science.definitions.fundamental.code import CODE
from definit_db.data.field.computer_science.definitions.fundamental.test import TEST
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _ConceptualTest(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {TEST.key.get_reference("test")} used to check understanding of an idea,
model, or design, rather than to execute {CODE.key.get_reference()}.

A conceptual test evaluates whether some {CRITERION.key.get_reference("criteria")} are satisfied.

---

Before writing any code, a designer might ask: "If the {QUEUE.key.get_reference()} is empty and we try to remove
an element, what should happen?" Answering "it should report that there is nothing to remove, not crash" is a
conceptual test — it checks that the design handles the empty case correctly, without yet building anything.
"""


CONCEPTUAL_TEST = _ConceptualTest(
    key=DefinitionKey(
        name="conceptual test",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
