from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.boundary import BOUNDARY
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.iteration import ITERATION
from definit_db.data.field.mathematics.definitions.fundamental.loop import LOOP
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _OffByOne(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
A common error in {ALGORITHM.key.get_reference("algorithms")} where a 
{LOOP.key.get_reference()} {ITERATION.key.get_reference(phrase="iterates")} one time too many or one time too few, 
or where an {INDEX.key.get_reference()} is off by one position. This often occurs when using zero-based indexing or 
when defining loop {BOUNDARY.key.get_reference(phrase="boundaries")} incorrectly. Off-by-one errors can lead to 
incorrect results or missing the first or last {ITEM.key.get_reference(phrase="element")} of a 
{SEQUENCE.key.get_reference(phrase="sequence")}.

---

A {LOOP.key.get_reference()} meant to visit every element of a 5-element sequence
uses the condition "i <= 5" instead of "i < 5". On its last pass the {INDEX.key.get_reference()} "i" equals "5", which 
lies outside the valid range of "0" to "4", causing an off-by-one error.
"""


OFF_BY_ONE = _OffByOne(DefinitionKey(name="off-by-one", field=FieldName.MATHEMATICS))
