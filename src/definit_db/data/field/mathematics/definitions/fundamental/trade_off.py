from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName


class _TradeOff(Definition):
    def _get_content(self) -> str:
        return """
A situation in which improving one desirable outcome requires accepting a worse outcome in another.

---

Choosing a shorter but more expensive route instead of a longer but cheaper route involves a trade-off: reducing
travel time increases the cost, while reducing the cost increases the travel time.
"""


TRADE_OFF = _TradeOff(
    key=DefinitionKey(
        name="trade-off",
        field=FieldName.MATHEMATICS,
    )
)
