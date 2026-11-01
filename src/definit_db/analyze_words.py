"""Analyze words used in the definitions that are not definitions themselves.

Loads the markdown database, tokenizes the content of every definition
(case-insensitive, punctuation stripped) and lemmatizes tokens with a
best-effort offline English plural lemmatizer (no external API). Words that
match any definition name or alias (after lemmatization) are treated as
"definition words"; every other word forms the base collection of
non-definition words.

The analysis reports:

- the base collection: unique non-definition words, sorted alphabetically;
- occurrence statistics: how often each word appears in total and in how many
  distinct definitions it appears;
- the most common non-definition words (with and without English stopwords);
- candidate words that might deserve their own definition: non-stopwords that
  appear in at least ``min_definitions`` distinct definitions.

Run it with:

    cd src
    uv run python -m definit_db.analyze_words [--db PATH] [--top N]
        [--min-definitions M] [--output PATH]
"""

import argparse
import re
import sys
import textwrap
from collections import Counter
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from definit.db.md import DatabaseMd
from definit.definition.definition import Definition

_DEFAULT_DB_PATH = Path(__file__).parent / "data_md"
_DEFAULT_TOP = 50
_DEFAULT_MIN_DEFINITIONS = 5
_MIN_WORD_LENGTH = 2
_CANDIDATE_MIN_LENGTH = 3
_WRAP_WIDTH = 100

_TOKEN_PATTERN = re.compile(r"[a-z]+")
# Markdown links like [phrase](field/definition_id): keep the phrase (it is part of
# the prose) but drop the target (field/definition ids are not English words).
_MARKDOWN_LINK_PATTERN = re.compile(r"\[(?P<phrase>[^\]]*)\]\([^)]*\)")

_IRREGULAR_PLURALS = {
    "analyses": "analysis",
    "axes": "axis",
    "children": "child",
    "criteria": "criterion",
    "feet": "foot",
    "geese": "goose",
    "halves": "half",
    "indices": "index",
    "knives": "knife",
    "leaves": "leaf",
    "matrices": "matrix",
    "men": "man",
    "moduli": "modulus",
    "phenomena": "phenomenon",
    "radii": "radius",
    "teeth": "tooth",
    "vertices": "vertex",
    "women": "woman",
}

_STOPWORDS = frozenset(
    {
        "a",
        "about",
        "above",
        "after",
        "again",
        "against",
        "all",
        "am",
        "an",
        "and",
        "any",
        "are",
        "as",
        "at",
        "be",
        "because",
        "been",
        "before",
        "being",
        "below",
        "between",
        "both",
        "but",
        "by",
        "can",
        "could",
        "did",
        "do",
        "does",
        "doing",
        "down",
        "during",
        "each",
        "eg",
        "eight",
        "etc",
        "few",
        "five",
        "for",
        "four",
        "from",
        "had",
        "has",
        "have",
        "having",
        "he",
        "her",
        "here",
        "hers",
        "herself",
        "him",
        "himself",
        "his",
        "how",
        "ie",
        "if",
        "in",
        "into",
        "is",
        "it",
        "its",
        "itself",
        "just",
        "may",
        "me",
        "might",
        "more",
        "most",
        "must",
        "my",
        "nine",
        "no",
        "nor",
        "not",
        "now",
        "of",
        "off",
        "on",
        "once",
        "one",
        "only",
        "or",
        "other",
        "our",
        "ours",
        "out",
        "over",
        "own",
        "same",
        "seven",
        "she",
        "should",
        "six",
        "so",
        "some",
        "such",
        "ten",
        "than",
        "that",
        "the",
        "their",
        "them",
        "then",
        "there",
        "these",
        "they",
        "this",
        "those",
        "three",
        "through",
        "to",
        "too",
        "two",
        "under",
        "until",
        "up",
        "use",
        "used",
        "uses",
        "using",
        "very",
        "vs",
        "was",
        "we",
        "were",
        "what",
        "when",
        "where",
        "which",
        "while",
        "who",
        "whom",
        "why",
        "will",
        "with",
        "within",
        "without",
        "would",
        "you",
        "your",
    }
)


