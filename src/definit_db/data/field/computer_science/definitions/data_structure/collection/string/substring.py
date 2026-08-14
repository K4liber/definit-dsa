from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.mathematics.definitions.fundamental.subsequence import SUBSEQUENCE


class _Substring(Definition):
    def _get_content(self) -> str:
        return f"""
A contiguous {SUBSEQUENCE.key.get_reference(phrase="subsequence")} of 
{CHARACTER.key.get_reference(phrase="characters")} within a {STRING.key.get_reference(phrase="string")}. Unlike a 
subsequence, the selected characters must appear next to each other in the original string.

---

In the string `It was the best of times`, the segment `the best of` is a substring because its characters appear 
consecutively. By contrast, `I was times` is not a substring, since those words are not adjacent, even though they 
appear in order.
"""


SUBSTRING = _Substring(
    key=DefinitionKey(
        name="substring",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
