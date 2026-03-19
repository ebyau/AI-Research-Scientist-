# Memory & Provenance

## Files
- `MEMORY.md` — curated long-term facts (user preferences, environment notes, recurring decisions).
- `memory/YYYY-MM-DD.md` — daily log (auto-loaded into QMD-backed `memory_search`).
- `memory/provenance/<project>.md` — citation trails per project (created on demand).

## Logging workflow
1. **Durable notes:** When Dubois asks us to “remember” something, append it to `MEMORY.md` (or today’s daily file for transient context).
2. **Citations / datasets:** Run `python3 tools/log_citation.py --project <slug> --title "..." --source "..." --link "..." --summary "..." --added-by "Hard-guy" --tags "paper,baseline"` to append a structured entry under `memory/provenance/`.
3. **Searchability:** QMD indexes all of the above so `memory_search` returns provenance alongside summaries.

## Script reference
- `tools/log_citation.py` — appends provenance entries with timestamp, source, link, summary, and tags.
- `memory/provenance/README.md` — describes the folder layout for manual edits.

Keep using `memory_get`/`memory_search` to recall notes; QMD will blend Markdown memories with provenance trails for richer context.
