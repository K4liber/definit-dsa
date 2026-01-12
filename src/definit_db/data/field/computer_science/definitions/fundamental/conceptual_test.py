from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.test import TEST
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION


class _ConceptualTest(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {TEST.key.get_reference("test")} used to check understanding of an idea,
model, or design, rather than to execute code.

A conceptual test evaluates whether some {CRITERION.key.get_reference("criteria")} are satisfied.
"""


CONCEPTUAL_TEST = _ConceptualTest(
    key=DefinitionKey(
        name="conceptual test",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
