from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION
from definit_db.data.field.mathematics.definitions.tree.unbalanced_binary_tree import UNBALANCED_BINARY_TREE


class _Lopsided(Definition):
    def _get_content(self) -> str:
        return f"""
lopsided describes a situation where something is unbalanced or heavily skewed toward one side.

In computer science, it often refers to a {DATA_STRUCTURE.key.get_reference(phrase="data structure")} or workload
whose shape or {DISTRIBUTION.key.get_reference(phrase="distribution")} is highly uneven.

---

An {UNBALANCED_BINARY_TREE.key.get_reference(phrase="unbalanced binary tree")} is a lopsided data structure: one
side may contain a long chain of nodes while the other side is nearly empty, so the tree leans heavily toward one
side rather than spreading its nodes evenly.
"""


LOPSIDED = _Lopsided(
    key=DefinitionKey(
        name="lopsided",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
