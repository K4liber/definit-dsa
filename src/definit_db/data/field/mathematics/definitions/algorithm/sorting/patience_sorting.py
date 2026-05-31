from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _PatienceSorting(Definition):
    def _get_content(self) -> str:
        return f"""
Patience sorting is a {SORTING.key.get_reference(phrase="sorting")} algorithm that processes a 
{SEQUENCE.key.get_reference(phrase="sequence")} by dealing its elements into ordered piles, placing each element 
on the leftmost compatible pile. The piles are then repeatedly merged or selected from to produce the sorted 
sequence.
"""


PATIENCE_SORTING = _PatienceSorting(
    key=DefinitionKey(
        name="Patience sorting",
        field=FieldName.MATHEMATICS,
    )
)