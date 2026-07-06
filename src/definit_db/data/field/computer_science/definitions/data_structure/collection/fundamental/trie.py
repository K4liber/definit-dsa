from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Trie(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {TREE.key.get_reference(phrase="tree")} data structure that is used to store a dynamic 
{SET.key.get_reference(phrase="set")} of strings, where the keys are usually strings. Each 
{NODE.key.get_reference(phrase="node")} in the trie represents a single {CHARACTER.key.get_reference()} of a 
{STRING.key.get_reference(phrase="string")}, and the path from the root to a node represents a prefix of the 
string. The main advantage of using a trie is that it allows for efficient retrieval of strings with common 
prefixes.
"""


TRIE = _Trie(
    key=DefinitionKey(
        name="trie",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
