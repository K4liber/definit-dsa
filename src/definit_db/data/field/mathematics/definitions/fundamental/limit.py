from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Limit(Definition):
    def _get_content(self) -> str:
        return f"""
The value that a {FUNCTION.key.get_reference()} or {SEQUENCE.key.get_reference()} approaches as the 
{INPUT_DATA.key.get_reference(phrase="input")} or {INDEX.key.get_reference()} gets arbitrarily close to some point 
(or grows without end). The limit need not be reached — what matters is the trend of approach, not the value at any 
single point.

---

As x approaches 0, the {FUNCTION.key.get_reference()} f(x) = (sin x) / x approaches the {NUMBER.key.get_reference()}
1, even though f(0) itself is undefined. We write lim(x → 0) (sin x) / x = 1: 1 is the limit, the value being
approached, regardless of whether the function ever takes that value.
"""


LIMIT = _Limit(
    key=DefinitionKey(
        name="limit",
        field=FieldName.MATHEMATICS,
    )
)
