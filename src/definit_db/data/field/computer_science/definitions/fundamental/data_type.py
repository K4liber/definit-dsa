from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _DataType(Definition):
    def _get_content(self) -> str:
        return f"""
Data type (or simply type) is a grouping of {DATA.key.get_reference(phrase="data")} values, usually specified by a 
{SET.key.get_reference(phrase="set")} of possible values, a {SET.key.get_reference(phrase="set")} of allowed 
{OPERATION.key.get_reference(phrase="operations")} on these values, and/or a representation of these values as a 
sequence of {BIT.key.get_reference(phrase="bits")}.

---

For example, the 8-bit unsigned integer data type is defined by its set of possible values (0 through 255), a
set of allowed operations such as addition and comparison, and a representation as a sequence of 8 bits.
"""


DATA_TYPE = _DataType(
    key=DefinitionKey(
        name="data_type",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=("type",),
)
