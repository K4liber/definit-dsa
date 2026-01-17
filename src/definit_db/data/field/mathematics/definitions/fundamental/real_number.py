from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _RealNumber(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference(phrase="Real number")} is a {NUMBER.key.get_reference(phrase="number")} that can represent a
quantity on the continuous number line.
"""


REAL_NUMBER = _RealNumber(
    key=DefinitionKey(
        name="Real number",
        field=FieldName.MATHEMATICS,
    )
)
