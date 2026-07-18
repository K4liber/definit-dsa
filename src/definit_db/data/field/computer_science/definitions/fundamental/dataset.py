from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Dataset(Definition):
    def _get_content(self) -> str:
        return f"""
A {SET.key.get_reference(phrase="set")} of {DATA.key.get_reference(phrase="data")}, 
typically organized as records or examples for analysis, training, or testing.

---

A table of 100 rows, each containing a student's exam scores across five subjects, is a dataset: it is a set
of data records that can be analyzed to study student performance.
"""


DATASET = _Dataset(
    key=DefinitionKey(
        name="dataset",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
