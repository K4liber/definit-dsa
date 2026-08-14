from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _LevenshteinDistance(Definition):
    def _get_content(self) -> str:
        return f"""
Levenshtein distance is the minimum {NUMBER.key.get_reference(phrase="number")} of 
single-{CHARACTER.key.get_reference(phrase="character")} {OPERATION.key.get_reference(phrase="operations")} 
needed to transform one {STRING.key.get_reference(phrase="string")} into another, where each operation is an 
insertion, deletion, or substitution.

---

The Levenshtein distance between `kitten` and `sitting` is 3: substitute `k` with `s`, substitute `e` with `i`, and 
insert `g` at the end. The distance between `flaw` and `lawn` is 2: delete `f`, and insert `n` at the end.
"""


LEVENSHTEIN_DISTANCE = _LevenshteinDistance(
    key=DefinitionKey(
        name="Levenshtein distance",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
