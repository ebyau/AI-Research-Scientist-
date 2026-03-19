#!/usr/bin/env python3
"""Append a citation/provenance entry to memory/provenance/<project>.md."""
from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path
from textwrap import dedent

WORKSPACE = Path.home() / ".openclaw" / "workspace"
PROVENANCE_DIR = WORKSPACE / "memory" / "provenance"


def ensure_header(path: Path, project: str) -> None:
    if not path.exists():
        header = f"# {project.replace('-', ' ').title()} provenance\n\n"
        path.write_text(header)


def main() -> None:
    parser = argparse.ArgumentParser(description="Append a provenance entry to memory/provenance/<project>.md")
    parser.add_argument("--project", required=True, help="Slug for the project (filename will be <slug>.md)")
    parser.add_argument("--title", required=True, help="Title or key takeaway")
    parser.add_argument("--source", required=True, help="Source name (journal, repo, dataset, etc.)")
    parser.add_argument("--link", default="", help="URL or identifier")
    parser.add_argument("--summary", required=True, help="1-2 sentence summary of why this matters")
    parser.add_argument("--added-by", required=True, help="Agent adding the entry (e.g., Hard-guy)")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    args = parser.parse_args()

    PROVENANCE_DIR.mkdir(parents=True, exist_ok=True)
    project_slug = args.project.strip()
    path = PROVENANCE_DIR / f"{project_slug}.md"
    ensure_header(path, project_slug)

    timestamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    tags = ", ".join(t.strip() for t in args.tags.split(",") if t.strip())
    entry = dedent(
        f"""
        ## {timestamp} — {args.title}
        - Source: {args.source}
        - Link: {args.link or 'N/A'}
        - Added by: {args.added_by}
        - Tags: {tags or 'None'}
        - Summary: {args.summary}
        """
    ).strip()

    with path.open("a", encoding="utf-8") as fh:
        fh.write("\n" + entry + "\n")

    print(f"Saved entry to {path}")


if __name__ == "__main__":
    main()
