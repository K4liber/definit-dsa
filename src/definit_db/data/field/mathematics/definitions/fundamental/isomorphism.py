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
"""


ISOMORPHISM = _Isomorphism(
    key=DefinitionKey(
        name="isomorphism",
        field=FieldName.MATHEMATICS,
    )
)
