from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Peak(Definition):
    def _get_content(self) -> str:
        return f"""
A peak is an {ITEM.key.get_reference(phrase="element")} in a {SEQUENCE.key.get_reference(phrase="sequence")} 
whose value is greater than or equal to the values of its adjacent elements. A peak is often identified by an 
{INDEX.key.get_reference(phrase="index")}; boundary elements are compared only with the neighbor that exists.
"""


PEAK = _Peak(
    key=DefinitionKey(
        name="peak",
        field=FieldName.MATHEMATICS,
    )
)