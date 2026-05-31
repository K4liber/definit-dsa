from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION


class _LevenshteinDistance(Definition):
    def _get_content(self) -> str:
        return f"""
Levenshtein distance is the minimum number of single-character {OPERATION.key.get_reference(phrase="operations")} 
needed to transform one {STRING.key.get_reference(phrase="string")} into another, where each operation is an 
insertion, deletion, or substitution.
"""


LEVENSHTEIN_DISTANCE = _LevenshteinDistance(
    key=DefinitionKey(
        name="Levenshtein distance",
        field=FieldName.COMPUTER_SCIENCE,
    )
)