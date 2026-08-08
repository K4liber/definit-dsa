from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM


class _SoftwareSystem(Definition):
    def _get_content(self) -> str:
        return f"""
A set of {PROGRAM.key.get_reference("programs")} designed to work together as a unified whole to serve a common 
purpose. Unlike a single program, a software system coordinates multiple programs that each handle a distinct 
part of the overall task.

---

An online store is a software system. One program handles user authentication, another processes payments, 
and a third manages the product catalogue. Each is its own program, but together they form the software system 
that delivers the shopping experience.
"""


SOFTWARE_SYSTEM = _SoftwareSystem(
    key=DefinitionKey(
        name="software_system",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