@dataclass(frozen=True)
class WordStats:
    """Occurrences of a non-definition word across the whole database."""

    occurrences: int
    definitions: int


@dataclass(frozen=True)
class Analysis:
    """Result of analyzing all definitions for non-definition words."""

    definition_count: int
    base_collection: tuple[str, ...]
    stats: dict[str, WordStats]


def strip_markdown_links(text: str) -> str:
    """Replace markdown links ``[phrase](target)`` with just the phrase."""
    return _MARKDOWN_LINK_PATTERN.sub(r"\g<phrase>", text)


def tokenize(text: str) -> list[str]:
    """Lowercase, strip punctuation and return alphabetic tokens of length >= 2."""
    tokens = _TOKEN_PATTERN.findall(strip_markdown_links(text).lower())
    return [token for token in tokens if len(token) >= _MIN_WORD_LENGTH]


def lemma(word: str) -> str:
    """Best-effort base form of a lowercase English word, focused on plurals."""
    if word in _IRREGULAR_PLURALS:
        return _IRREGULAR_PLURALS[word]
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if word.endswith(("ches", "shes", "sses", "xes")):
        return word[:-2]
    # Words ending in "ss", "us" or "is" are almost always singular already
    # (class, bus, axis, basis, analysis).
    if word.endswith(("ss", "us", "is")) or len(word) <= 3:
        return word
    if word.endswith("s"):
        return word[:-1]
    return word


def definition_word_lemmas(definitions: list[Definition]) -> set[str]:
    """Lemmas of all words appearing in any definition name or alias."""
    lemmas: set[str] = set()
    for definition in definitions:
        for word in tokenize(definition.key.name):
            lemmas.add(lemma(word))
        for alias in definition.aliases:
            for word in tokenize(alias):
                lemmas.add(lemma(word))
    return lemmas


def analyze(definitions: list[Definition]) -> Analysis:
    """Build the base collection of non-definition words with occurrence statistics."""
    known_lemmas = definition_word_lemmas(definitions)

    occurrences: Counter[str] = Counter()
    definitions_per_word: dict[str, set[str]] = defaultdict(set)

    for definition in definitions:
        for token in tokenize(definition.content):
            word = lemma(token)
            if word in known_lemmas:
                continue
            occurrences[word] += 1
            definitions_per_word[word].add(definition.key.uid)

    stats = {
        word: WordStats(occurrences=occurrences[word], definitions=len(definitions_per_word[word]))
        for word in occurrences
    }
    return Analysis(
        definition_count=len(definitions),
        base_collection=tuple(sorted(stats)),
        stats=stats,
    )


def most_common(
    analysis: Analysis,
    top: int = _DEFAULT_TOP,
    include_stopwords: bool = False,
) -> list[tuple[str, WordStats]]:
    """Most common non-definition words, ordered by total occurrences."""
    items = [(word, stats) for word, stats in analysis.stats.items() if include_stopwords or word not in _STOPWORDS]
    return sorted(items, key=lambda item: (-item[1].occurrences, -item[1].definitions, item[0]))[:top]


def candidate_words(
    analysis: Analysis,
    min_definitions: int = _DEFAULT_MIN_DEFINITIONS,
    min_length: int = _CANDIDATE_MIN_LENGTH,
) -> list[tuple[str, WordStats]]:
    """Non-definition words that might deserve their own definition.

    A word is a candidate when it is not a stopword, is at least ``min_length``
    characters long and appears in at least ``min_definitions`` distinct
    definitions. Ordered by the number of distinct definitions using the word.
    """
    candidates = [
        (word, stats)
        for word, stats in analysis.stats.items()
        if len(word) >= min_length and word not in _STOPWORDS and stats.definitions >= min_definitions
    ]
    return sorted(candidates, key=lambda item: (-item[1].definitions, -item[1].occurrences, item[0]))


