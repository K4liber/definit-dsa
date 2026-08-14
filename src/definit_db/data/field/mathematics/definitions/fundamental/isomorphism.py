from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.bijection import BIJECTION
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION


class _Isomorphism(Definition):
    def _get_content(self) -> str:
        return f"""
An isomorphism is a structure-preserving {BIJECTION.key.get_reference(phrase="bijection")} between two 
{OBJECT.key.get_reference(phrase="objects")}. It pairs elements one-to-one while preserving the 
{RELATION.key.get_reference(phrase="relations")} or {OPERATION.key.get_reference(phrase="operations")} that are 
relevant to the objects being compared.

---

Addition on integers is isomorphic to addition on even integers via the
{BIJECTION.key.get_reference(phrase="bijection")} f(n) = 2n:

  f(a + b) = 2(a + b) = 2a + 2b = f(a) + f(b)

The {OPERATION.key.get_reference(phrase="operation")} is preserved — both structures behave identically
under their respective additions.
"""


ISOMORPHISM = _Isomorphism(
    key=DefinitionKey(
        name="isomorphism",
        field=FieldName.MATHEMATICS,
    )
)
