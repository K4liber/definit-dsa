from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.dataset import DATASET
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.fundamental.partitioning import PARTITIONING
from definit_db.data.field.mathematics.definitions.notations.label import LABEL


class _Clustering(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is the task of {PARTITIONING.key.get_reference(phrase="partitioning")} a 
{DATASET.key.get_reference(phrase="dataset")} into multiple groups (clusters) such that items in the same cluster 
are more similar to each other than to items in other clusters.

The resulting clusters can be assigned a {LABEL.key.get_reference(phrase="label")} 
(e.g., a cluster id) for downstream use.

Clustering {ALGORITHM.key.get_reference(phrase="algorithms")} typically learn structure from unlabeled data.
"""


CLUSTERING = _Clustering(
    key=DefinitionKey(
        name="clustering",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
