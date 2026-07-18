from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY


class _ExpectedValue(Definition):
    def _get_content(self) -> str:
        return f"""
The long-run average value of a random outcome.

For a {DISTRIBUTION.key.get_reference("distribution")}, the expected value is computed by weighting each
possible value by its {PROBABILITY.key.get_reference()} and summing the results.

---

Rolling a fair six-sided die gives each outcome "1" through "6" an equal {PROBABILITY.key.get_reference()} of 
"1/6". The expected value of a roll is "(1+2+3+4+5+6) × (1/6) = 3.5", the long-run 
average result over many rolls.
"""


EXPECTED_VALUE = _ExpectedValue(
    key=DefinitionKey(
        name="expected value",
        field=FieldName.MATHEMATICS,
    )
)
