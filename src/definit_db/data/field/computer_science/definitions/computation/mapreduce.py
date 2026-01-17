from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.map import MAP
from definit_db.data.field.computer_science.definitions.fundamental.dataset import DATASET
from definit_db.data.field.computer_science.definitions.fundamental.parallelism import PARALLELISM
from definit_db.data.field.computer_science.definitions.fundamental.worker import WORKER


class _MapReduce(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a programming model for processing large {DATASET.key.get_reference(phrase="datasets")}
by splitting work into two phases:

- map: transform input records into intermediate key/value pairs (conceptually a {MAP.key.get_reference(phrase="map")}).
- reduce: aggregate the intermediate values for each key.

MapReduce enables {PARALLELISM.key.get_reference()} by distributing the map and reduce work across many
{WORKER.key.get_reference(phrase="workers")}.
"""


MAPREDUCE = _MapReduce(
    key=DefinitionKey(
        name="MapReduce",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
