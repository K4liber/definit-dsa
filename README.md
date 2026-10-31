# DefinIT - Data Structures and Algorithms

## Install dev dependencies

```
uv sync --index https://pypi.org/simple --extra dev
```

## Run tests
```
uv run pytest
```

## Generate Markdown database
```
cd src
uv run python -m definit_db.serialize
```

## Analyze non-definition words

Analyzes all words used in the definitions that are not definitions themselves
(case-insensitive, punctuation-free, lemmatized) and reports the base collection,
the most common words and candidates for new definitions:

```
cd src
uv run python -m definit_db.analyze_words [--db PATH] [--top N] [--min-definitions M] [--output PATH]
```

Use `--output ../docs/word_analysis.md` to write the Markdown report to a file
instead of stdout (requires the database to be generated first).
