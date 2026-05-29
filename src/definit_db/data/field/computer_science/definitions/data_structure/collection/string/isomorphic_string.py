from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.mathematics.definitions.fundamental.isomorphism import ISOMORPHISM


class _IsomorphicString(Definition):
    def _get_content(self) -> str:
        return f"""
Two {STRING.key.get_reference(phrase="strings")} are isomorphic when the characters of one string can be replaced 
to obtain the other string using a consistent one-to-one mapping. This mapping is an 
{ISOMORPHISM.key.get_reference(phrase="isomorphism")} between the character patterns of the strings: each character 
in the first string maps to exactly one character in the second string, and no two different characters map to the 
same character.
"""


ISOMORPHIC_STRING = _IsomorphicString(
    key=DefinitionKey(
        name="isomorphic string",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
