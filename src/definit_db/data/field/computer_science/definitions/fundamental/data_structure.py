from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _DataStructure(Definition):
    def _get_content(self) -> str:
        return f"""
A way of organizing and storing {DATA.key.get_reference(phrase="data")} so it can be 
accessed and modified {EFFICIENCY.key.get_reference(phrase="efficiently")}. A data structure contains a value or group 
of values and the {FUNCTION.key.get_reference(phrase="functions")} or 
{OPERATION.key.get_reference(phrase="operations")} that can be applied to the data.

---

A list of exam scores (72, 85, 90), together with operations such as "add a score" or "find the highest score",
forms a data structure: the values are organized in a {SEQUENCE.key.get_reference()} and paired with the functions 
that act on them.
"""


DATA_STRUCTURE = _DataStructure(
    key=DefinitionKey(
        name="data_structure",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
