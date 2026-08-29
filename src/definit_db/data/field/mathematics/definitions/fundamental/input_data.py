from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _InputData(Definition):
    def _get_content(self) -> str:
        return f"""
The {INFORMATION.key.get_reference()} provided to a 
{FUNCTION.key.get_reference()} to be processed. 
It represents the initial state or values that the function operates on to produce an output.

---

For the function f(x) = x + 1, the {NUMBER.key.get_reference(phrase="number")} 3 is the input data; 
the function processes it to produce the output 4.
"""


INPUT_DATA = _InputData(DefinitionKey(name="input data", field=FieldName.MATHEMATICS), aliases=["input"])
