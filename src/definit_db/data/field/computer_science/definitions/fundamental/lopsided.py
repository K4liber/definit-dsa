from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION


class _Lopsided(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} describes a situation where something is unbalanced or heavily skewed toward one side.

In computer science, it often refers to a {DATA_STRUCTURE.key.get_reference(phrase="data structure")} or workload
whose shape or {DISTRIBUTION.key.get_reference(phrase="distribution")} is highly uneven.
"""


LOPSIDED = _Lopsided(
    key=DefinitionKey(
        name="lopsided",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
