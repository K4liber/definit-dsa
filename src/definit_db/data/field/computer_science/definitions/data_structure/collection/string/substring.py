from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.mathematics.definitions.fundamental.subsequence import SUBSEQUENCE


class _Substring(Definition):
    def _get_content(self) -> str:
        return f"""
A contiguous {SUBSEQUENCE.key.get_reference(phrase="subsequence")} of characters within a 
{STRING.key.get_reference(phrase="string")}. For instance, 'the best of' is a substring of 
'It was the best of times'.
"""


SUBSTRING = _Substring(
    key=DefinitionKey(
        name="substring",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