def load_definitions(db_path: Path) -> list[Definition]:
    """Load all definitions of the markdown database at ``db_path``."""
    db = DatabaseMd(data_md_path=db_path, load_cache=True)
    keys = sorted(db.get_index(), key=lambda key: key.uid)
    return [db.get_definition(definition_key=key) for key in keys]


def _word_table(rows: list[tuple[str, WordStats]], occurrence_first: bool) -> list[str]:
    lines = []
    if occurrence_first:
        lines += ["| Word | Occurrences | Distinct definitions |", "| --- | ---: | ---: |"]
        lines += [f"| {word} | {stats.occurrences} | {stats.definitions} |" for word, stats in rows]
    else:
        lines += ["| Word | Distinct definitions | Occurrences |", "| --- | ---: | ---: |"]
        lines += [f"| {word} | {stats.definitions} | {stats.occurrences} |" for word, stats in rows]
    return lines


def build_report(
    analysis: Analysis,
    top: int = _DEFAULT_TOP,
    min_definitions: int = _DEFAULT_MIN_DEFINITIONS,
    db_path: Path | None = None,
) -> str:
    """Render the analysis as a Markdown report."""
    lines: list[str] = [
        "# Non-Definition Words Analysis",
        "",
    ]

    source = f"`{db_path}`" if db_path is not None else "in-memory definitions"
    lines += [
        f"Source database: {source} ({analysis.definition_count} definitions).",
        "",
        "Words are lowercased, stripped of punctuation and lemmatized with a best-effort offline"
        " English plural lemmatizer. Words matching any definition name or alias are treated as"
        " definition words and excluded from the base collection.",
        "",
    ]

    lines += [
        "## Base collection",
        "",
        f"{len(analysis.base_collection)} unique non-definition words, sorted alphabetically:",
        "",
    ]
    lines += textwrap.wrap(", ".join(analysis.base_collection), width=_WRAP_WIDTH)
    lines.append("")

    common = most_common(analysis=analysis, top=top)
    lines += [
        f"## Most common non-definition words (top {len(common)}, excluding stopwords)",
        "",
    ]
    lines += _word_table(rows=common, occurrence_first=True)
    lines.append("")

    common_raw = most_common(analysis=analysis, top=top, include_stopwords=True)
    lines += [
        f"## Most common non-definition words (top {len(common_raw)}, including stopwords)",
        "",
    ]
    lines += _word_table(rows=common_raw, occurrence_first=True)
    lines.append("")

    candidates = candidate_words(analysis=analysis, min_definitions=min_definitions)
    lines += [
        "## Candidate words for new definitions",
        "",
        f"Non-stopwords of length >= {_CANDIDATE_MIN_LENGTH} that appear in at least"
        f" {min_definitions} distinct definitions, ordered by how many distinct definitions use"
        " them. These are the words from the base collection most likely to deserve their own"
        " definition:",
        "",
    ]
    lines += _word_table(rows=candidates, occurrence_first=False)
    lines.append("")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Analyze words in the definitions that are not definitions themselves.",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=_DEFAULT_DB_PATH,
        help=f"Path to the markdown database directory (default: {_DEFAULT_DB_PATH}).",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=_DEFAULT_TOP,
        help=f"Number of most common words to list (default: {_DEFAULT_TOP}).",
    )
    parser.add_argument(
        "--min-definitions",
        type=int,
        default=_DEFAULT_MIN_DEFINITIONS,
        help=(
            "Minimum number of distinct definitions a word must appear in to be listed as a"
            f" candidate for a new definition (default: {_DEFAULT_MIN_DEFINITIONS})."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write the Markdown report to this file instead of printing it to stdout.",
    )
    args = parser.parse_args(argv)

    if not args.db.exists():
        parser.error(
            f"Database path does not exist: {args.db}."
            " Generate it first: cd src && uv run python -m definit_db.serialize",
        )

    definitions = load_definitions(db_path=args.db)
    analysis = analyze(definitions=definitions)
    report = build_report(
        analysis=analysis,
        top=args.top,
        min_definitions=args.min_definitions,
        db_path=args.db,
    )

    if args.output is None:
        sys.stdout.write(report)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Report written to {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
