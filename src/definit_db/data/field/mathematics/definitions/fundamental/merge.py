from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Merge(Definition):
    def _get_content(self) -> str:
        return f"""
Merge is an {OPERATION.key.get_reference()} that combines two {SEQUENCE.key.get_reference("sequences")} into a 
single sequence by interleaving their elements while preserving the order of each input sequence.

---

Merge the {SEQUENCE.key.get_reference("sequences")} ("1", "3") and ("2", "4") into the single sequence 
("1", "2", "3", "4"). The result interleaves the inputs while keeping each input's internal order: "1" still 
precedes "3", and "2" still precedes "4".
"""


MERGE = _Merge(
    key=DefinitionKey(
        name="merge",
        field=FieldName.MATHEMATICS,
    )
)
