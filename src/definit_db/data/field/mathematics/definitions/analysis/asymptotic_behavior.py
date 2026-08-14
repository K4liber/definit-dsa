from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.infinity import INFINITY
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.limit import LIMIT


class _AsymptoticBehavior(Definition):
    def _get_content(self) -> str:
        return f"""
The behavior of a {FUNCTION.key.get_reference()} as its {INPUT_DATA.key.get_reference("input")} 
approaches {INFINITY.key.get_reference(phrase="infinity")} or some other {LIMIT.key.get_reference(phrase="limit")}. 
Asymptotic behavior describes how a function grows or behaves in the limit, focusing on the dominant terms and 
ignoring lower-order terms and constant factors.

---

For f(n) = 3n² + 5n + 7, the asymptotic behavior is dominated by the n² term: as n approaches 
{INFINITY.key.get_reference(phrase="infinity")}, n² grows far faster than 5n and the constant 7, so the 
lower-order terms can be ignored.
"""


ASYMPTOTIC_BEHAVIOR = _AsymptoticBehavior(
    key=DefinitionKey(
        name="asymptotic_behavior",
        field=FieldName.MATHEMATICS,
    )
)
