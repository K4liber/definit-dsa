from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Dataset(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a group of {DATA.key.get_reference("data")}, 
typically organized for analysis, training, or testing.

A dataset can be viewed as a {SET.key.get_reference("set")} of records or examples.
"""


DATASET = _Dataset(
    key=DefinitionKey(
        name="dataset",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
