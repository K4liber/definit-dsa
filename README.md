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
