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
A programming model for processing large {DATASET.key.get_reference(phrase="datasets")}
by splitting work into two phases:

- map: transform input records into intermediate key/value pairs (conceptually a {MAP.key.get_reference(phrase="map")}).
- reduce: aggregate the intermediate values for each key.

MapReduce enables {PARALLELISM.key.get_reference()} by distributing the map and reduce work across many
{WORKER.key.get_reference(phrase="workers")}.

---

To count how often each word appears in a large {DATASET.key.get_reference(phrase="dataset")} of documents, the map
phase turns each word it reads into a (word, 1) pair. The reduce phase then collects all pairs sharing a word and
adds their counts, producing a single (word, total) result per word. Because each 
{WORKER.key.get_reference(phrase="worker")} handles a different slice of the documents, the counting is done in 
{PARALLELISM.key.get_reference(phrase="parallel")} and finishes much faster than reading the documents one by one.
"""


MAPREDUCE = _MapReduce(
    key=DefinitionKey(
        name="MapReduce",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
