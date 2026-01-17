from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY


class _ExpectedValue(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} is the long-run average value of a random outcome.

For a {DISTRIBUTION.key.get_reference("distribution")}, the expected value is computed by weighting each
possible value by its {PROBABILITY.key.get_reference()} and summing the results.
"""


EXPECTED_VALUE = _ExpectedValue(
    key=DefinitionKey(
        name="expected value",
        field=FieldName.MATHEMATICS,
    )
)
