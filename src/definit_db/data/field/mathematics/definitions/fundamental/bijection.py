from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS


class _Bijection(Definition):
    def _get_content(self) -> str:
        return f"""
A bijection is a {FUNCTION.key.get_reference(phrase="function")} between two 
{SET.key.get_reference(phrase="sets")} that pairs every element of the first set with exactly one element of the 
second set, and every element of the second set with exactly one element of the first set. In other words, it 
preserves {UNIQUENESS.key.get_reference(phrase="uniqueness")} in both directions.
"""


BIJECTION = _Bijection(
    key=DefinitionKey(
        name="bijection",
        field=FieldName.MATHEMATICS,
    )
)
