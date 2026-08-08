from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.primitive.character import CHARACTER
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.root import ROOT
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _Trie(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {TREE.key.get_reference(phrase="tree")} {DATA_STRUCTURE.key.get_reference(phrase="data structure")} 
used to store a dynamic 
{SET.key.get_reference(phrase="set")} of {STRING.key.get_reference(phrase="strings")}, where each 
{NODE.key.get_reference(phrase="node")} represents a single {CHARACTER.key.get_reference(phrase="character")} of a 
string. The path from the {ROOT.key.get_reference(phrase="root")} to a node represents a prefix shared by every 
string that passes through it. The main advantage of a trie is efficient retrieval of strings with common prefixes.

---

Storing the words `tea`, `ten`, and `in` starts at a root node. Under the root, a child `t` and a child `i` branch 
off. From `t`, a child `e` is added, which then has two children `a` and `n` to complete `tea` and `ten`. From `i`, a 
child `n` completes `in`. Looking up any word means walking from the root along its characters one node at a time.
"""


TRIE = _Trie(
    key=DefinitionKey(
        name="trie",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
