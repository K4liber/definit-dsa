from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.interval import INTERVAL
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.tree.balanced_binary_tree import BALANCED_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.binary_search_tree import BINARY_SEARCH_TREE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE


class _IntervalTree(Definition):
    def _get_content(self) -> str:
        return f"""
A type of {BINARY_SEARCH_TREE.key.get_reference(phrase="binary search tree")} that stores intervals as its keys. 
Each {NODE.key.get_reference(phrase="node")} in the interval tree represents an 
{INTERVAL.key.get_reference(phrase="interval")}, and the tree is structured in such a way that it allows for 
efficient searching of all intervals that overlap with a given interval or point. The intervals are typically 
represented by their start and end points, and the 
{TREE.key.get_reference(phrase="tree")} is {BALANCED_BINARY_TREE.key.get_reference(phrase="balanced")} to ensure 
efficient search operations.
"""


INTERVAL_TREE = _IntervalTree(
    key=DefinitionKey(
        name="interval_tree",
        field=FieldName.MATHEMATICS,
    )
)
