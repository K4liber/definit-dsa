from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION


class _UpperBound(Definition):
    def _get_content(self) -> str:
        return f"""
A {BOUND.key.get_reference()} that establishes the maximum value or growth rate that a 
{FUNCTION.key.get_reference()} or expression can achieve. An upper bound provides a ceiling or constraint 
on how large values can become.
"""


UPPER_BOUND = _UpperBound(
    key=DefinitionKey(
        name="upper_bound",
        field=FieldName.MATHEMATICS,
    )
)
