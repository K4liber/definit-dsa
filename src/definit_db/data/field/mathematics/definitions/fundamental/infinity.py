from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.collection import COLLECTION
from definit_db.data.field.mathematics.definitions.fundamental.finite_set import FINITE_SET
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Infinity(Definition):
    def _get_content(self) -> str:
        return f"""
Infinity is a mathematical concept representing something without an end or limit: a quantity, process, or 
{OBJECT.key.get_reference(phrase="object")} that is not limited by any finite 
{BOUND.key.get_reference(phrase="bound")}. It is not an ordinary 
{NUMBER.key.get_reference(phrase="number")} in the usual real-number system; instead, it is used to describe 
objects that grow without bound or a {COLLECTION.key.get_reference(phrase="collection")} or 
{SET.key.get_reference(phrase="set")} that is not {FINITE_SET.key.get_reference(phrase="finite")}.
"""


INFINITY = _Infinity(
    key=DefinitionKey(
        name="infinity",
        field=FieldName.MATHEMATICS,
    )
)
