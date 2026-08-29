from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.substring import SUBSTRING
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.notations.label import LABEL


class _RegularExpression(Definition):
    def _get_content(self) -> str:
        return f"""
A {SEQUENCE.key.get_reference(phrase="sequence")} of 
{CHARACTER.key.get_reference(phrase="characters")} that defines a search pattern for 
{STRING.key.get_reference(phrase="strings")}. Regular expressions use special syntax — including literal characters, 
character classes (sets like `[0-9]`), quantifiers (such as `+` or `*`), and anchors (such as `^` and `$`) — 
to specify patterns for matching, searching, and manipulating text. 
Groups and {LABEL.key.get_reference(phrase="labels")} can capture and reference parts of the matched text.

---

The pattern `[0-9]+` matches one or more digits, so it finds {SUBSTRING.key.get_reference(phrase="substrings")} such 
as `42` or `7` inside a longer string. The pattern `^[a-z]+$` matches only strings that consist entirely of lowercase 
letters from start to end, such as `hello` but not `Hello123`.
"""


REGULAR_EXPRESSION = _RegularExpression(
    DefinitionKey(name="regular expression", field=FieldName.COMPUTER_SCIENCE),
    aliases=["regex"],
)
