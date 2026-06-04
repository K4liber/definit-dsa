"""Generate ``index_review.md`` from the markdown database.

TODO(K4liber): remove the script after review is done

For every definition listed in ``data_md/index.md`` this script writes a
matching line in ``data_md/index_review.md`` with a checkbox in front of the
definition name. A definition is considered *reviewed* (``[x]``) when its
generated markdown file contains a standalone ``---`` separator, which marks
the presence of an example. Otherwise the checkbox is left empty (``[ ]``).

The script first regenerates the markdown database so the review index always
reflects the latest definitions. Run it after adding or changing definitions:

    uv run python scripts/generate_index_review.py
"""

from __future__ import annotations

import re
from pathlib import Path

from definit_db.serialize import serialize

_INDEX_LINE = re.compile(r"- \[(.+?)\]\((.+?)\)")


def generate_index_review() -> Path:
    """Regenerate the markdown database and write ``index_review.md``.

    Returns the path to the generated ``index_review.md`` file.
    """
    base = serialize()
    defs_dir = base / "definitions"
    index = (base / "index.md").read_text(encoding="utf-8")

    out_lines: list[str] = []
    reviewed = 0
    total = 0
    for line in index.splitlines():
        match = _INDEX_LINE.match(line)
        if match is None:
            continue
        total += 1
        name, path = match.group(1), match.group(2)
        md_file = defs_dir / f"{path}.md"
        has_example = False
        if md_file.exists():
            content = md_file.read_text(encoding="utf-8")
            has_example = any(text.strip() == "---" for text in content.splitlines())
        if has_example:
            reviewed += 1
        box = "[x]" if has_example else "[ ]"
        out_lines.append(f"- {box} [{name}]({path})")

    review_file = base / "index_review.md"
    review_file.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"Wrote {total} definitions, {reviewed} reviewed (have example) to {review_file}.")
    return review_file


if __name__ == "__main__":
    generate_index_review()
