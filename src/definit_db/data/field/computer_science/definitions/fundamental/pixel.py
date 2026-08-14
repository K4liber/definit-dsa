from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION


class _Pixel(Definition):
    def _get_content(self) -> str:
        return f"""
The smallest addressable unit in a digital image, typically storing
{DATA.key.get_reference()} such as color and intensity values.

---

In a photo that is 1920 by 1080, each pixel contributes one tiny part of the
overall {INFORMATION.key.get_reference()}; changing many pixels changes what
the image looks like.
"""


PIXEL = _Pixel(
    key=DefinitionKey(
        name="pixel",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
