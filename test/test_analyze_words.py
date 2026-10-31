from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.analyze_words import Analysis
from definit_db.analyze_words import WordStats
from definit_db.analyze_words import analyze
from definit_db.analyze_words import candidate_words
from definit_db.analyze_words import definition_word_lemmas
from definit_db.analyze_words import lemma
from definit_db.analyze_words import most_common
from definit_db.analyze_words import strip_markdown_links
from definit_db.analyze_words import tokenize


def _definition(name: str, content: str, aliases: tuple[str, ...] = ()) -> Definition:
    return Definition(
        key=DefinitionKey(name=name, field="computer_science"),
        content=content,
        aliases=aliases,
    )


def test_strip_markdown_links_keeps_phrase_drops_target() -> None:
    text = "Uses a [stack](mathematics/stack) internally."
    assert strip_markdown_links(text) == "Uses a stack internally."


def test_tokenize_lowercases_strips_punctuation_and_short_tokens() -> None:
    assert tokenize("The Bits; e.g. 1011 -- are 'units'!") == [
        "the",
        "bits",
        "are",
        "units",
    ]


def test_tokenize_removes_markdown_link_targets() -> None:
    assert tokenize("[items](mathematics/item) and [nodes](mathematics/node)") == ["items", "and", "nodes"]


def test_lemma_irregular_plurals() -> None:
    assert lemma("indices") == "index"
    assert lemma("vertices") == "vertex"
    assert lemma("matrices") == "matrix"
    assert lemma("criteria") == "criterion"
    assert lemma("children") == "child"


def test_lemma_regular_plurals() -> None:
    assert lemma("trees") == "tree"
    assert lemma("copies") == "copy"
    assert lemma("boxes") == "box"
    assert lemma("bytes") == "byte"
    assert lemma("edges") == "edge"


def test_lemma_does_not_stem_non_plurals() -> None:
    assert lemma("class") == "class"
    assert lemma("data") == "data"
    assert lemma("bus") == "bus"
    assert lemma("axis") == "axis"
    assert lemma("run") == "run"


def test_definition_word_lemmas_covers_names_and_aliases() -> None:
    definitions = [
        _definition(name="bit", content="", aliases=("binary digit",)),
        _definition(name="Queue", content=""),
    ]
    lemmas = definition_word_lemmas(definitions)
    assert lemmas >= {"bit", "binary", "digit", "queue"}


def test_analyze_excludes_definition_words_case_and_plural_insensitive() -> None:
    definitions = [
        _definition(name="bit", content="Bits and BYTES store values."),
        _definition(name="byte", content="A byte consists of bits."),
    ]
    analysis = analyze(definitions=definitions)
    assert analysis.definition_count == 2
    assert analysis.base_collection == ("and", "consist", "of", "store", "value")
    assert analysis.stats["and"].occurrences == 1
    assert analysis.stats["and"].definitions == 1
    assert analysis.stats["consist"].definitions == 1


def test_analyze_is_case_insensitive_and_unique() -> None:
    definitions = [_definition(name="bit", content="Value value VALUE.")]
    analysis = analyze(definitions=definitions)
    assert analysis.base_collection == ("value",)
    assert analysis.stats["value"].occurrences == 3


def test_analyze_excludes_definition_aliases() -> None:
    definitions = [
        _definition(name="bit", content="Uses a node and a vertex.", aliases=("binary digit",)),
        _definition(name="node", content="", aliases=()),
    ]
    analysis = analyze(definitions=definitions)
    # "vertex" is not a name/alias in this database, so it stays in the base collection.
    assert analysis.base_collection == ("and", "use", "vertex")


def test_most_common_orders_by_occurrences_and_excludes_stopwords() -> None:
    analysis = Analysis(
        definition_count=1,
        base_collection=("tree", "value", "the", "use"),
        stats={
            "the": WordStats(occurrences=10, definitions=1),
            "tree": WordStats(occurrences=4, definitions=2),
            "value": WordStats(occurrences=4, definitions=1),
            "use": WordStats(occurrences=1, definitions=1),
        },
    )
    common = most_common(analysis=analysis, top=2)
    assert common == [
        ("tree", WordStats(occurrences=4, definitions=2)),
        ("value", WordStats(occurrences=4, definitions=1)),
    ]

    common_raw = most_common(analysis=analysis, top=1, include_stopwords=True)
    assert common_raw == [("the", WordStats(occurrences=10, definitions=1))]


def test_candidate_words_filtering_and_ordering() -> None:
    analysis = Analysis(
        definition_count=3,
        base_collection=("array", "use", "of", "it"),
        stats={
            "array": WordStats(occurrences=9, definitions=3),
            "use": WordStats(occurrences=5, definitions=3),
            "of": WordStats(occurrences=4, definitions=2),
            "it": WordStats(occurrences=4, definitions=2),
        },
    )
    # min_definitions=2: "array" (3 defs), "of"/"it" (2 defs but stopwords) pass the
    # definitions threshold; only "array" survives the stopword filter.
    assert candidate_words(analysis=analysis, min_definitions=2) == [
        ("array", WordStats(occurrences=9, definitions=3)),
    ]


def test_lemmatization_matches_plural_definition_names() -> None:
    # "trees" in prose is recognized as the definition "tree" and excluded,
    # while "roots" (no such definition here) stays in the base collection.
    definitions = [
        _definition(name="tree", content="Roots of trees."),
        _definition(name="byte", content="Bytes."),
    ]
    analysis = analyze(definitions=definitions)
    assert analysis.base_collection == ("of", "root")


def test_candidate_words_min_length() -> None:
    analysis = Analysis(
        definition_count=2,
        base_collection=("sum", "byte"),
        stats={
            "sum": WordStats(occurrences=2, definitions=2),
            "byte": WordStats(occurrences=2, definitions=2),
        },
    )
    assert [word for word, _ in candidate_words(analysis=analysis, min_definitions=2, min_length=4)] == ["byte"]
