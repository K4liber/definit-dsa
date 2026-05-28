from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.array import ARRAY
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.subsequence import SUBSEQUENCE


class _Subarray(Definition):
    def _get_content(self) -> str:
        return f"""
A contiguous {SUBSEQUENCE.key.get_reference(phrase="subsequence")} of an 
{ARRAY.key.get_reference(phrase="array")} A of length n. A subarray is determined by two 
{INDEX.key.get_reference(phrase="indices")} l and r with 0 <= l <= r < n, and contains exactly the 
elements A[l], A[l+1], ..., A[r] in their original order. For example, [2, 3, 4] is a subarray of 
[1, 2, 3, 4, 5], while [1, 3, 5] is not because its elements are not adjacent in the original array.
"""


SUBARRAY = _Subarray(
    key=DefinitionKey(
        name="subarray",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
