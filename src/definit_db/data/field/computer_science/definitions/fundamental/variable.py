from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.notations.label import LABEL


class _Variable(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a named storage location identified by a {LABEL.key.get_reference()} 
that holds {DATA.key.get_reference()} which can be modified during {PROGRAM.key.get_reference()} execution. 
A variable associates a name with a value that can change over time.

---

For example, a variable named `count` might initially hold the {NUMBER.key.get_reference()} 0. Each time a relevant 
event occurs, the stored value is updated — to 1, then 2, and so on. The name `count` stays the same throughout, but 
the data at that location changes over time.
"""


VARIABLE = _Variable(DefinitionKey(name="variable", field=FieldName.COMPUTER_SCIENCE))
