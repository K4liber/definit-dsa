from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.notations.label import LABEL


class _RegularExpression(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a {SEQUENCE.key.get_reference()} of 
{CHARACTER.key.get_reference(phrase="characters")} that defines a search pattern for 
{STRING.key.get_reference("strings")}. Regular expressions use special syntax to specify patterns, including 
literal characters, character classes, quantifiers, and anchors. They 
enable powerful text matching, searching, and manipulation operations, allowing users to find, extract, or replace text 
that matches specific patterns. For example, the pattern `[0-9]+` matches one or more digits, and `^[a-z]+$` matches 
{STRING.key.get_reference("strings")} containing only lowercase letters from start to end. Regular expressions 
can also use groups and {LABEL.key.get_reference("labels")} to capture and reference parts of the matched text.
"""


REGULAR_EXPRESSION = _RegularExpression(DefinitionKey(name="regular expression", field=FieldName.COMPUTER_SCIENCE))
