from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.natural_number import NATURAL_NUMBER
from definit_db.data.field.mathematics.definitions.problem.base_case import BASE_CASE


class _MathematicalInduction(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a proof technique used to show that a statement holds for all 
{NATURAL_NUMBER.key.get_reference("natural numbers")}.

It typically consists of proving a {BASE_CASE.key.get_reference("base case")} and then proving that if the 
statement holds for one value, it also holds for the next.
"""


MATHEMATICAL_INDUCTION = _MathematicalInduction(
    key=DefinitionKey(
        name="mathematical induction",
        field=FieldName.MATHEMATICS,
    )
)
