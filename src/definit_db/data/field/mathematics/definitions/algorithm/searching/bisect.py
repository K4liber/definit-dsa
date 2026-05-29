from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.searching.binary_search import BINARY_SEARCH
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Bisect(Definition):
    def _get_content(self) -> str:
        return f"""
Bisect is a {BINARY_SEARCH.key.get_reference(phrase="binary search")} technique that finds the 
{INDEX.key.get_reference(phrase="index")} where a value should be inserted into a sorted 
{SEQUENCE.key.get_reference(phrase="sequence")} while preserving the order of the sequence. It can return the 
leftmost or rightmost valid insertion position when equal values are already present.
"""


BISECT = _Bisect(
    key=DefinitionKey(
        name="bisect",
        field=FieldName.MATHEMATICS,
    )
)