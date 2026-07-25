from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Sorting(Definition):
    def _get_content(self) -> str:
        return f"""
Sorting is an {ALGORITHM.key.get_reference(phrase="algorithmic")} process that arranges the 
{ITEM.key.get_reference(phrase="elements")} of a {SEQUENCE.key.get_reference(phrase="sequence")} or 
{SET.key.get_reference(phrase="set")} in a certain order, typically according to a specified 
{RELATION.key.get_reference(phrase="relation")} (such as ascending or descending). 

---

Given the sequence [4, 1, 7, 2, 9, 3], sorting by the ascending relation (each element ≤ the next) produces:

[4, 1, 7, 2, 9, 3]  →  [1, 2, 3, 4, 7, 9]

The relation defines the order — the same sequence sorted by the descending relation gives:

[4, 1, 7, 2, 9, 3]  →  [9, 7, 4, 3, 2, 1]
"""


SORTING = _Sorting(
    key=DefinitionKey(
        name="sorting",
        field=FieldName.MATHEMATICS,
    )
)
